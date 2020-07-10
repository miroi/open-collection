abinit testing
==============


www.abinit.org

http://packages.ubuntu.com/trusty/amd64/abinit/filelist

test from abinbit suite;

tbase1_x.files contains file names , the first is the input

abinit < tbase1_x.files 

lxir127
~~~~~~~
/data.local1/milias/software/abinit/abinit-8.10.3/bin/abinit < tbase1_x.files > output

mpirun -np 4 /data.local1/milias/software/abinit/abinit-8.10.3/bin/abinit < tbase1_x.files > output



