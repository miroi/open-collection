======================
LibXC module on Devana
======================

see

https://www.tddft.org/programs/libxc/manual/libxc-5.1.x/

module load libxc/5.2.3-intel-compilers-2022.1.0

module whatis libxc/5.2.3-intel-compilers-2022.1.0

module spider libxc/5.2.3-intel-compilers-2022.1.0


Libxc lib path:
$LD_LIBRARY_PATH: /storage-apps/easybuild/software/libxc/5.2.3-intel-compilers-2022.1.0/lib

$PATH: /storage-apps/easybuild/software/libxc/5.2.3-intel-compilers-2022.1.0/bin

xc-info


Compiling demo program
~~~~~~~~~~~~~~~~~~~~~~

https://www.tddft.org/programs/libxc/manual/libxc-5.1.x/

milias@login02.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/libxc/devana_nscc_sk/.ifort libxctest.F90  -I/strage-apps/easybuild/software/libxc/5.2.3-intel-compilers-2022.1.0/include -L/storage-apps/easybuild/software/libxc/5.2.3-intel-compilers-202.1.0/lib  -lxc -lxcf03 -lxcf90

or better

milias@login02.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/libxc/devana_nscc_sk/.ifort -o libxctest  libxctest.F90  -lxc lxcf03 -lxcf90


milias@login02.devana.local:~/work/projects/open-collection/theoretical_chemistry/software/libxc/devana_nscc_sk/.libxctest
Libxc version: 5.2.3
0.100000 -0.342809
0.200000 -0.431912
0.300000 -0.494416
0.400000 -0.544175
0.500000 -0.586194



