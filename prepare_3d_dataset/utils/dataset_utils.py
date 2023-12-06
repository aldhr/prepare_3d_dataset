from rdkit import Chem
import requests  
from rdkit.Chem import MolStandardize

#1
def generate_smiles_from_pdb_bank(id): ## ID is the name of the ligand in original [crystal] pdb
    """Generate SMILES string for a given ligand ID."""
    try:
        response = requests.get(f"https://files.rcsb.org/ligands/download/{id}_ideal.sdf")
        if response.status_code == 200:
            sdf_data = response.text
            mol_supplier = Chem.SDMolSupplier()
            mol_supplier.SetData(sdf_data)
            mol = next(mol_supplier)
            if mol is not None:
                standardizer = MolStandardize.Standardizer()
                standardized_mol = standardizer.standardize(mol)
                smiles = Chem.MolToSmiles(standardized_mol, isomericSmiles=False)     ##isomericSmiles=True keeps 3d space somehow    
                return smiles
    except Exception as e:
        print(f"Error processing {id}: {str(e)}")
    return None

