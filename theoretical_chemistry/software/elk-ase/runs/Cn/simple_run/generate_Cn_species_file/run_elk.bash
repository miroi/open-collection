#!/bin/bash
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=4
export OMP_STACKSIZE=512M
ulimit -Ss unlimited
elk
