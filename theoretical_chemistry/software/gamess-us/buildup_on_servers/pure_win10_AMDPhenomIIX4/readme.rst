======================
GAMESS-US on Windows10
======================

on AMD Phenom II X4 965 one can not install WSL2 !

only Windows version of GMS can be installed

installation on MS Windows:

https://www.msg.chem.iastate.edu/GAMESS/download/GAMESS-Windows-64-Bit-README-THEN-README-AGAIN.pdf

first install Intel-MPI, then GAMESS-US
https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library-download.html

also MacMolPlt
https://brettbode.github.io/wxmacmolplt/

running
-------
Launch the Windows Command Prompt

C:\Users\Public\gamess-64> get-version-names.bat
------                                  -------
Binary                                  Version
======                                  =======
gamess.2023.R1.intel.exe                2023.R1.intel

Running All Serial Test Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\Public\gamess-64>runall.bat 2023.R1.intel 1

C:\Users\Public\gamess-64>clean-runall-files.bat

Finish removing exam*log, scratch\exam*.*, and restart\exam*.* files

Press any key to continue . . .

Testing and Validating Using Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\Public\gamess-64>python tests\runtest.py --version=2023.R1.intel --folder=travis-ci

cd tests
python checkgms.py --verbose_validation

C:\Users\Public\gamess-64\tests>python checkgms.py
[Validation result                       ] [ 1 / 15] .\travis-ci/exam05.log                                       [Passed]
[Validation result                       ] [ 2 / 15] .\travis-ci/exam32.log                                       [Passed]
[Validation result                       ] [ 3 / 15] .\travis-ci/exam39.log                                       [Passed]
[Validation result                       ] [ 4 / 15] .\travis-ci/exam42.log                                       [Passed]
[Validation result                       ] [ 5 / 15] .\travis-ci/exam45.log                                       [Passed]
[Validation result                       ] [ 6 / 15] .\travis-ci/exam46.log                                       [Passed]
[Validation result                       ] [ 7 / 15] .\travis-ci/exam47.log                                       [Passed]
[Validation result                       ] [ 8 / 15] .\travis-ci\parallel/exam01.log                              [Passed]
[Validation result                       ] [ 9 / 15] .\travis-ci\parallel/exam02.log                              [Passed]
[Validation result                       ] [10 / 15] .\travis-ci\parallel/exam03.log                              [Passed]
[Validation result                       ] [11 / 15] .\travis-ci\parallel/exam04.log                              [Passed]


cd ..
clean-runall-files.bat


C:\Users\Public\gamess-64>python tests\runtest.py --version=2023.R1.intel --folder=travis-ci\parallel -n 2

C:\Users\Public\gamess-64\tests>python checkgms.py
... all Passed

