===================
Govorun's GPU nodes
===================

see https://pm.jinr.ru/issues/10626#note-1

also fix:

CUDA-Fortran-Book/appendixC/fCallingC/Makefile:

build: fCallingC.cuf zero.cu
        $(NVXX) -O3 $(NVCCOPTIONS) -c zero.cu
        #$(FC) $(FCFLAGS) $(CUDAFLAGS) -gpu=nordc -o fCallingC.$(EXE) zero.o fCallingC.cuf
        $(FC) $(FCFLAGS) $(CUDAFLAGS) -gpu=nordc -c++libs -o fCallingC.$(EXE) zero.o fCallingC.cuf

