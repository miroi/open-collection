==================
HF with ase-nwchem
==================

lias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/nwchem-ase/runs/HF/ase_run/.python3 HF_ase_nwchem.py
[0] ARMCI Warning: Freed 1 leaked allocations
HF PBE run, d(HF)= 0.91 Ang; Energy= -2730.5740514669287  eV
total energy = -2730.5740514669287
<ase.calculators.nwchem.NWChem object at 0x7f01f939bfa0>
atomic numbers array: [1 9]
dipole moment : [-0.         -0.         -0.44812472]
chemical formula : HF
Traceback (most recent call last):
  File "/home/milias/work/git-projects/open-collection/theoretical_chemistry/software/nwchem-ase/runs/HF/ase_run/HF_ase_nwchem.py", line 24, in <module>
    print('atomic mulliken charges :',hf.get_charges())
  File "/home/milias/.local/lib/python3.10/site-packages/ase/atoms.py", line 703, in get_charges
    return self._calc.get_charges(self)
  File "/home/milias/.local/lib/python3.10/site-packages/ase/calculators/abc.py", line 45, in get_charges
    return self.get_property('charges', atoms)
  File "/home/milias/.local/lib/python3.10/site-packages/ase/calculators/calculator.py", line 517, in get_property
    raise PropertyNotImplementedError(
ase.calculators.calculator.PropertyNotImplementedError: charges property not implemented

