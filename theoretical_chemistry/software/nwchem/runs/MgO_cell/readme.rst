==============
NWChem for MgO
==============

https://github.com/nwchemgit/nwchem/blob/master/examples/pspw/MgO%2BCu/pspw_MgO.nw

ubuntu-kch (fpv.UMB.sk)
~~~~~~~~~~~~~~~~~~~~~~~
/usr/bin/mpirun -np 2 nwchem pspw_MgO.nw > pspw_MgO.out-ubuntu-kch

lxir127 (GSI.de)
~~~~~~~~~~~~~~~~
/usr/bin/mpirun -np 2 nwchem pspw_MgO.nw > pspw_MgO.out-lxir127

mpirun -np 2 /data.local1/milias/software/nwchem/nwchem_master/bin/LINUX64/nwchem pspw_MgO.nw > pspw_MgO.out-lxir127-nwmaster

