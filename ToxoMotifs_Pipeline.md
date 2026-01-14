
# Toxomotifs3 Codes and pipeline

## Motifs Raw Predictions
```
python   ../Software/MM_RawPrediction.py   ALIAS   Proteomes/ToxoDB-67/ToxoDB-67_TgondiiME49_AnnotatedProteins.fasta   elm_classes_Dec2023.tsv 0.4
```

## Reformatting motif match sites
```
Rscript 	MotifMatches_Sites.R	ALIAS_MotifMatches_list.txt
```

## Alignments
Download ToxoDB release 67
[Link](https://toxodb.org/toxo/app/downloads)

Join proteomes files
```
cat ToxoDB-67_*.fasta > Sarcocystidae.fasta
```

Create Blast database using all Sarcocystidae proteomes
```
makeblastdb -in Sarcocystidae.fasta -dbtype prot -title Sarcocystidae
```

Get TgondiiME49 IDs in a single textfile
```
grep ">" ToxoDB-67_TgondiiME49_AnnotatedProteins.fasta | awk '{print $1}' | sed 's/>//g'  > TgondiiME49_ID.txt
```

Get TgondiiME49 Descriptions in a single textfile
```
grep ">" ToxoDB-67_TgondiiME49_AnnotatedProteins.fasta | awk -F '|' '{print $3, $5, $8}' | sed 's/ gene=//g' | sed 's/ gene_product=//g'| sed 's/ protein_length=//g' > TgondiiME49_Descriptions.txt
```

Create Blast tables for all TgondiiME49 proteins
```
sh runblast.sh TgondiiME49_ID.txt
```

Code looping over textfile IDs
```
awk '/'"$name"'/{flag=1;print $0;next}/^>/{flag=0}flag' ToxoDB-67_TgondiiME49_AnnotatedProteins.fasta > temp.fasta
psiblast -db Sarcocystidae.fasta -query temp.fasta -evalue=0.00000001 -out Tables/Unfiltered/"$name".txt -outfmt "6 qseqid sseqid evalue pident qlen slen"
```


Get all seqIDs and gene IDs in a single textfile
```
ls ToxoDB-67_*.fasta | while read line; do grep ">" $line | awk -F '|' '{print $1, $3}' | sed 's/\>//g' | sed 's/ gene=//g' >> Sarcocystidae_IDs.txt; done
#be careful to only execute once as it might lead to repetitions of the IDs
```

Filtered Blast result tables to create standard groups and text files with seqIDs

Combine all blast results into a single table
```
cat TGME49_* > UnfilteredTables.txt
```

Create groups for each ID
- Filter out ME49 paralogs
- Retain the sequence of each other strain with the lowest E-value
- Create a text file for each group with the IDs of each sequence 
`Blast_tables.R` 


Create Alignments
- Retrieve sequences using Filtered tables and create fastas
- Run Clustal
```
sh create_fastaGroups.sh TgondiiME49_ID.txt
```

### Search motifs in Alignments
```
python ../Software/MM_Alignments.py ../Data/elm_classes_Dec2023.tsv ALIAS_MotifMatches_sites.txt 
```




