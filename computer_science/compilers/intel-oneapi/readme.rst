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

