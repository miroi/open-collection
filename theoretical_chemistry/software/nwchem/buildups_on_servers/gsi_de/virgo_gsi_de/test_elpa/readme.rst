Test ELPA spack module on Virgo
===============================

see 
https://groups.google.com/g/nwchem-forum/c/OhWndXRuG6E/m/VhsZeLy7AAAJ

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/projects/open-collection/theoretical_chemistry/software/nwchem/buildups_on_servers/gsi_de/virgo_gsi_de/test_elpa/.spack load elpa%gcc target=x86_64

check: ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/projects/open-collection/theoretical_chemistry/software/nwchem/buildups_on_servers/gsi_de/virgo_gsi_de/test_elpa/.export LD_LIBRARY_PATH=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

check: ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules

Compile 
~~~~~~~~

gfortran test_elpa.f90 -I /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -lelpa_openmp -lgfortran

get error:

 /usr/bin/ld: /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/libelpa_openmp.so: undefined reference to `_gfortran_os_error_at@GFORTRAN_10'
collect2: error: ld returned 1 exit status


related bug: https://access.redhat.com/solutions/6156392

