CO molecule optimization
=========================


based on 
https://www.youtube.com/watch?v=hUVu7Kcs7Tc

datasets
~~~~~~~~~
see https://gpaw.readthedocs.io/setups/setups.html#installation-of-paw-datasets

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/.wget https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-24.1.0.tar.gz

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/gpaw-setups-24.1.0/.cp C.PBE.gz  O.PBE.gz /home/miroi/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/runs/CO_molecule_gemopt/.

https://gpaw.readthedocs.io/setups/generation_of_setups.html#using-your-own-setups

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/runs/CO_molecule_gemopt/.python3 CO_relax.py
/home/miroi/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/runs/CO_molecule_gemopt/CO_relax.py:19: DeprecationWarning: Please use atoms.calc = calc
  atoms.set_calculator(calc)
/home/miroi/.local/lib/python3.10/site-packages/gpaw/calculator.py:730: DeprecatedParameterWarning: Finite-difference mode implicitly chosen; it will be an error to not specify a mode in the future
  warnings.warn(

