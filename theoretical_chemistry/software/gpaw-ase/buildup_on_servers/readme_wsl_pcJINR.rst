GPAW
====

conda install --channel conda-forge gpaw
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/milias/miniconda3

  added / updated specs:
    - gpaw


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    elpa-2021.11.002           |mpi_openmpi_ha0c50f8_1         3.4 MB  conda-forge
    fftw-3.3.10                |mpi_openmpi_h4a81ba8_9         2.0 MB  conda-forge
    gpaw-24.6.0                |py312_mpi_openmpi_omp_0         4.4 MB  conda-forge
    gpaw-data-0.9.20000        |       hd8ed1ab_2        50.3 MB  conda-forge
    libblas-3.9.0              |1_h86c2bf4_netlib         199 KB  conda-forge
    liblapack-3.9.0            |6_ha36c22a_netlib         2.6 MB  conda-forge
    libstdcxx-ng-14.1.0        |       h4852527_1          51 KB  conda-forge
    libvdwxc-0.4.0             |mpi_openmpi_he05bc30_1         2.3 MB  conda-forge
    libxc-6.2.2                |   cpu_h5ef0af7_6          77 KB  conda-forge
    libxc-c-6.2.2              |   cpu_h20a523f_6        54.5 MB  conda-forge
    mpi-1.0                    |          openmpi           4 KB  conda-forge
    openmpi-4.1.6              |     hc5af2df_101         3.9 MB  conda-forge
    pyyaml-6.0.2               |  py312h66e93f0_1         202 KB  conda-forge
    scalapack-2.2.0            |       h67de57e_1         2.2 MB  conda-forge
    yaml-0.2.5                 |       h7f98852_2          87 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       126.2 MB

The following NEW packages will be INSTALLED:

  elpa               conda-forge/linux-64::elpa-2021.11.002-mpi_openmpi_ha0c50f8_1
  fftw               conda-forge/linux-64::fftw-3.3.10-mpi_openmpi_h4a81ba8_9
  gpaw               conda-forge/linux-64::gpaw-24.6.0-py312_mpi_openmpi_omp_0
  gpaw-data          conda-forge/noarch::gpaw-data-0.9.20000-hd8ed1ab_2
  libblas            conda-forge/linux-64::libblas-3.9.0-1_h86c2bf4_netlib
  liblapack          conda-forge/linux-64::liblapack-3.9.0-6_ha36c22a_netlib
  libvdwxc           conda-forge/linux-64::libvdwxc-0.4.0-mpi_openmpi_he05bc30_1
  libxc              conda-forge/linux-64::libxc-6.2.2-cpu_h5ef0af7_6
  libxc-c            conda-forge/linux-64::libxc-c-6.2.2-cpu_h20a523f_6
  mpi                conda-forge/linux-64::mpi-1.0-openmpi
  openmpi            conda-forge/linux-64::openmpi-4.1.6-hc5af2df_101
  pyyaml             conda-forge/linux-64::pyyaml-6.0.2-py312h66e93f0_1
  scalapack          conda-forge/linux-64::scalapack-2.2.0-h67de57e_1
  yaml               conda-forge/linux-64::yaml-0.2.5-h7f98852_2

The following packages will be UPDATED:

  libstdcxx-ng       pkgs/main::libstdcxx-ng-11.2.0-h12345~ --> conda-forge::libstdcxx-ng-14.1.0-h4852527_1


Proceed ([y]/n)?


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: \
For Linux 64, Open MPI is built with CUDA awareness but this support is disabled by default.
To enable it, please set the environment variable OMPI_MCA_opal_cuda_support=true before
launching your MPI processes. Equivalently, you can set the MCA parameter in the command line:
mpiexec --mca opal_cuda_support 1 ...

In addition, the UCX support is also built but disabled by default.
To enable it, first install UCX (conda install -c conda-forge ucx). Then, set the environment
variables OMPI_MCA_pml="ucx" OMPI_MCA_osc="ucx" before launching your MPI processes.
Equivalently, you can set the MCA parameters in the command line:
mpiexec --mca pml ucx --mca osc ucx ...
Note that you might also need to set UCX_MEMTYPE_CACHE=n for CUDA awareness via UCX.
Please consult UCX's documentation for detail.


done
