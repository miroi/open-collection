======
Og 
======

install
~~~~~~~
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/.source
~/work/software/venv/bin/activate
(venv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/.

(venv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/.sudo apt-get install libkim-api-dev   openkim-models

(venv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/.pip install -U --no-deps kimpy
.
.
Successfully built kimpy
Installing collected packages: kimpy
Successfully installed kimpy-2.1.1


runs
~~~~
python3 Og_fcc_poten.py
3D Og fcc potential energy: -2.67564203880867 eV

python3 Og_hcp_poten.py
Og hcp cell  Cell([[5.25, 0.0, 0.0], [-2.625, 4.546633369868303, 0.0], [0.0, 0.0, 8.573214099741124]])
3D Og hcp potential energy: -0.023000632064852727 eV

(venv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/.py
thon3 Og_fcc_optimize_lattice.py
^[[DOg fcc cell befor optimization:
[4.24264069 4.24264069 4.24264069] [60. 60. 60.]
Og fcc potential energy before opt: -0.04071359421179172 eV
/home/miroi/work/projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/rare_gas_fcc_tests/Og_fcc_optimize_lattice.py:21: FutureWarning: Import StrainFilter from ase.filters
  Og_fcc = StrainFilter(Og_fcc)
      Step     Time          Energy          fmax
BFGS:    0 23:34:57       -0.040714        0.132869
BFGS:    1 23:34:57       -0.040967        0.133600
BFGS:    2 23:34:57       -0.079685        0.232025
BFGS:    3 23:34:57       -0.144201        0.245894
BFGS:    4 23:34:57       -0.055923        1.637809
BFGS:    5 23:34:57       -0.151980        0.203546
BFGS:    6 23:34:57       -0.156626        0.155064
BFGS:    7 23:34:57       -0.158735        0.152213
BFGS:    8 23:34:57       -0.160892        0.037336
Og fcc cell AFTER optimization:
[3.07116472 3.07116472 3.07116472] [60. 60. 60.]
Og fcc potential energy AFTER opt: -0.16089153579510446 eV



