===================================
openmpi-5.0.9-intel2025 buildup
===================================

software in /lustre/projects/m/milias/work/software/openmpi/openmpi-5.0.9-intelv2025.3.1

sbatch hydra_slurm_openmpi_buildup.01


Test installation
-----------------

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/openmpi-5.0.9-intelv2025.3.1/openmpi-5.0.9/examples/.

error:
https://pm.jinr.ru/issues/10357

configure ...
 --with-pmix(=DIR)       Build pmix support. DIR can take one of three
                          values: "internal", "external", or a valid directory
                          name. "internal" forces Open MPI to use its internal
                          copy of pmix. "external" forces Open MPI to use an
                          external installation of pmix. Supplying a valid
                          directory name also forces Open MPI to use an
                          external installation of pmix, and adds DIR/include,
                          DIR/lib, and DIR/lib64 to the search path for
                          headers and libraries. Note that Open MPI no longer
                          supports --without-pmix. If no argument is
                          specified, Open MPI will search default locations
                          for pmix and fall back to an internal version if one
                          is not found.

