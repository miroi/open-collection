=============================
Fl@Se54 addsorbate on 2D slab
=============================

checking BAND xyz file
----------------------
~/work/software/dft-d4/dftd4/_build/app/dftd4 -v  FlSe54_2d.xyz  > FlSe54_2d.logfile

~/work/software/dft-d4/dftd4/_build/app/dftd4 -v  FlSe54_2d_lattmod.xyz   > FlSe54_2d_lattmod.logfile

diff  FlSe54_2d_lattmod.logfile  FlSe54_2d.logfile ... files are IDENTICAL !!!


disp.energies
~~~~~~~~~~~~~
~/work/software/dft-d4/dftd4/_build/app/dftd4 -v  FlSe54_2d_lattmod.xyz  -f PBE0  
Dispersion energy:      -3.6863152983787E-01 Eh

~/work/software/dft-d4/dftd4/_build/app/dftd4 -v  FlSe54_2d.xyz  -f PBE0
Dispersion energy:      -3.6863152983787E-01 Eh


