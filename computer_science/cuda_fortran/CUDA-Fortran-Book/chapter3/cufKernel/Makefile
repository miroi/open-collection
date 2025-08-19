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

FCFLAGS ?= -O2

# Uncomment the CUDAFLAGS line if you have hardware requirements that
# require a specific compute capability
# CUDAFLAGS ?= -gpu=cc60

all: build run verify

build: cufKernel.cuf
	$(FC) $(FCFLAGS) $(CUDAFLAGS) -o cufKernel.$(EXE) $<

run: cufKernel.$(EXE)
	$(RUN) ./cufKernel.$(EXE)

verify:

clean:
	@echo 'Cleaning up...'
	@rm -rf cufKernel.$(EXE) *.$(OBJ) *.mod *.dwf *.pdb prof
