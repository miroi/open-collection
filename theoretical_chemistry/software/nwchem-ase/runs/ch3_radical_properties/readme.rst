==========================
CH3(.) radical with NWChem
==========================

https://nwchemgit.github.io/EPR-pNMR.html


running interactively
~~~~~~~~~~~~~~~~~~~~~
mpirun -np 6 nwchem ch3_zora_b3lyp_prop.nw


or via script with command line:

wsl_bash_run.01

wsl_bash_run.01  4

wsl_bash_run.01  6

perfomance on 12th Gen Intel(R) Core(TM) i5-12450H
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nthr    Wall
2        9.9s
4        6.8s
6        6.6s


larger basis set

       

