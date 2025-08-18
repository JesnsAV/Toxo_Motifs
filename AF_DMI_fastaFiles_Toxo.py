#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2 July 2025

@author: Jesus Alvarado Valverde
"""

import os
import numpy as np
import re
import argparse
import pandas as pd
import warnings

'''
Make a list of all proteins in the Toxoplasma proteome
IDs are the dictionary keys
'''

os.chdir('/Data/')

ToxoProteome = 'ToxoDB-68_TgondiiME49_AnnotatedProteins.fasta' #File with information on Proteins 
    
proteins_file = open(ToxoProteome, 'r') #open up file
proteins_seqs = {}

for line in proteins_file: #for every line in the protein file     
    if line.startswith(">"):
        row = line.strip()
        row_parts = row.split("|")
        ID = row_parts[2].replace(" gene=", "").strip() # Get the ID
        
        proteins_seqs[ID] = [""]
    else:
        row = line.strip()
        proteins_seqs[ID][0] = proteins_seqs[ID][0] + row # Add characters to protein sequence
        
del row, line, ID


'''
Get Motif boundary information and select unique protein pair IDs
'''


# Motif information
Motif_info = pd.read_table('Motif_table.tsv')
Motif_info = Motif_info.dropna(subset=['start'])

Motif_proteins = Motif_info["ID"].unique().tolist()

'''
Get Domain sequences
'''

# Human domain information
Domain_info = pd.read_table('Domain_seqs.tsv')

'''
Produce a table with the Fasta files' limits
'''
out_file = open('ToxoHuman_DMI_fragment_boundaries.txt',"w")

out_file.write('HumanDomainProtein\tDomainID1\tdomain_start\tdomain_end\tToxoMotifProtein\tMotifAccession\tELM_start\tELM_end\tmotif_start\tmotif_end\n' ) 
for index, row in Motif_info.iterrows():
    domain_tb = Domain_info.loc[Domain_info['Motif_Name'] == row.Motif_Name ]
    for index_d, row_d in domain_tb.iterrows():
        domain_info = row_d.ID.split('_')
        domainProtein = domain_info[0]
        domainID = domain_info[1]
        domain_start = domain_info[3]
        domain_end = domain_info[4] 
        
        motifProtein = row.ID # Motif ID
        motifID = row.Motif_Accession # Motif ID
        motif_start = row.start 
        motif_end = row.start + len(row.sequence) - 1 
        if motif_start > 4:
            m_s = int(motif_start)-5
        else:
            m_s = 1
        
        if motif_end < len(proteins_seqs[motifProtein][0])-4:
            m_e = int(motif_end) + 5
        else:
            m_e = len(proteins_seqs[motifProtein][0])
            
        out_file.write(f'{domainProtein}\t{domainID}\t{domain_start}\t{domain_end}\t{motifProtein}\t{motifID}\t{m_s}\t{m_e}\n' ) 
        

out_file.close()


'''
Produce fasta files with protein fragment pairs
'''
os.chdir('Fastas')

for index, row in Motif_info.iterrows():
    domain_tb = Domain_info.loc[Domain_info['Motif_Name'] == row.Motif_Name ]
    for index_d, row_d in domain_tb.iterrows():
        domain_info = row_d.ID
        domain_seq = row_d.sequence
        
        motifProtein = row.ID # Motif ID
        motifID = row.Motif_Accession # Motif ID
        motif_start = row.start 
        motif_end = row.start + len(row.sequence) - 1
        if motif_start > 4:
            m_s = int(motif_start)-5
        else:
            m_s = 1
        
        if motif_end < len(proteins_seqs[motifProtein][0])-4:
            m_e = int(motif_end) + 5
        else:
            m_e = len(proteins_seqs[motifProtein][0])
            
        motif_seq = proteins_seqs[motifProtein][0][m_s-1:m_e] # Motif sequence plus flanking regions
        
        motif_info = motifProtein + '_' + motifID + '_D_' + str(m_s) + '_' + str(m_e)
        
        out_file = open(f'{domain_info}.{motif_info}.fasta',"w")
        out_file.write(f'>{domain_info}\n' ) 
        out_file.write(f'{domain_seq}\n' ) 
        out_file.write(f'>{motif_info}\n' ) 
        out_file.write(f'{motif_seq}' ) 
        out_file.close()






