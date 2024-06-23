Quantum Espresso tests
======================

milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/test-suite/.make
To run Quantum ESPRESSO test-suite, type at the shell prompt:

  make target

where <target> identifies an action
 run-tests-XX [NPROCS=N]        : run tests [optionally, on N processors]
 for XX=pw, cp, ph, epw, hp, tddfpt, kcw, all_currents, pp, zg, xsd-pw
 run-tests [NPROCS=N]           : run all tests above (except the last four)
 run-custom-test testdir=DIR [NPROCS=N]: run test in DIR only
 compare                     : compare last output with reference
 pseudo                      : download needed PPs into ESPRESSO_PSEUDO
 clean                       : clean stdout/sderr of all tests

For additional advanced commands and settings please manually inspect
ENVIRONMENT and Makefile files
milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/test-suite/.

