Avogadro2 buildup under WSL
===========================

https://github.com/OpenChemistry/avogadroapp


cloning
-------
see https://two.avogadro.cc/develop/build

miroi@MIRO:~/work/software/avogadro2/cloned/openchemistry/.git submodule update --init --recursive

git submodule update --remote

Submodule 'avogadro-i18n' (https://github.com/OpenChemistry/avogadro-i18n.git) registered for path 'avogadro-i18n'
Submodule 'avogadroapp' (https://github.com/OpenChemistry/avogadroapp.git) registered for path 'avogadroapp'
Submodule 'avogadrodata' (https://github.com/OpenChemistry/avogadrodata.git) registered for path 'avogadrodata'
Submodule 'avogadrogenerators' (https://github.com/openchemistry/avogenerators.git) registered for path 'avogadrogenerators'
Submodule 'avogadrolibs' (https://github.com/OpenChemistry/avogadrolibs.git) registered for path 'avogadrolibs'
Submodule 'crystals' (https://github.com/OpenChemistry/crystals.git) registered for path 'crystals'
Submodule 'fragments' (https://github.com/OpenChemistry/fragments.git) registered for path 'fragments'
Submodule 'jupyter-examples' (https://github.com/OpenChemistry/jupyter-examples.git) registered for path 'jupyter-examples'
Submodule 'molecules' (https://github.com/OpenChemistry/molecules.git) registered for path 'molecules'
Submodule 'molequeue' (https://github.com/OpenChemistry/molequeue.git) registered for path 'molequeue'
Submodule 'thirdparty/VTK' (https://github.com/Kitware/VTK.git) registered for path 'thirdparty/VTK'
Submodule 'thirdparty/pybind11' (https://github.com/pybind/pybind11.git) registered for path 'thirdparty/pybind11'
Submodule 'thirdparty/qttesting' (https://github.com/Kitware/qttesting.git) registered for path 'thirdparty/qttesting'
Submodule 'thirdparty/yaehmop' (https://github.com/greglandrum/yaehmop) registered for path 'thirdparty/yaehmop'
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/avogadro-i18n'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/avogadrodata'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/avogadrogenerators'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/crystals'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/fragments'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/jupyter-examples'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/molecules'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/molequeue'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/thirdparty/VTK'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/thirdparty/pybind11'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/thirdparty/qttesting'...
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/thirdparty/yaehmop'...
Submodule path 'avogadro-i18n': checked out '07bee855ee8f34b64caf804e69cc4c0b34112ca3'
Submodule path 'avogadroapp': checked out '2addc17d59a9e1cc990c60d2714aaa8b9df6709d'
Submodule path 'avogadrodata': checked out 'fad6c548e9a21b7ccefe8fe65c91f65c72ef8e44'
Submodule path 'avogadrogenerators': checked out 'f4e3bd7f63664a6844e732e89598bfed48b2c47e'
Submodule path 'avogadrolibs': checked out '7c04f6412472269594d2b1378bec5c56932c6345'
Submodule path 'crystals': checked out '28404bd4cceae4c7a688f78b50a59ea819186ccd'
Submodule path 'fragments': checked out 'c4943b58a488061615e3daf1f183acb01591e890'
Submodule path 'jupyter-examples': checked out '735b08309119759ffac6527dbb5b2d2a09944765'
Submodule path 'molecules': checked out '8a37883ef47375247be5bbb41b538c85e131bc12'
Submodule path 'molequeue': checked out 'b92da87f2818e045adc2497ab16ea49d06863473'
Submodule path 'thirdparty/VTK': checked out '4f02ae83179c6a1542ac3c335c73dea976578c63'
Submodule 'VTK-m' (https://gitlab.kitware.com/vtk/vtk-m.git) registered for path 'thirdparty/VTK/ThirdParty/vtkm/vtkvtkm/vtk-m'
Cloning into '/home/miroi/work/software/avogadro2/cloned/openchemistry/thirdparty/VTK/ThirdParty/vtkm/vtkvtkm/vtk-m'...
Submodule path 'thirdparty/VTK/ThirdParty/vtkm/vtkvtkm/vtk-m': checked out 'cfd6d3fbe534343d217c2dce47a46763692db0ec'
Submodule path 'thirdparty/pybind11': checked out '15d9dae14b148509f3e1e7a42d5b1260fffff3ad'
Submodule path 'thirdparty/qttesting': checked out '39eb6be1af55a8b7d35914f58f239958b13c3913'
Submodule path 'thirdparty/yaehmop': checked out '719975c2b13a2c0e57cf21ab1367e48990cb5d82'
miroi@MIRO:~/work/software/avogadro2/cloned/openchemistry/.

CMake build
-----------
https://two.avogadro.cc/develop/build#configuring-cmake

sudo apt install -y qtcreator qtbase5-dev qt5-qmake cmake (https://askubuntu.com/questions/1404263/how-do-you-install-qt-on-ubuntu22-04)
sudo apt install python3-mmtf libmmtf-java
sudo apt-get install build-essential
sudo apt-get install libopengl-dev freeglut3-dev
sudo apt-get install libeigen3-dev
sudo apt-get install libboost-dev
sudo apt install  libboost1.74-all-dev
sudo apt install  libarchive-dev libarchive-any-perl libarchive-tools
sudo apt install libacl1 python3-pylibacl liblinux-acl-perl

cmake update
~~~~~~~~~~~~
needs cmake 3.24 ! apply https://apt.kitware.com/


miroi@MIRO:~/work/software/avogadro2/cloned/.cmake -DQT_VERSION=5 -DBUILD_MOLEQUEUE=OFF -S ./openchemistry -B ./build
-- The CXX compiler identification is GNU 13.3.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to 'Debug' as none was specified.
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.3")
-- Found LibXml2: /usr/lib/x86_64-linux-gnu/libxml2.so (found version "2.9.14")
-- Configuring done (3.4s)
-- Generating done (0.0s)
-- Build files have been written to: /home/miroi/work/software/avogadro2/cloned/build


miroi@MIRO:~/work/software/avogadro2/cloned/build/.make -j4 all
.
.
.
see  https://discuss.avogadro.cc/t/cmake-buildup-of-fresh-repos-failes-on-wsl-ubuntu-24-04-2/7049


