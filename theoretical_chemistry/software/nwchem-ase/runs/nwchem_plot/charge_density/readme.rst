===========
NWChem plot
===========


mpirun -np 2 nwchem n2.scf_chdens.nw > n2.scf_chdens.logfile


open chargedensity.cube in  : Avogadro2, VESTA, ase 

ase gui chargedensity.cube


