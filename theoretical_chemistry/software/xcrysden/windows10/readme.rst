================================
XCrysDen on Windows10 under WSL
================================

milias@Miro:~/snap$ wget http://www.xcrysden.org/download/xcrysden-1.6.2-linux_x86_64-shared.tar.gz

milias@Miro:~/snap$ tar xvzf xcrysden-1.6.2-linux_x86_64-shared.tar.gz

milias@Miro:~/snap/xcrysden-1.6.2-bin-shared$ sudo apt-cache search fftw3

milias@Miro:~/snap/xcrysden-1.6.2-bin-shared$ sudo apt-get install libfftw3-bin

Missing:
/home/milias/snap/xcrysden-1.6.2-bin-shared/bin/xcrys: error while loading shared libraries: libtk8.6.so: cannot open shared object file: No such file or directory

milias@Miro:~/snap/xcrysden-1.6.2-bin-shared$ sudo apt-cache search libtk8
libtk8.6 - Tk toolkit for Tcl and X11 v8.6 - run-time files

milias@Miro:~/snap/xcrysden-1.6.2-bin-shared$ sudo apt-get install libtk8.6

/home/milias/snap/xcrysden-1.6.2-bin-shared/bin/xcrys: error while loading shared libraries: libTogl.so.2: cannot open shared object file: No such file or directory

milias@Miro:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy

