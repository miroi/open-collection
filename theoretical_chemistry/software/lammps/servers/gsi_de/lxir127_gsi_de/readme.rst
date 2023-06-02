LAMMPS on lxir127.gsi.de
========================

https://docs.lammps.org/Build_cmake.html

milias@lxir127.gsi.de:/data.local1/milias/software/lammps/lammps-stable_23Jun2022/.mkdir build
milias@lxir127.gsi.de:/data.local1/milias/software/lammps/lammps-stable_23Jun2022/.cd build/
milias@lxir127.gsi.de:/data.local1/milias/software/lammps/lammps-stable_23Jun2022/build/.cmake ../cmake
-- The CXX compiler identification is GNU 8.3.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Git: /usr/bin/git (found version "2.20.1") 
-- Running check for auto-generated files from make-based build system
-- Found MPI_CXX: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so (found version "3.1") 
-- Found MPI: TRUE (found version "3.1")  
-- Looking for C++ include omp.h
-- Looking for C++ include omp.h - found
-- Found OpenMP_CXX: -fopenmp (found version "4.5") 
-- Found OpenMP: TRUE (found version "4.5")  
-- Found JPEG: /usr/lib/x86_64-linux-gnu/libjpeg.so (found version "62") 
-- Found PNG: /usr/lib/x86_64-linux-gnu/libpng.so (found version "1.6.36") 
-- Found ZLIB: /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-broadwell/gcc-8.3.0/zlib-1.2.11-pqdidq3pxucqbvyxnlf552vxypl6zxvs/lib/libz.so (found version "1.2.11") 
-- Found GZIP: /bin/gzip  
-- Found FFMPEG: /usr/bin/ffmpeg  
-- Looking for C++ include cmath
-- Looking for C++ include cmath - found
-- Generating style headers...
-- Generating package headers...
-- Generating lmpinstalledpkgs.h...
-- Could NOT find ClangFormat: Found unsuitable version "7.0.1", but required is at least "8.0" (found /usr/bin/clang-format)
-- The following tools and libraries have been found and configured:
 * Git
 * MPI
 * OpenMP
 * JPEG
 * PNG
 * ZLIB

-- <<< Build configuration >>>
   LAMMPS Version:   20220623
   Operating System: Linux Debian GNU/Linux 10
   Build type:       RelWithDebInfo
   Install path:     /u/milias/.local
   Generator:        Unix Makefiles using /usr/bin/make
-- Enabled packages: <None>
-- <<< Compilers and Flags: >>>
-- C++ Compiler:     /usr/bin/c++
      Type:          GNU
      Version:       8.3.0
      C++ Flags:     -O2 -g -DNDEBUG
      Defines:       LAMMPS_SMALLBIG;LAMMPS_MEMALIGN=64;LAMMPS_OMP_COMPAT=3;LAMMPS_JPEG;LAMMPS_PNG;LAMMPS_GZIP;LAMMPS_FFMPEG
-- <<< Linker flags: >>>
-- Executable name:  lmp
-- Static library flags:    
-- <<< MPI flags >>>
-- MPI_defines:      MPICH_SKIP_MPICXX;OMPI_SKIP_MPICXX;_MPICC_H
-- MPI includes:     /usr/lib/x86_64-linux-gnu/openmpi/include/openmpi;/usr/lib/x86_64-linux-gnu/openmpi/include
-- MPI libraries:    /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so;/usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so;
-- Configuring done
-- Generating done
-- Build files have been written to: /data.local1/milias/software/lammps/lammps-stable_23Jun2022/build
milias@lxir127.gsi.de:/data.local1/milias/software/lammps/lammps-stable_23Jun2022/build/.



milias@lxir127.gsi.de:/data.local1/milias/software/lammps/lammps-stable_23Jun2022/build/.ldd lmp 
        linux-vdso.so.1 (0x00007ffcf20b8000)
        libgomp.so.1 => /usr/lib/x86_64-linux-gnu/libgomp.so.1 (0x00007f86d8534000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f86d8513000)
        libmpi_cxx.so.40 => /usr/lib/x86_64-linux-gnu/libmpi_cxx.so.40 (0x00007f86d84f5000)
        libmpi.so.40 => /usr/lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f86d83ec000)
        libjpeg.so.62 => /usr/lib/x86_64-linux-gnu/libjpeg.so.62 (0x00007f86d8381000)
        libpng16.so.16 => /usr/lib/x86_64-linux-gnu/libpng16.so.16 (0x00007f86d8346000)
        libz.so.1 => /cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-broadwell/gcc-8.3.0/zlib-1.2.11-pqdidq3pxucqbvyxnlf552vxypl6zxvs/lib/libz.so.1 (0x00007f86d832d000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f86d8328000)
        libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f86d81a4000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f86d8021000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f86d8007000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f86d7e45000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f86d8a83000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f86d7e3b000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f86d7e36000)
        libhwloc.so.5 => /usr/lib/x86_64-linux-gnu/libhwloc.so.5 (0x00007f86d7df4000)
        libevent-2.1.so.6 => /usr/lib/x86_64-linux-gnu/libevent-2.1.so.6 (0x00007f86d7b9e000)
        libevent_pthreads-2.1.so.6 => /usr/lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.6 (0x00007f86d799b000)
        libopen-rte.so.40 => /usr/lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f86d78e1000)
        libopen-pal.so.40 => /usr/lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f86d7834000)
        libnuma.so.1 => /usr/lib/x86_64-linux-gnu/libnuma.so.1 (0x00007f86d7826000)
        libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007f86d781b000)
milias@lxir127.gsi.de:/data.local1/milias/software/lammps/lammps-stable_23Jun2022/build/.

