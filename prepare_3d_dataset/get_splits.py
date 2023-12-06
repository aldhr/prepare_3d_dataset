import deepchem as dc
import numpy as np
import pandas as pd
import yaml

""" this script uses fingerprintspliter from deepchem
to perform splits accordingly to tanimoto similarity"""

# Read the configuration file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    
df = pd.read_csv(config['dataset_path'])

# creation of data set with smiles strings
list_of_smiles = df['smiles'].tolist()
Xs = np.zeros(len(list_of_smiles))

# creation of a deepchem dataset with the smile codes in the ids field
dataset = dc.data.DiskDataset.from_numpy(X=Xs, ids=list_of_smiles)
fingerprintsplitter = dc.splits.FingerprintSplitter()
train_idx, valid_idx, test_idx = fingerprintsplitter.split(dataset)

# add a column named split
df['split'] = ''
df.loc[df.index.isin(train_idx), 'split'] = 'train'
df.loc[df.index.isin(valid_idx), 'split'] = 'val'
df.loc[df.index.isin(test_idx), 'split'] = 'test'
df.to_csv(config['dataset_path'], index=False)

