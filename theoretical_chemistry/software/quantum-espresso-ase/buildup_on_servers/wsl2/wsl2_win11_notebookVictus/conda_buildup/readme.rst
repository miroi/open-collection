Quantum Espresso buildup with conda
===================================

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/buildup_on_servers/wsl2/wsl2_win11_notebookVictus/conda_buildup/.con
miniconda activated :conda 26.5.3
onda: command not found
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/buildup_on_servers/wsl2/wsl2_win11_notebookVictus/conda_buildup/.conda ac
tivate xtb_env
(xtb_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/buildup_on_servers/wsl2/wsl2_win11_notebookVictus/conda_buildup/.conda install -c conda-forge qe
.
.
The following NEW packages will be INSTALLED:

  c-ares             conda-forge/linux-64::c-ares-1.34.8-hb03c661_0
  elpa               conda-forge/linux-64::elpa-2025.06.001-mpi_openmpi_h335e491_1
  fftw               conda-forge/linux-64::fftw-3.3.11-nompi_h3b011a4_100
  hdf5               conda-forge/linux-64::hdf5-1.14.6-mpi_openmpi_h8367ee7_10
  keyutils           conda-forge/linux-64::keyutils-1.6.3-hb9d3cd8_0
  krb5               conda-forge/linux-64::krb5-1.22.2-hbde042b_1
  libaec             conda-forge/linux-64::libaec-1.1.5-h088129d_0
  libcap             conda-forge/linux-64::libcap-2.78-h084b8d7_1
  libcurl            conda-forge/linux-64::libcurl-8.21.0-heca4667_4
  libedit            conda-forge/linux-64::libedit-3.1.20250104-pl5321h7949ede_0
  libev              conda-forge/linux-64::libev-4.33-h280c20c_3
  libevent           conda-forge/linux-64::libevent-2.1.12-hf998b51_1
  libfabric          conda-forge/linux-64::libfabric-2.6.0-ha770c72_0
  libfabric1         conda-forge/linux-64::libfabric1-2.6.0-h6b3ec72_0
  libhwloc           conda-forge/linux-64::libhwloc-2.13.0-default_he001693_1000
  liblapacke         conda-forge/linux-64::liblapacke-3.11.0-9_h6ae95b6_openblas
  libnghttp2         conda-forge/linux-64::libnghttp2-1.68.1-h877daf1_0
  libnl              conda-forge/linux-64::libnl-3.11.0-hb9d3cd8_0
  libpmix            conda-forge/linux-64::libpmix-5.0.8-h31fc519_4
  libpsl             conda-forge/linux-64::libpsl-0.23.0-hf670292_0
  libssh2            conda-forge/linux-64::libssh2-1.11.1-hcf80075_0
  libsystemd0        conda-forge/linux-64::libsystemd0-261.1-h6f4a2f1_0
  libudev1           conda-forge/linux-64::libudev1-261.1-h6f4a2f1_0
  libxml2            conda-forge/linux-64::libxml2-2.15.3-h49c6c72_0
  libxml2-16         conda-forge/linux-64::libxml2-16-2.15.3-hca6bf5a_0
  mpi                conda-forge/noarch::mpi-1.0.1-openmpi
  openmpi            conda-forge/linux-64::openmpi-5.0.10-h67ed482_1
  qe                 conda-forge/linux-64::qe-7.5-h19104ac_2
  rdma-core          conda-forge/linux-64::rdma-core-63.0-h192683f_1
  scalapack          conda-forge/linux-64::scalapack-2.2.0-h606478a_6
  ucc                conda-forge/linux-64::ucc-1.8.0-hcedbda0_0
  ucx                conda-forge/linux-64::ucx-1.20.1-hbe80e26_0


Proceed ([y]/n)?


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: -
To enable CUDA support, UCX requires the CUDA Runtime library (libcudart).
The library can be installed with the appropriate command below:

* For CUDA 12, run:    conda install cuda-cudart cuda-version=12
* For CUDA 13, run:    conda install cuda-cudart cuda-version=13

If any of the packages you requested use CUDA then CUDA should already
have been installed for you.


|
To enable CUDA support, please follow UCX's instruction above.

To additionally enable NCCL support, run:    conda install nccl


-
On Linux, Open MPI is built with CUDA awareness but it is disabled by default.
To enable it, please set the environment variable
OMPI_MCA_opal_cuda_support=true
before launching your MPI processes.
Equivalently, you can set the MCA parameter in the command line:
mpiexec --mca opal_cuda_support 1 ...
Note that you might also need to set UCX_MEMTYPE_CACHE=n for CUDA awareness via
UCX. Please consult UCX documentation for further details.


done

(xtb_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/buildup_on_servers/wsl2/wsl2_win11_notebookVictus/conda_buildup/.which pw.x
/home/miroi/miniconda3/envs/xtb_env/bin/pw.x


