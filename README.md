# Toxo_Motifs
Code to predict short linear motifs in the Toxoplasma gondii proteome


### Motif prediction
MM_RawPrediction.py

`python ../Software/MM_RawPrediction.py 'ALIAS' ../Data/ToxoDB-42_TgondiiME49_AnnotatedProteins.fasta ../Data/elm_classes.tsv 0.4`
 
 Dependencies:
 - IUPred3 library (https://iupred3.elte.hu/)
 
 Inputs:
- Parasite proteome: header fasta format from ToxoDB
- ELM classes table: containing motif name, REGEX in parentheses, and motif probability 

 Outputs:
- Table of motif predictions with: Protein ID, motif name, match number, motif sequence, motif start, IUPred3 score, disorder context


### Motif presence in MSAs
MM_sites.R
`rscript ./Software/MM_sites.R  ../Data/ALIAS_MM_list.txt`

MM_InAlignments.py 
`python ../Software/MM_InAlignments.py elm_classes.tsv ALIAS_MM_sites.txt `

 Inputs:
- Table of motif predictions
- ELM classes table: containing motif name, REGEX in parentheses, and motif probability 
- Multiple sequence alignment directory (within Data folder): MSAs in fasta format 

 Outputs:
- Table of motif predictions with protein and motif information, as well as columns for presence fraction among organisms, strains, and species. A value of 0 indicates the motif is only present in the reference strain, and a value of 1 indicates the motif is present in all other organisms/strains/species.

