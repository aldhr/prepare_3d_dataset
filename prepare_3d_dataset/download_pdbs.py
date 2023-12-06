## download pdbs
""" Download pdb files | This script uses batch download from RCSB
    it createa new folder within structure. df contains IDs in first
    column to be downloaded
"""

import os
import pandas as pd
import yaml
import subprocess
import shutil


# Read the configuration file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Read the dataset
dataset = pd.read_csv(config['dataset_path'], sep=',')

# Get the PDB IDs from the DataFrame column
pdb_ids = dataset.iloc[:, 0].tolist()

# Create a file-comma-separeted of PDB IDs
with open('pdb_ids.txt', 'w') as pdb_id_file:
    pdb_id_file.write(','.join(pdb_ids))

# Create a directory for saving PDB files
os.makedirs(config['structures_downloaded'], exist_ok=True)

# Run batch download script with tqdm progress bar
subprocess.run(['./pdb_batch_download.sh', '-f', 'pdb_ids.txt', '-o', config['structures_downloaded'], '-p'])

## de-compress all files
os.system(f'gunzip {config["structures_downloaded"]}/*.pdb.gz')


