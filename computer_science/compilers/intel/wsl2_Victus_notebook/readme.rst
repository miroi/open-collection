==================================
Get the Intel® oneAPI Base Toolkit
==================================

in Russia - switch on VPN

https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html

following

https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html?packages=oneapi-toolkit&oneapi-toolkit-os=linux&oneapi-lin=offline


downloading Intel® oneAPI Base Toolkit - Linux, offline installer  

downloading offline installer, file intel-oneapi-base-toolkit-2025.3.1.36_offline.sh

miroi@MIRO:~/work/software/intel/.mv /mnt/c/Users/miroi/Downloads/intel-oneapi-base-toolkit-2025.3.1.36_offline.sh  .

sudo apt-get install xdg-utils

miroi@MIRO:~/work/software/intel/.sudo sh ./intel-oneapi-base-toolkit-2025.3.1.36_offline.sh

installation GUI... no Eclipse 

Extract intel-oneapi-base-toolkit-2025.3.1.36_offline to /home/miroi/work/software/intel/intel-oneapi-base-toolkit-2025.3.1.36_offline...
[#####################################################################################################################]
Extract intel-oneapi-base-toolkit-2025.3.1.36_offline completed!
The installer is running in graphical user interface (GUI) mode. If you expected to run the installer in command line interface (CLI) or silent mode, relaunch it with the appropriate parameters: --cli or --silent.
Remove extracted files: /home/miroi/work/software/intel/intel-oneapi-base-toolkit-2025.3.1.36_offline...

miroi@MIRO:~/work/software/intel/.ls /opt/intel/
oneapi/  packagemanager/
miroi@MIRO:~/work/software/intel/.ls /opt/intel/oneapi/
2025.3/   compiler/       dnnl/       ipp/        mkl/                   setvars.sh   umf/
advisor/  dal/            dpcpp-ct/   ippcp/      modulefiles-setup.sh*  support.txt  vtune/
ccl/      debugger/       dpl/        licensing/  mpi/                   tbb/
common/   dev-utilities/  installer/  logs/       oneapi-base-toolkit/   tcm/

sudo apt -y install cmake pkg-config build-essential

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/.which cmake pkg-config make gcc g++
/usr/bin/cmake
/usr/bin/pkg-config
/usr/bin/make
/usr/bin/gcc
/usr/bin/g++

envirovariables
~~~~~~~~~~~~~~~

miroi@MIRO:~/work/software/intel/.source /opt/intel/oneapi/2025.3/oneapi-vars.sh

:: initializing oneAPI environment ...
   -bash: BASH_VERSION = 5.2.21(1)-release
   args: Using "$@" for oneapi-vars.sh arguments: autologout=no
:: advisor -- processing etc/advisor/vars.sh
:: ccl -- processing etc/ccl/vars.sh
:: compiler -- processing etc/compiler/vars.sh
:: dal -- processing etc/dal/vars.sh
:: debugger -- processing etc/debugger/vars.sh
:: dnnl -- processing etc/dnnl/vars.sh
:: dpct -- processing etc/dpct/vars.sh
:: dpl -- processing etc/dpl/vars.sh
:: ipp -- processing etc/ipp/vars.sh
:: ippcp -- processing etc/ippcp/vars.sh
:: mkl -- processing etc/mkl/vars.sh
:: mpi -- processing etc/mpi/vars.sh
:: tbb -- processing etc/tbb/vars.sh
:: vtune -- processing etc/vtune/vars.sh
:: oneAPI environment initialized ::

miroi@MIRO:~/work/software/intel/.emkl
Intel MKL library ? MKLROOT=/opt/intel/oneapi/2025.3
miroi@MIRO:~/work/software/intel/.ls /opt/intel/oneapi/2025.3/lib/


ls /opt/intel/oneapi/2025.3/bin/ ... needs ifx !!!

Get Intel® Fortran Compiler
---------------------------

https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler-download.html?operatingsystem=linux&distribution-linux=offline


Linux, offline installer

miroi@MIRO:~/work/software/intel/.mv /mnt/c/Users/miroi/Downloads/intel-fortran-compiler-2025.3.2.25_offline.sh  .

miroi@MIRO:~/work/software/intel/.sudo sh intel-fortran-compiler-2025.3.2.25_offline.sh
Extract intel-fortran-compiler-2025.3.2.25_offline to /home/miroi/work/software/intel/intel-fortran-compiler-2025.3.2.25_offline...
[#####################################################################################################################]
Extract intel-fortran-compiler-2025.3.2.25_offline completed!
The installer is running in graphical user interface (GUI) mode. If you expected to run the installer in command line interface (CLI) or silent mode, relaunch it with the appropriate parameters: --cli or --silent.
Remove extracted files: /home/miroi/work/software/intel/intel-fortran-compiler-2025.3.2.25_offline...

source  /opt/intel/oneapi/2025.3/oneapi-vars.sh  ... :: WARNING: oneapi-vars.sh has already been run. Skipping re-execution.

miroi@MIRO:~/work/software/intel/.which icx
/opt/intel/oneapi/2025.3/bin/icx
miroi@MIRO:~/work/software/intel/.ifx --version
ifx (IFX) 2025.3.2 20260112
miroi@MIRO:~/work/software/intel/.icx --version
Intel(R) oneAPI DPC++/C++ Compiler 2025.3.2 (2025.3.2.20260112)

clean the space
---------------
miroi@MIRO:~/work/software/intel/.ls
intel-fortran-compiler-2025.3.2.25_offline.sh*  intel-oneapi-base-toolkit-2025.3.1.36_offline.sh*
miroi@MIRO:~/work/software/intel/.du -h -s .
3.3G    .



