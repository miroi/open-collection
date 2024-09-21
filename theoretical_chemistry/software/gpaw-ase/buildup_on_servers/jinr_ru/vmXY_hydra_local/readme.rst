gpaw-ase
========

milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/buildup_on_servers/jinr_ru/vmXY_hydra_local/.pip3 install gpaw
Defaulting to user installation because normal site-packages is not writeable
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
WARNING: Ignoring invalid distribution -ip (/lustre/home/user/m/milias/.local/lib/python3.10/site-packages)
Collecting gpaw
  Downloading gpaw-24.6.0.tar.gz (2.0 MB)
.
.
.
      mpicc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNPY_NO_DEPRECATED_API=7 -DGPAW_NO_UNDERSCORE_CBLACS -DGPAW_NO_UNDERSCORE_CSCALAPACK -DGPAW_MPI_INPLACE -DPARALLEL -UNDEBUG -I/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/include/python3.10 -I/tmp/pip-build-env-n11vgh_c/normal/lib/python3.10/site-packages/numpy/core/include -c c/_gpaw_so.c -o build/temp.linux-x86_64-cpython-310/c/_gpaw_so.o -Wall -Wno-unknown-pragmas -std=c99
      In file included from c/_gpaw_so.c:1:0:
      c/_gpaw.h:14:123: fatal error: xc.h: No such file or directory
       #include <xc.h> // If this file is not found, install libxc https://wiki.fysik.dtu.dk/gpaw/install.html#libxc-installation
                                                                                                                                 ^
      compilation terminated.
      error: command '/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/openmpi/v1.8.8-1/bin/mpicc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for gpaw
Failed to build gpaw
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (gpaw)
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/gpaw-ase/buildup_on_servers/jinr_ru/vmXY_hydra_local/.

