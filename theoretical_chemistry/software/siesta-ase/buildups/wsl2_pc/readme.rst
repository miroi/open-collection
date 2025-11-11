==============
SIESTA buildup
==============

download
---------
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.wget https://gitlab.com/siesta-project/siesta/-/releases/5.4.1/downloads/siesta-5.4.1.tar.gz
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.tar xvzf siesta-5.4.1.tar.gz

installation
-------------
https://docs.siesta-project.org/projects/siesta/en/stable/installation/build-manually.html

milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.cmake -S. -B_build -DCMAKE_INSTALL_PREFIX=/home/milias/work/software/siesta/packaged  -DSIESTA_WITH_MPI=ON -DSIESTA_WITH_ELPA=ON



