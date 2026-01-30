==========================
Windows 10 MiroPhenomII-X6
==========================

MS DOS Window
-------------
C:\Users\miroi> C:\Users\miroi\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip

C:\Users\miroi>pip install ase

Installing collected packages: six, pyparsing, pillow, packaging, numpy, kiwisolver, fonttools, cycler, scipy, python-dateutil, contourpy, matplotlib, ase
  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts' which is not on PATH.

   ------------------ ---------------------  6/13 [fonttools]  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script ase.exe is installed in 'C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts' which is not on PATH.

Successfully installed ase-3.27.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.61.1 kiwisolver-1.4.9 matplotlib-3.10.8 numpy-2.4.0 packaging-25.0 pillow-12.1.0 pyparsing-3.3.1 python-dateutil-2.9.0.post0 scipy-1.16.3 six-1.17.0

C:\Users\miroi\Desktop\Git-projects\open-collection\theoretical_chemistry\software\ase\buildup_on_servers\windows10\MiroPhenomII-X6>pip show ase
Name: ase
Version: 3.27.0
Summary: Atomic Simulation Environment
Home-page: https://ase-lib.org/
Author:
Author-email:
License-Expression: LGPL-2.1-or-later
Location: C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages
Requires: matplotlib, numpy, scipy
Required-by:

C:\Users\miroi\Desktop\Git-projects\open-collection\theoretical_chemistry\software\ase\buildup_on_servers\windows10\MiroPhenomII-X6\tests>pip list
Package         Version
--------------- -----------
ase             3.27.0
contourpy       1.3.3
cycler          0.12.1
fonttools       4.61.1
kiwisolver      1.4.9
matplotlib      3.10.8
numpy           2.4.0
packaging       25.0
pillow          12.1.0
pip             25.3
pyparsing       3.3.1
python-dateutil 2.9.0.post0
scipy           1.16.3
six             1.17.0


C:\Users\miroi\Desktop\Git-projects\open-collection\theoretical_chemistry\software\ase\buildup_on_servers\windows10\MiroPhenomII-X6\tests>C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\ase -h
Traceback (most recent call last):
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\_core\__init__.py", line 22, in <module>
    from . import multiarray
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\_core\multiarray.py", line 11, in <module>
    from . import _multiarray_umath, overrides
ImportError: DLL load failed while importing _multiarray_umath: A dynamic link library (DLL) initialization routine failed.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\ase.exe\__main__.py", line 2, in <module>
    from ase.cli.main import main
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\ase\__init__.py", line 8, in <module>
    import ase.parallel  # noqa
    ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\ase\parallel.py", line 11, in <module>
    import numpy as np
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py", line 125, in <module>
    from numpy.__config__ import show_config
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__config__.py", line 4, in <module>
    from numpy._core._multiarray_umath import (
    ...<3 lines>...
    )
  File "C:\Users\miroi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\_core\__init__.py", line 83, in <module>
    raise ImportError(msg) from exc
ImportError:

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python 3.13 from "C:\Users\miroi\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe"
  * The NumPy version is: "2.4.0"

and make sure that they are the versions you expect.

Please carefully study the information and documentation linked above.
This is unlikely to be a NumPy issue but will be caused by a bad install
or environment on your machine.

Original error was: DLL load failed while importing _multiarray_umath: A dynamic link library (DLL) initialization routine failed.
