# SPDX-FileCopyrightText: Copyright (c) 2019 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

CC ?= nvc
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

build: transposeP2P.cuf timing.f90 wallclock.c
	$(FC) $(FCLAGS) -c timing.f90
	$(CC) $(CCFLAGS) -c wallclock.c
	$(FC) $(FCFLAGS) $(CUDAFLAGS) -o transposeP2P.$(EXE) timing.$(OBJ) wallclock.$(OBJ) $<

run: transposeP2P.$(EXE)
	$(RUN) ./transposeP2P.$(EXE)

verify:

clean:
	@echo 'Cleaning up...'
	@rm -rf transposeP2P.$(EXE) *.$(OBJ) *.mod *.dwf *.pdb prof
