================
ase-driven mopac 
================

from Dip, /lustre/home/user/d/dsen/Documents/2_example/mopac_example/3_ASE_MOPAC

ASE MOPAC final script - 
1) reads input structure from pdb file 
2) optimizes and saves the final structure in pdb and xyz format 
3) reports final heat of formation and forces in stdout

last days calculations with 0.01 force tolerance was taking too much time,
so I (Dip) finalized the script with lower 0.1 ev force tolerance for testing. 

For production calculations we have to check what sort of tolerance people use in papers.
