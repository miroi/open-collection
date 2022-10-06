Singularity at ADF2 UMB server
==============================

singularity version 3.2.1-1.1.el7

https://github.com/bdusell/singularity-tutorial

Defining an Image
-----------------
see definition file description, https://sylabs.io/guides/3.2/user-guide/definition_files.html

- create definition file "ubuntu_python.def"

- sudo singularity build version-1.sif ubuntu_python.def

version-1.sif is of 1.7GB !!!!

Running a Shell
---------------

singularity shell version-1.sif

Singularity version-1.sif:~/singularity-tutorial/examples/xor> python3 train_xor.py

Pull the Image
--------------

singularity pull version-1.sif library://brian/default/singularity-tutorial:version-1

