=====================
NWCHEM-master buildup
=====================

downloading
-----------

ga
~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/cloned/nwchem_master/src/tools/.get-tools-github
downloading ga-5.9.2.tar.gz from https://github.com/GlobalArrays/ga/releases/download/v5.9.2/ga-5.9.2.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 8343k  100 8343k    0     0  5999k      0  0:00:01  0:00:01 --:--:-- 5999k
ga-5.9.2.tar.gz file integrity OK
patched
configure present. no autogen.sh required

dftd3
~~~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/cloned/nwchem_master/src/nwpw/nwpwlib/nwpwxc/../build_dftd3a.sh
downloading dftd3.tgz
chchc curl -f -L https://www.chemie.uni-bonn.de/grimme/de/software/dft-d3//dftd3.tgz -o dftd3.tgz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  542k  100  542k    0     0   838k      0 --:--:-- --:--:-- --:--:--  837k
patching file nwpwxc_vdw3a.F

elpa
~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/nwchem/cloned/nwchem_master/src/libext/elpa/../build_elpa.sh
mpif90 is /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/bin/mpif90
using existing elpa-2025.01.002.tar.gz

...
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443...




configure & compile
~~~~~~~~~~~~~~~~~~~
sbatch hydra_slurm_compile_nwchem.01


/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/config-3.10-x86_64-linux-gnu/libpython3.10.a(posixmod
ule.o): In function `os_openpty_impl':
/root/zuev/Python-3.10.13/./Modules/posixmodule.c:7259: undefined reference to `openpty'
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/Python/v3.10.13/lib/python3.10/config-3.10-x86_64-linux-gnu/libpython3.10.a(posixmodule.o): In function `os_forkpty_impl':
/root/zuev/Python-3.10.13/./Modules/posixmodule.c:7360: undefined reference to `forkpty'
make: *** [link] Error 1

try -lutil
