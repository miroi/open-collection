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



