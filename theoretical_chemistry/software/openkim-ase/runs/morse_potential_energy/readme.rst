OpenKIM example
===============

https://wiki.fysik.dtu.dk/ase/ase/calculators/kim.html


As an example, suppose we want to know the potential energy predicted by the example model “ex_model_Ar_P_Morse_07C” for an FCC argon lattice at a lattice spacing of 5.25 Angstroms. This can be accomplished in a manner similar to how most other ASE calculators are used, where the name of the KIM model is passed as an argument:

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/openkim-ase/runs/morse_potential_energy/.python3 morse.py
/usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.26.4
  warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion}"
Potential energy of FCC Ar: -0.37120682093323026 eV


milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/openkim-ase/runs/morse_potential_energy/.pip install lammps
Defaulting to user installation because normal site-packages is not writeable
Collecting lammps
  Downloading lammps-2023.8.2.3.1-py2.py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (81.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 81.9/81.9 MB 33.5 MB/s eta 0:00:00
Installing collected packages: lammps
Successfully installed lammps-2023.8.2.3.1


MiroPhenomII-X6
---------------
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/morse_potential_energy/.python morse.py
Potential energy of FCC Ar: -0.37120682093323026 eV

venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/morse_potential_energy/.python au_fcc_lammps.py
Traceback (most recent call last):
  File "/home/miroi/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/morse_potential_energy/au_fcc_lammps.py", line 11, in <module>
    energy = atoms.get_potential_energy()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/atoms.py", line 1950, in get_potential_energy
    energy = self._calc.get_potential_energy(self)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/calculators/abc.py", line 26, in get_potential_energy
    return self.get_property(name, atoms)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/calculators/calculator.py", line 519, in get_property
    self.calculate(atoms, [name], system_changes)
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/calculators/lammpslib.py", line 384, in calculate
    self.propagate(atoms, properties, system_changes, 0)
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/calculators/lammpslib.py", line 403, in propagate
    self.start_lammps()
  File "/home/miroi/software/venv/lib/python3.12/site-packages/ase/calculators/lammpslib.py", line 661, in start_lammps
    from lammps import LMP_STYLE_ATOM, LMP_TYPE_VECTOR, lammps
ModuleNotFoundError: No module named 'lammps'
