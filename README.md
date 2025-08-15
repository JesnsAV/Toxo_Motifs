# Toxo_Motifs
Code to predict short linear motifs in the Toxoplasma gondii proteome


### Initial motif prediction
MM_RawPrediction.py

`python ../Software/MotifMatches_RawPrediction.py 'ALIAS' ../Data/ToxoDB-42_TgondiiME49_AnnotatedProteins.fasta ../Data/elm_classes.tsv 0.4`
 
 Dependencies:
 - IUPred3 library (https://iupred3.elte.hu/)
 
 Inputs:
- Parasite proteome: header fasta format from ToxoDB
- ELM classes table: containing motif name, REGEX in parentheses, and motif probability 

 Outputs:
- Table of motif predictions with: Protein ID, motif name, match number, motif sequence, motif start, IUPred3 score, disorder context
