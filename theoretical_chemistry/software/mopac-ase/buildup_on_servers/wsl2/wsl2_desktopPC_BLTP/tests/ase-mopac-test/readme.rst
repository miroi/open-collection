================
ASE-driven MOPAC
================


fix:

No 'label' parameter: ASE will generate distinct, clean filenames for each step, forcing MOPAC to read the fresh coordinates instead of reading a cached geometry.molecule('H2O'): Generates a standard, un-trapped water geometry out of the box.


water_pm7_asegeopt_07.py
-------------------------
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/tests/ase-mopac-test/.python  water_pm7_asegeopt_07.py
--- Computational Environment ---
MOPAC Executable : /usr/bin/mopac
MOPAC Version    : MOPAC v22.0.6 Linux

--- Thermodynamic Results ---
Heat of Formation: -57.79985 kcal/mol

--- Net Atomic Charges ---
Atom  1 (O ) : -0.649360 e
Atom  2 (H ) : 0.324681 e
Atom  3 (H ) : 0.324679 e

--- Optimized Geometry Results ---
O-H1 Bond Length : 0.969 Å
O-H2 Bond Length : 0.969 Å
H-O-H Bond Angle : 104.0°

Optimization log saved to 'optimization.log'


Errors!
-------
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/tests/ase-mopac-test/.python   water_pm7_asegeopt_07.py
Traceback (most recent call last):
  File "/home/milias/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/tests/ase-mopac-test/water_pm7_asegeopt_07.py", line 32, in <module>
    opt.run(fmax=0.01)
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/optimize/optimize.py", line 506, in run
    return Dynamics.run(self, steps=steps)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/optimize/optimize.py", line 375, in run
    for converged in Dynamics.irun(self, steps=steps):
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/optimize/optimize.py", line 322, in irun
    gradient = self.optimizable.get_gradient()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/optimize/optimize.py", line 38, in get_gradient
    return -self.atoms.get_forces().ravel()
            ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/atoms.py", line 1994, in get_forces
    forces = self._calc.get_forces(self)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/calculators/abc.py", line 32, in get_forces
    return self.get_property('forces', atoms)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/calculators/calculator.py", line 519, in get_property
    self.calculate(atoms, [name], system_changes)
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/calculators/calculator.py", line 1163, in calculate
    self.read_results()
  File "/home/milias/work/software/venv/lib/python3.12/site-packages/ase/calculators/mopac.py", line 216, in read_results
    raise ReadError
ase.calculators.calculator.ReadError

