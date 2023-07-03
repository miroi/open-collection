ELPA Using OpenMP threading
===========================

https://gitlab.mpcdf.mpg.de/elpa/elpa/-/blob/master/documentation/USERS_GUIDE.md
https://gitlab.mpcdf.mpg.de/elpa/elpa/-/blob/master/documentation/USERS_GUIDE.md#iv-using-openmp-threading

IMPORTANT: In case of hybrid MPI and OpenMP builds it is mandatory that your MPI library supports the threading levels "MPI_THREAD_SERIALIZED" or "MPI_THREAD_MULTIPLE" (you can check this for example by building ELPA with MPI and OpenMP and run one of the test programs, they will warn you if this prerequiste is not met). If your MPI library does not provide these threading levels, then ELPA will internally (independent of what you set) use only one OpenMP thread and inform you at runtime with a warning. The number of threads used in a threaded implementation of your BLAS library are not affected by this, as long as these threads can be controlled with another method than specifying OMP_NUM_THREADS (for instance with Intel's MKL libray you can specify MKL_NUM_THREADS).

milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/theoretical_chemistry/software/wien2k/buildups_on_servers/gsi_de/lxir127_gsi_de/buildups/elpa_test/.wget https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/2023.05.001/elpa-2023.05.001.tar.gz
