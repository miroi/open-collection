================
QE input to VASP
================

from ase.io import read, write
# Read QE input
structure = read('Se54_r_Fl_2steprelax.in', format='espresso-in')
# Write VASP POSCAR
write('FlSe54.vasp', structure, format='vasp', vasp5=True, direct=True)


