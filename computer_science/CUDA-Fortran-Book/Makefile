# SPDX-FileCopyrightText: Copyright (c) 2017 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

#
# just typing 'make OPTIONS=$(OPT)' prints out this help message
#

UNAME := $(shell uname -a)
ifneq ($(findstring _NT, $(UNAME)), _NT)
help:
	@echo "To build and run a specific example, do the following:"
	@echo "    "
	@echo "Chapter 1  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) increment                : Section 1.3.1"
	@echo "make OPTIONS=$(OPT) increment2               : Section 1.3.2"
	@echo "make OPTIONS=$(OPT) multidim                 : Section 1.3.3"
	@echo "make OPTIONS=$(OPT) deviceQuery              : Section 1.4"
	@echo "    "
	@echo "Chapter 2  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) limitingFactor2          : Section 2.2"
	@echo "make OPTIONS=$(OPT) peakBandwidth            : Section 2.3.1"
	@echo "    "
	@echo "Chapter 3  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) pinned                   : Section 3.1.1"
	@echo "make OPTIONS=$(OPT) async                    : Section 3.1.3"
	@echo "make OPTIONS=$(OPT) offsetNstride            : Section 3.2.2"
	@echo "make OPTIONS=$(OPT) local                    : Section 3.2.4"
	@echo "make OPTIONS=$(OPT) constant                 : Section 3.2.5"
	@echo "make OPTIONS=$(OPT) sharedExample            : Section 3.3.3"
	@echo "make OPTIONS=$(OPT) transpose                : Section 3.4"
	@echo "make OPTIONS=$(OPT) parallelism              : Section 3.5.1"
	@echo "make OPTIONS=$(OPT) cufILP                   : Section 3.7"
	@echo "make OPTIONS=$(OPT) cufKernel                : Section 3.7"
	@echo "make OPTIONS=$(OPT) cufKernel2D              : Section 3.7"
	@echo "make OPTIONS=$(OPT) cufReduction             : Section 3.7"
	@echo "    "
	@echo "Chapter 4  "
	@echo "    "
	@echo "P2P "
	@echo "make OPTIONS=$(OPT) minimal                  : Section 4.1"
	@echo "make OPTIONS=$(OPT) p2pAccess                : Section 4.1.1"
	@echo "make OPTIONS=$(OPT) directTransfer           : Section 4.1.2"
	@echo "make OPTIONS=$(OPT) p2pBandwidth             : Section 4.1,2"
	@echo "make OPTIONS=$(OPT) transposeP2P             : Section 4.1.3"
	@echo "MPI "
	@echo "make OPTIONS=$(OPT) [NPROCS=n] mpiDevices    : Section 4.2.1"
	@echo "make OPTIONS=$(OPT) [NPROCS=n] assignDevice  : Section 4.2.1"
	@echo "make OPTIONS=$(OPT) [NPROCS=n] transposeMPI  : Section 4.2.2"
	@echo "    "
	@echo "Chapter 5  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) rng_gpu                  : Section 5.1"
	@echo "make OPTIONS=$(OPT) pi                       : Section 5.2"
	@echo "make OPTIONS=$(OPT) compute_pi_performance   : Section 5.3"
	@echo "make OPTIONS=$(OPT) mc_european              : Section 5.5"
	@echo "    "
	@echo "Chapter 6  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) finiteDifference         : Section 6.1"
	@echo "make OPTIONS=$(OPT) limitingFactor6          : Section 6.1"
	@echo "make OPTIONS=$(OPT) finiteDifferenceStr      : Section 6.1.4"
	@echo "    "
	@echo "Chapter 7  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) fft_test_c2c             : Section 7.1"
	@echo "make OPTIONS=$(OPT) fft_test_r2c             : Section 7.1"
	@echo "make OPTIONS=$(OPT) fft_derivative           : Section 7.2"
	@echo "make OPTIONS=$(OPT) exampleOverlapFFT        : Section 7.3"
	@echo "    "
	@echo "Appendix C  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) sgemmDevice              : Section C.1"
	@echo "make OPTIONS=$(OPT) fCallingC                : Section C.2"
	@echo "    "
	@echo "make OPTIONS=$(OPT) all                      : all of the above tests"
	@echo ""
	@echo "where NPROCS is set to the number of processors to test, default is 2."
