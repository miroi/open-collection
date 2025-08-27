=======================
NWChem driven by Python
=======================

to fix:

mpirun -np 2 nwchem N2.dft_plots.nw



                               NWChem Python program
                               ---------------------

e = task_energy('dft')
if (ga_nodeid() == 0):
  print('DFT energy=',e)

 ------------------------------------------------------------------------
 python_input: indentation must be >= that of first line                   2
 ------------------------------------------------------------------------
 ------------------------------------------------------------------------
  current input line :
    22: python
 ------------------------------------------------------------------------
 ------------------------------------------------------------------------
 There is an error in the input file

