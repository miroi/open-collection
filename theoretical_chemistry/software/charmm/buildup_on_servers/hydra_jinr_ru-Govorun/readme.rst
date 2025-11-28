======
CHARMM
======

latest version
--------------
https://academiccharmm.org/documentation

Available Versions
c50b1

download and unpack
-------------------
http://brooks.chem.lsa.umich.edu/register/download_charmm.php

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/charmm/.tar xvzf c50b1.tar.gz

installation
------------
https://academiccharmm.org/documentation/installation

module add  openmpi/v5.0.7_gcc1230
module add Python/v3.10.13
module add CMake/v3.29.2
module add  LAPACK/v3.12.0_gcc1230
module add fftw/v3.3.10_gcc1120 # may need proper verson

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/charmm/c50b1/charmm_c50b1/../configure --prefix=/zfs/scratch/HybriLITWorkshop2025/milias/software/charmm/c50b1/openmpi_build

batch job
~~~~~~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/projects/open-collection/theoretical_chemistry/software/charmm/buildup_on_servers/hydra_jinr_ru-Govorun/.sbatch hydra_slurm_charmm.01





