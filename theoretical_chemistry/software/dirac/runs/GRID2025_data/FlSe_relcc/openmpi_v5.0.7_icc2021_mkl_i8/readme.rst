FlSe with DIRAC RelCC
=====================

https://manpages.debian.org/unstable/openmpi-bin/mpirun.openmpi.1.en.html

--------------------------------------------------------------------------
A request was made to bind that would require binding
processes to more cpus than are available in your allocation:

   Application:     /lustre/home/user/m/milias/DIRAC_scratch_directory/milias/DIRAC_x2c-ach0.scf_relcc_m3.20-vir50.00_FlSe.dyall_acv3z_lsym_59814/dirac.x
   #processes:      6
   Mapping policy:  BYCORE
   Binding policy:  CORE

You can override this protection by adding the "overload-allowed"
option to your binding directive.
--------------------------------------------------------------------------

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/dirac/runs/GRID2025_data/FlSe_relcc/openmpi_v5.0.7_icc2021_mkl_i8/.ls -lt
total 57
-rw-r--r--. 1 milias hybrilit  642 Jul  3 09:37 readme.rst
-rwxr--r--. 1 milias hybrilit 4961 Jul  3 09:36 hydra_slurm_dirac.01*
lrwxrwxrwx. 1 milias hybrilit   56 Jul  3 08:20 x2c-ach0.scf_relcc_m3.20-vir50.00.inp -> ../intelmpi_mkl_i8/x2c-ach0.scf_relcc_m3.20-vir50.00.inp
lrwxrwxrwx. 1 milias hybrilit   44 Jul  3 08:19 FlSe.dyall_acv3z_lsym.mol -> ../intelmpi_mkl_i8/FlSe.dyall_acv3z_lsym.mol
lrwxrwxrwx. 1 milias hybrilit   49 Jul  3 08:19 DFPCMO.FlSe.acv3z_x2c_scf_lsym -> ../intelmpi_mkl_i8/DFPCMO.FlSe.acv3z_x2c_scf_lsym
