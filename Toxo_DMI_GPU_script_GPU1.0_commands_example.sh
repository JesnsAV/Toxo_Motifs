#! /bin/bash

python3 /fsimb/groups/imb-luckgr/imb-luckgr2/projects/AlphaFold/scripts/organize_computed_msas.py -computed_msas_path /fsimb/groups/imb-luckgr/imb-luckgr2/projects/AlphaFold/computed_msas/ -run_path /fsimb/groups/imb-luckgr/imb-luckgr2/projects/AlphaFold/Toxoplasma/AF_predictions/

NVIDIA_VISIBLE_DEVICES=6 time singularity run --contain --nv --nvccli --writable-tmpfs --bind /home,/fsimb,/media,/mnt,/tmp /mnt/storage/alphafold/v232/alphafold_2.3.2.sif \
--fasta_paths=/fsimb/groups/imb-luckgr/imb-luckgr2/projects/AlphaFold/Toxoplasma/AF_predictions/FILE_NAME.fasta

--output_dir=/fsimb/groups/imb-luckgr/imb-luckgr2/projects/AlphaFold/Toxoplasma/AF_predictions/ \
--model_preset=multimer \
--db_preset=full_dbs \
--max_template_date=2020-05-14 \
--num_multimer_predictions_per_model=1 \
--use_gpu_relax=True \
--data_dir=/mnt/storage/alphafold/v232 \
--bfd_database_path=/mnt/storage/alphafold/v232/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
--mgnify_database_path=/mnt/storage/alphafold/v232/mgnify/mgy_clusters_2022_05.fa \
--obsolete_pdbs_path=/mnt/storage/alphafold/v232/pdb_mmcif/obsolete.dat \
--pdb_seqres_database_path=/mnt/storage/alphafold/v232/pdb_seqres/pdb_seqres.txt \
--template_mmcif_dir=/mnt/storage/alphafold/v232/pdb_mmcif/mmcif_files \
--uniprot_database_path=/mnt/storage/alphafold/v232/uniprot/uniprot.fasta \
--uniref90_database_path=/mnt/storage/alphafold/v232/uniref90/uniref90.fasta \
--uniref30_database_path=/mnt/storage/alphafold/v232/uniref30/UniRef30_2021_03 \
--use_precomputed_msas=True