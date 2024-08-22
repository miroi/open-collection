==========================
Ramping up the temperature
==========================

In this example, a small cubic nanoparticle is melted by increasing the temperature stepwise. 
Five plots are generated at each temperature using PrimiPlotter

https://asap3.readthedocs.io/en/latest/examples/Ramping_up_the_temperature.html


error https://gitlab.com/asap/asap/-/issues/61

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/asap3-ase/runs/melting_asap3/.python3 Melting.py
/usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.26.4
  warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion}"
Traceback (most recent call last):
  File "/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/asap3-ase/runs/melting_asap3/Melting.py", line 8, in <module>
    from ase.visualize.primiplotter import PrimiPlotter, PngFile
ModuleNotFoundError: No module named 'ase.visualize.primiplotter'

fixed version
~~~~~~~~~~~~~
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/asap3-ase/runs/melting_asap3/.python3 Melting_modif.py  > Melting_modif.logfile
/usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3 and <1.25.0 is required for this version of SciPy (detected version 1.26.4
  warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion}"
Using Asap-optimized C++-Langevin algorithm
/usr/lib/python3/dist-packages/ase/md/md.py:48: FutureWarning: Specify the temperature in K using the 'temperature_K' argument
  warnings.warn(FutureWarning(w))

