##%cd Tutorials

from ase.io import read, write
import numpy as np

# from https://github.com/ilyes319/mace-tutorials/tree/main/mace-users/data
#db = read('data/solvent_configs.xyz', ':') #read in list of configs
db = read('solvent_mace_small1_train.xyz', ':') #read in list of configs

print("Number of configs in database: ", len(db))
print("Number of atoms in each config: ", np.array([len(at) for at in db]))
print("Number of atoms in the smallest config: ", np.min([len(at) for at in db])) #test if database contains isolated atoms
print("Information stored in config.info: \n", db[10].info) #check info
print("Information stored in config.arrays: \n", db[10].arrays)
