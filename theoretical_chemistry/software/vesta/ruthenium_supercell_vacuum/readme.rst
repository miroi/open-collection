=============================================================
Supercell construction and adding Vacuum in Vesta - Ruthenium
=============================================================

based on video
~~~~~~~~~~~~~~~

https://www.youtube.com/watch?v=Jk0QUB1fkMU


download cif
~~~~~~~~~~~~
https://next-gen.materialsproject.org/materials/mp-8639 ... download Ru.cif


notes
~~~~~

only cif, vesta  and vasp files contain lattice parameters !!! export as cif

Vesta exported xyz,pdb  do not contain lattice params !!!

OpenBabelGUI: convert Vesta vasp --> pdb file, this contains lattice params 


cif2cell
~~~~~~~~

cif2cell -f Ru_supercell_with_vacuum.cif  -p quantum-espresso



