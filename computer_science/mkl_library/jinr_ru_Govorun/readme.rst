==============================================
Get Intel® oneAPI Math Kernel Library (oneMKL) 
==============================================

https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-download.html?operatingsystem=linux&linux-install=offline


wget https://registrationcenter-download.intel.com/akdlm/IRC_NAS/17f37e16-768e-40d2-bcf8-c252dc6c5499/intel-onemkl-2026.1.0.237_offline.sh

sh ./intel-onemkl-2026.1.0.237_offline.sh

Change installation directory:

/lustre/projects/m/milias/intel_mkl/oneapi


After installation
------------------
milias@hydra.jinr.ru:/lustre/projects/m/milias/intel_mkl/oneapi/.. setvars.sh

:: initializing oneAPI environment ...
   -bash: BASH_VERSION = 5.1.8(1)-release
   args: Using "$@" for setvars.sh arguments: autologout=no
:: compiler -- latest
:: mkl -- latest
:: mpi -- latest
:: tbb -- latest
:: tcm -- latest
:: umf -- latest
:: oneAPI environment initialized ::

milias@hydra.jinr.ru:/lustre/projects/m/milias/intel_mkl/oneapi/.emkl
Intel MKL library ? MKLROOT=/lustre/projects/m/milias/intel_mkl/oneapi/mkl/2026.1
