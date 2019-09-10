Singularity at ADF2 UMB server
==============================

singularity version 3.2.1-1.1.el7

https://sylabs.io/guides/3.2/user-guide/
https://sylabs.io/guides/3.2/user-guide/quick_start.html

singularity --debug run library://sylabsed/examples/lolcow

singularity run --containall library://sylabsed/examples/lolcow

Download pre-built images
-------------------------

singularity search alp

singularity pull library://sylabsed/linux/alpine # This image is not signed, and thus its contents cannot be verified.

singularity pull docker://godlovedc/lolcow  # Build complete: lolcow_latest.sif

Download and build images
-------------------------
singularity build lolcow.sif docker://godlovedc/lolcow # Build complete: lolcow.sif
singularity build ubuntu.sif library://ubuntu  # Build complete: ubuntu.sif

Shell
-----
singularity shell lolcow_latest.sif

Executing commands
------------------
singularity exec lolcow_latest.sif cowsay moo

singularity exec library://sylabsed/examples/lolcow cowsay "Fresh from the library...! "


Running a container
-------------------
singularity run lolcow_latest.sif  # local run
singularity run library://sylabsed/examples/lolcow # distant run

Build images
------------
# ... This command creates a directory called ubuntu/ with an entire Ubuntu Operating System and some Singularity metadata in your current working directory

 sudo singularity build --sandbox ubuntu/ library://ubuntu # Build complete: ubuntu/

 sudo singularity exec --writable ubuntu touch /foo
 singularity exec ubuntu/ ls /foo


Converting image
----------------

sudo singularity build new-sif ubuntu

Singularity Definition Files
----------------------------

lolcow.def ... definition file

sudo singularity build lolcow.sif lolcow.def  # Build complete: lolcow.sif

To test:
singularity exec lolcow.sif cowsay

===============================================
https://github.com/bdusell/singularity-tutorial
===============================================

Defining an Image
-----------------
see definition file description, https://sylabs.io/guides/3.2/user-guide/definition_files.html

create definition file "ubuntu18_04.def"

sudo singularity build version-1.sif ubuntu18_04.def









