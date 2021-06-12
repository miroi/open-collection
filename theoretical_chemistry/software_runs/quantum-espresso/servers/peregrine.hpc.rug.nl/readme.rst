==========================
QE on peregrine.hpc.rug.nl
==========================


module load QuantumESPRESSO/6.5-foss-2019b

access to binaries in /software/software/QuantumESPRESSO/6.5-foss-2019b/bin/ , no PPs


Own installation
----------------

module purge
s

f113112@peregrine.hpc.rug.nl:~/work/qch/software/quantum_espresso/qe-6.7/.module list

Currently Loaded Modules:
  1) GCCcore/6.4.0                                        8) imkl/2018.1.163-iimpi-2018a    15) SQLite/3.21.0-GCCcore-6.4.0
  2) binutils/2.28-GCCcore-6.4.0                          9) intel/2018a                    16) GMP/6.1.2-GCCcore-6.4.0
  3) iccifort/2018.1.163-GCC-6.4.0-2.28                  10) bzip2/1.0.6-GCCcore-6.4.0      17) libffi/3.2.1-GCCcore-6.4.0
  4) icc/2018.1.163-GCC-6.4.0-2.28                       11) zlib/1.2.11-GCCcore-6.4.0      18) Python/3.6.4-intel-2018a
  5) ifort/2018.1.163-GCC-6.4.0-2.28                     12) ncurses/6.0-GCCcore-6.4.0      19) Boost/1.66.0-intel-2018a-Python-3.6.4
  6) impi/2018.1.163-iccifort-2018.1.163-GCC-6.4.0-2.28  13) libreadline/7.0-GCCcore-6.4.0
  7) iimpi/2018a                                         14) Tcl/8.6.8-GCCcore-6.4.0


f113112@peregrine.hpc.rug.nl:~/work/qch/software/quantum_espresso/qe-6.7/../configure 
f113112@peregrine.hpc.rug.nl:~/work/qch/software/quantum_espresso/qe-6.7/.make -j12 all

f113112@peregrine.hpc.rug.nl:~/work/qch/software/quantum_espresso/qe-6.7/bin/.ldd pw.x
        linux-vdso.so.1 =>  (0x00007ffd3e577000)
        libmkl_intel_lp64.so => /software/software/imkl/2018.1.163-iimpi-2018a/mkl/lib/intel64/libmkl_intel_lp64.so (0x00007fd64f6c5000)
        libmkl_sequential.so => /software/software/imkl/2018.1.163-iimpi-2018a/mkl/lib/intel64/libmkl_sequential.so (0x00007fd64e3b7000)
        libmkl_core.so => /software/software/imkl/2018.1.163-iimpi-2018a/mkl/lib/intel64/libmkl_core.so (0x00007fd64c224000)
        libmpifort.so.12 => /software/software/impi/2018.1.163-iccifort-2018.1.163-GCC-6.4.0-2.28/lib64/libmpifort.so.12 (0x00007fd64be7b000)
        libmpi.so.12 => /software/software/impi/2018.1.163-iccifort-2018.1.163-GCC-6.4.0-2.28/lib64/libmpi.so.12 (0x00007fd64b1f6000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fd64aff2000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fd64adea000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fd64abce000)
        libm.so.6 => /lib64/libm.so.6 (0x00007fd64a8cc000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fd64a4fe000)
        libgcc_s.so.1 => /software/software/GCCcore/6.4.0/lib64/libgcc_s.so.1 (0x00007fd65039a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fd6501b3000)


