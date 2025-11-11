==============
SIESTA buildup
==============

download
---------
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.wget https://gitlab.com/siesta-project/siesta/-/releases/5.4.1/downloads/siesta-5.4.1.tar.gz
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.tar xvzf siesta-5.4.1.tar.gz

flook
~~~~~~
wget https://github.com/ElectronicStructureLibrary/flook/archive/refs/tags/v0.8.4.tar.gz
/siesta-5.4.1/External/flook_package/flook-0.8.4

sudo apt-get install libreadline-deva
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook-0.8.4/.make
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook-0.8.4/.quick_test.sh  > quick_test.logfile

elpa
~~~~
sudo apt install libelpa-dev

installation
-------------
https://docs.siesta-project.org/projects/siesta/en/stable/installation/build-manually.html

milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.cmake -S. -B_build -DCMAKE_INSTALL_PREFIX=/home/milias/work/software/siesta/packaged  -DSIESTA_WITH_MPI=ON -DSIESTA_WITH_ELPA=ON  -DSCALAPACK_LIBRARY="/usr/lib/x86_64-linux-gnu/libmkl_scalapack_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_blacs_openmpi_lp64.so" -DFLOOK_ROOT=/home/milias/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook-0.8.4 


