# SPDX-FileCopyrightText: Copyright (c) 2019 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

FC ?= nvfortran
OBJ = o
EXE = out
UNAME := $(shell uname -a)
ifeq ($(findstring _NT, $(UNAME)), _NT)
	OBJ = obj
	EXE = exe
endif

NVXX := nvcc
FCFLAGS ?= -O2

# nvcc requires specifying compute capability to generate code for. The following logic
# attempts to figure this out automatically by looking through GPUs on current systems.
# However, it if fails to do so it may need done manually like the example.
# Example for Ampere: --generate-code arch=compute_80,code=sm_80
SYSCOMPCAP := $(shell nvaccelinfo | grep "Default Target:" | awk -F "cc" '{ print $$2 }' | sort | uniq)
NVCCOPTIONS := $(foreach CCAP,$(SYSCOMPCAP), --generate-code arch=compute_$(CCAP),code=sm_$(CCAP))

# Uncomment the CUDAFLAGS line if you have hardware requirements that
# require a specific compute capability
# CUDAFLAGS ?= -gpu=cc60

all: build run verify

build: fCallingC.cuf zero.cu
	$(NVXX) -O3 $(NVCCOPTIONS) -c zero.cu
	$(FC) $(FCFLAGS) $(CUDAFLAGS) -gpu=nordc -o fCallingC.$(EXE) zero.o fCallingC.cuf

run: fCallingC.$(EXE)
	$(RUN) ./fCallingC.$(EXE)

verify:

clean:
	@echo 'Cleaning up...'
	@rm -rf fCallingC.$(EXE) *.$(OBJ) *.mod *.dwf *.pdb prof