else
help:
	@echo "To build and run a specific example, do the following:"
	@echo "    "
	@echo "Chapter 1  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) increment                : Section 1.3.1"
	@echo "make OPTIONS=$(OPT) increment2               : Section 1.3.2"
	@echo "make OPTIONS=$(OPT) multidim                 : Section 1.3.3"
	@echo "make OPTIONS=$(OPT) deviceQuery              : Section 1.4"
	@echo "    "
	@echo "Chapter 2  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) limitingFactor2          : Section 2.2"
	@echo "make OPTIONS=$(OPT) peakBandwidth            : Section 2.3.1"
	@echo "    "
	@echo "Chapter 3  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) pinned                   : Section 3.1.1"
	@echo "make OPTIONS=$(OPT) async                    : Section 3.1.3"
	@echo "make OPTIONS=$(OPT) offsetNstride            : Section 3.2.2"
	@echo "make OPTIONS=$(OPT) local                    : Section 3.2.4"
	@echo "make OPTIONS=$(OPT) constant                 : Section 3.2.5"
	@echo "make OPTIONS=$(OPT) sharedExample            : Section 3.3.3"
	@echo "make OPTIONS=$(OPT) transpose                : Section 3.4"
	@echo "make OPTIONS=$(OPT) parallelism              : Section 3.5.1"
	@echo "make OPTIONS=$(OPT) cufILP                   : Section 3.7"
	@echo "make OPTIONS=$(OPT) cufKernel                : Section 3.7"
	@echo "make OPTIONS=$(OPT) cufKernel2D              : Section 3.7"
	@echo "make OPTIONS=$(OPT) cufReduction             : Section 3.7"
	@echo "    "
	@echo "Chapter 4  "
	@echo "    "
	@echo "P2P "
	@echo "make OPTIONS=$(OPT) minimal                  : Section 4.1"
	@echo "make OPTIONS=$(OPT) p2pAccess                : Section 4.1.1"
	@echo "make OPTIONS=$(OPT) p2pBandwidth             : Section 4.1,2"
	@echo "make OPTIONS=$(OPT) transposeP2P             : Section 4.1.3"
	@echo "MPI "
	@echo "make OPTIONS=$(OPT) [NPROCS=n] mpiDevices    : Section 4.2.1"
	@echo "make OPTIONS=$(OPT) [NPROCS=n] assignDevice  : Section 4.2.1"
	@echo "    "
	@echo "Chapter 5  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) rng_gpu                  : Section 5.1"
	@echo "make OPTIONS=$(OPT) pi                       : Section 5.2"
	@echo "make OPTIONS=$(OPT) compute_pi_performance   : Section 5.3"
	@echo "make OPTIONS=$(OPT) mc_european              : Section 5.5"
	@echo "    "
	@echo "Chapter 6  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) finiteDifference         : Section 6.1"
	@echo "make OPTIONS=$(OPT) limitingFactor6          : Section 6.1"
	@echo "make OPTIONS=$(OPT) finiteDifferenceStr      : Section 6.1.4"
	@echo "    "
	@echo "Chapter 7  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) fft_test_c2c             : Section 7.1"
	@echo "make OPTIONS=$(OPT) fft_test_r2c             : Section 7.1"
	@echo "make OPTIONS=$(OPT) fft_derivative           : Section 7.2"
	@echo "make OPTIONS=$(OPT) exampleOverlapFFT        : Section 7.3"
	@echo "    "
	@echo "Appendix C  "
	@echo "    "
	@echo "make OPTIONS=$(OPT) sgemmDevice              : Section C.1"
	@echo "    "
	@echo "make OPTIONS=$(OPT) all                      : all of the above tests"
	@echo ""
	@echo "where NPROCS is set to the number of processors to test, default is 2."
endif

NPROCS ?= 2
CCFLAGS ?= $(OPTIONS)
CXXFLAGS ?= $(OPTIONS)
FCFLAGS ?= $(OPTIONS)

#
#  Chapter 1 examples
#
deviceQuery:
	cd chapter1/deviceQuery; make build; make run; make clean

increment:
	cd chapter1/increment; make build; make run; make clean

increment2:
	cd chapter1/increment2; make build; make run; make clean

multidim:
	cd chapter1/multidim; make build; make run; make clean



#
#  Chapter 2 examples
#
limitingFactor2:
	cd chapter2/limitingFactor; make build; make run; make clean

peakBandwidth:
	cd chapter2/peakBandwidth; make build; make run; make clean



#
#  Chapter 3 examples
#


async:
	cd chapter3/async; make build; make run; make clean

