===========================
Intel compiler installation
===========================

download
~~~~~~~~
https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html?packages=oneapi-toolkit&oneapi-toolkit-os=linux&oneapi-lin=offline

install
~~~~~~~
#milias@hydra.jinr.ru:~/work/software/intel_compilers/.sh ./intel-oneapi-base-toolkit-2025.0.0.885_offline.sh  -a --silent --cli --eula accept

milias@hydra.jinr.ru:~/work/software/intel_compilers/.sh ./intel-oneapi-base-toolkit-2025.0.0.885_offline.sh  -a  --cli --eula accept
Extract intel-oneapi-base-toolkit-2025.0.0.885_offline to /lustre/home/user/m/milias/work/software/intel_compilers/intel-oneapi-base-toolkit-2025.0.0.885_offline...
[################################################################################################################################]
Extract intel-oneapi-base-toolkit-2025.0.0.885_offline completed!
Checking system requirements...
Done.
Wait while the installer is preparing...
.
.
.

 Installation in Progress | Intel® oneAPI Base Toolkit
--------------------------------------------------------------------------------
  Checking integrity pkgconfig_post_remove.sh
  ###########################################################--------------  81%

  Installing 9 of 46: Intel® DPC++ Co     bili    ool
  ################---------------------------------------------------------  23%

.
.

final checks
~~~~~~~~~~~~~
milias@hydra.jinr.ru:~/intel/oneapi/.source setvars.sh

milias@hydra.jinr.ru:~/intel/oneapi/.emkl
Intel MKL library ? MKLROOT=/lustre/home/user/m/milias/intel/oneapi/mkl/2025.0

milias@hydra.jinr.ru:~/.mpiicc -V
/lustre/home/user/m/milias/intel/oneapi/mpi/2021.14/bin/mpiicx: line 552: icc: command not found
milias@hydra.jinr.ru:~/.mpiifort -V
/lustre/home/user/m/milias/intel/oneapi/mpi/2021.14/bin/mpiifx: line 715: ifort: command not found





