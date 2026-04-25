=====================
Simple ASE-DIRAC test
=====================

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/wsl2/wsl_notebook/dirac_ase/simple_test/.which pam
/home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/pam

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/wsl2/wsl_notebook/dirac_ase/simple_test/.which mpiifx
/opt/intel/oneapi/2025.3/bin/mpiifx
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/wsl2/wsl_notebook/dirac_ase/simple_test/.which mpirun
/opt/intel/oneapi/2025.3/bin/mpirun

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/wsl2/wsl_notebook/dirac_ase/simple_test/.echo $DIRAC_MPI_COMMAND
mpiexec -np 2

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/wsl2/wsl_notebook/dirac_ase/simple_test/.ldd /home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/dirac.x   .. CHECKED

run
---
(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/wsl2/wsl_notebook/dirac_ase/simple_test/.python mp2_water.py  > mp2_water.py_logfile





