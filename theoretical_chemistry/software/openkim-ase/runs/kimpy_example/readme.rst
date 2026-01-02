kimpy example
=============


https://github.com/openkim/kimpy/issues/27#issuecomment-2211562705


milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/.python3 kimpy_example.py
  Distance           Energy
  1.0000000000e+00   8.3309698035e+00
  1.5000000000e+00   4.0612306870e+00
  2.0000000000e+00   1.8021700693e-02
  2.5000000000e+00  -1.9353325249e+00
  3.0000000000e+00  -1.7714986219e+00
  3.5000000000e+00  -1.1478765871e+00
  4.0000000000e+00  -4.9042072724e-01
  4.5000000000e+00  -2.0418576357e-01
  5.0000000000e+00  -1.1762679400e-01
  5.5000000000e+00  -5.0038462875e-03
  6.0000000000e+00   0.0000000000e+00

MiroPhenomII-X6
---------------
miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/.source ~/software/venv/bin/activate
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/.python kimpy_example.py
Traceback (most recent call last):
  File "/home/miroi/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/kimpy_example.py", line 4, in <module>
    import kimpy
ModuleNotFoundError: No module named 'kimpy'
(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/.pip install kimpy
Collecting kimpy
  Using cached kimpy-2.1.3.tar.gz (49 kB)
.
.

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/.python kimpy_example.py
Traceback (most recent call last):
  File "/home/miroi/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/runs/kimpy_example/kimpy_example.py", line 37, in <module>
    units_accepted, kim_model = kimpy.model.create(
                                ^^^^^^^^^^^^^^^^^^^
RuntimeError: Unable to create a new KIM-API Model object!



