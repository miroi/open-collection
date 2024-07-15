LibXC libraty
=============


https://zoomadmin.com/HowToInstall/UbuntuPackage/libxc-dev

sudo apt-get install -y libxc-dev


dpkg -S libxc-dev
libxc-dev: /usr/share/doc/libxc-dev
libxc-dev: /usr/share/doc/libxc-dev/copyright
libxc-dev: /usr/share/doc/libxc-dev/changelog.Debian.gz


xc-info -h
libxc version 5.1.7
S. Lehtola, C. Steigemann, M. J. Oliveira, and M. A. Marques, SoftwareX 7, 1 (2018)
doi: 10.1016/j.softx.2017.11.002

Functional '-h' not found.


milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/libxc/wsl_win11_Victus/.gfortran -o libxctest  libxctest.F90 -I/usr/include/  -lxc -lxcf03 -lxcf90

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/libxc/wsl_win11_Victus/.libxctest
Libxc version: 5.1.7
0.100000 -0.342809
0.200000 -0.431912
0.300000 -0.494416
0.400000 -0.544175
0.500000 -0.586194

