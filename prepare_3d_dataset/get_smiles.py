## get ligands smiles
import pandas as pd
from utils.dataset_utils import generate_smiles_from_pdb_bank
import yaml

""" this script takes a defined function to grep smiles
and append them to df based on RCSB search of three
letter codes of ligands"""

# Read the configuration file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    
df = pd.read_csv(config['dataset_path'])

# function to apply 'generate_smiles_from_pdb_bank' to each row
def get_smiles(row):
    ligand_id = row['lig_id']
    smiles = generate_smiles_from_pdb_bank(ligand_id)
    return smiles

# Apply the function to each row and create a new 'smiles' column
df['smiles'] = df.apply(get_smiles, axis=1)

df.to_csv(config['dataset_path'], index=False)
