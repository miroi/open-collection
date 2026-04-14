mpi-test-suite
=============

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/.git clone git@github.com:open-mpi/mpi-test-suite.git mpi-test-suite_intel2025
Cloning into 'mpi-test-suite_intel2025'...
remote: Enumerating objects: 1595, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 1595 (delta 21), reused 19 (delta 19), pack-reused 1543 (from 2)
Receiving objects: 100% (1595/1595), 544.70 KiB | 1.78 MiB/s, done.
Resolving deltas: 100% (1212/1212), done.
Updating files: 100% (136/136), done.

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/.ls
LICENSE      cmdline.ggo     dynamic/  mpi_test_suite.c  threaded/   tst_output.c   tst_threads.h
Makefile.am  coll/           env/      mpi_test_suite.h  tst_comm.c  tst_output.h   tst_types.c
README.md    compile_info.h  io/       one-sided/        tst_comm.h  tst_tests.c
autogen.sh*  configure.ac    m4/       p2p/              tst_file.c  tst_threads.c
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/.

module add intel/v2025.3.1 Autoconf/v2.73

see error https://github.com/open-mpi/mpi-test-suite/issues/24

janko's autotools
-----------------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/.module purge
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/.export MODULEPATH=/cvmfs/nica.jinr.ru/sw/202309/MODULES/slc9_x86-64:$MODULEPATH
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/.module add autotools
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/.module list
Currently Loaded Modules:
  1) autotools/v1.7.0-1

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/openmpi/mpi-test-suite/mpi-test-suite_intel2025/../autogen.sh
Can't locate File/Copy.pm in @INC (you may need to install the File::Copy module) (@INC contains: /cvmfs/nica.jinr.ru/sw/202309/slc9_x86-64/autotools/v1.7.0-1/share/autoconf /usr/local/lib64/perl5/5.32 /usr/local/share/perl5/5.32 /usr/lib64/perl5/vendor_perl /usr/share/perl5/vendor_perl /usr/lib64/perl5 /usr/share/perl5) at /cvmfs/nica.jinr.ru/sw/202309/slc9_x86-64/autotools/v1.7.0-1/bin/autoreconf line 49.
BEGIN failed--compilation aborted at /cvmfs/nica.jinr.ru/sw/202309/slc9_x86-64/autotools/v1.7.0-1/bin/autoreconf line 49.