constant:
	cd chapter3/constant; make build; make run; make clean

cufILP:
	cd chapter3/cufILP; make build; make run; make clean

cufKernel:
	cd chapter3/cufKernel; make build; make run; make clean

cufKernel2D :
	cd chapter3/cufKernel2D ; make build; make run; make clean

cufReduction :
	cd chapter3/cufReduction ; make build; make run; make clean

local:
	cd chapter3/local; make build; make run; make clean

offsetNstride :
	cd chapter3/offsetNstride; make build; make run; make clean

parallelism:
	cd chapter3/parallelism; make build; make run; make clean

pinned:
	cd chapter3/pinned; make build; make run; make clean

sharedExample:
	cd chapter3/sharedExample; make build; make run; make clean

transpose:
	cd chapter3/transpose; make build; make run; make clean



#
#  Chapter 4 examples
#

# P2P

minimal:
	cd chapter4/P2P/minimal; make build; make run; make clean

p2pAccess:
	cd chapter4/P2P/p2pAccess; make build; make run; make clean

ifneq ($(findstring _NT, $(UNAME)), _NT)
directTransfer:
	cd chapter4/P2P/directTransfer; make build; make run; make clean
endif

p2pBandwidth:
	cd chapter4/P2P/p2pBandwidth; make build; make run; make clean

transposeP2P:
	cd chapter4/P2P/transposeP2P; make build; make run; make clean


# MPI

mpiDevices:
	cd chapter4/MPI/mpiDevices; make build; make NPROCS=$(NPROCS) run; make clean

assignDevice:
	cd chapter4/MPI/assignDevice; make build; make NPROCS=$(NPROCS) run; make clean

ifneq ($(findstring _NT, $(UNAME)), _NT)
transposeMPI:
	cd chapter4/MPI/transposeMPI; make build; make NPROCS=$(NPROCS) run; make clean
endif

#
#  Chapter 5 examples
#


rng_gpu:
	cd chapter5/rng_gpu; make build; make run; make clean

pi:
	cd chapter5/pi; make build; make run; make clean

compute_pi_performance:
	cd chapter5/compute_pi_performance; make build; make run; make clean

mc_european:
	cd chapter5/mc_european; make build; make run; make clean



#
#  Chapter 6 examples
#

finiteDifference:
	cd chapter6/finiteDifference; make build; make run; make clean

limitingFactor6:
	cd chapter6/limitingFactor; make build; make run; make clean

finiteDifferenceStr:
	cd chapter6/finiteDifferenceStr; make build; make run; make clean

#
#  Chapter 7 examples
#


fft_test_c2c:
	cd chapter7/fft_test_c2c; make build; make run; make clean

fft_test_r2c:
	cd chapter7/fft_test_r2c; make build; make run; make clean

fft_derivative:
	cd chapter7/fft_derivative; make build; make run; make clean

exampleOverlapFFT:
	cd chapter7/exampleOverlapFFT; make build; make run; make clean


#
#  Appendix C examples
#

sgemmDevice:
	cd appendixC/sgemmDevice; make build; make run; make clean

ifneq ($(findstring _NT, $(UNAME)), _NT)
fCallingC:
	cd appendixC/fCallingC; make build; make run; make clean
endif


ifneq ($(findstring _NT, $(UNAME)), _NT)
all: deviceQuery increment increment2 multidim limitingFactor2 \
     peakBandwidth async constant cufILP cufKernel \
     cufKernel2D cufReduction local offsetNstride parallelism \
     pinned sharedExample transpose \
     minimal p2pAccess directTransfer p2pBandwidth transposeP2P \
     mpiDevices assignDevice transposeMPI \
     rng_gpu pi compute_pi_performance mc_european finiteDifference \
     limitingFactor6 finiteDifferenceStr \
     fft_test_c2c fft_test_r2c fft_derivative exampleOverlapFFT \
     sgemmDevice fCallingC
else
all: deviceQuery increment increment2 multidim limitingFactor2 \
     peakBandwidth async constant cufILP cufKernel \
     cufKernel2D cufReduction local offsetNstride parallelism \
     pinned sharedExample transpose \
     minimal p2pAccess p2pBandwidth transposeP2P \
     mpiDevices assignDevice \
     rng_gpu pi compute_pi_performance mc_european finiteDifference \
     limitingFactor6 finiteDifferenceStr \
     fft_test_c2c fft_test_r2c fft_derivative exampleOverlapFFT \
     sgemmDevice
endif
