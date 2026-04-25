================
ASE-driven DIRAC
================

installation
------------
(myenv) miroi@MIRO:~/work/software/dirac/trunk_cloned/ase_dirac/.pip install -e .
Obtaining file:///home/miroi/work/software/dirac/trunk_cloned/ase_dirac
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: ase in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase_dirac==1.0.0) (3.28.0b1)
Requirement already satisfied: numpy>=1.21.6 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase->ase_dirac==1.0.0) (1.26.4)
Requirement already satisfied: scipy>=1.8.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase->ase_dirac==1.0.0) (1.16.0)
Requirement already satisfied: matplotlib>=3.5.2 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from ase->ase_dirac==1.0.0) (3.10.3)
Requirement already satisfied: contourpy>=1.0.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (1.3.2)
Requirement already satisfied: cycler>=0.10 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (4.58.5)
Requirement already satisfied: kiwisolver>=1.3.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (1.4.8)
Requirement already satisfied: packaging>=20.0 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (25.0)
Requirement already satisfied: pillow>=8 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (11.3.0)
Requirement already satisfied: pyparsing>=2.3.1 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (2.4.7)
Requirement already satisfied: python-dateutil>=2.7 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /home/miroi/work/software/myenv/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib>=3.5.2->ase->ase_dirac==1.0.0) (1.17.0)
Building wheels for collected packages: ase_dirac
  Building editable for ase_dirac (pyproject.toml) ... done
  Created wheel for ase_dirac: filename=ase_dirac-1.0.0-0.editable-py3-none-any.whl size=3313 sha256=3a766cd787ab683c5b2b3cfbe95a0210f86cbdc2919e7850733e0566f7801f38
  Stored in directory: /tmp/pip-ephem-wheel-cache-2n0ds48a/wheels/df/dc/f5/947c96d9b3c3c1a56ed5c7d6f05a126679059f3098b24eb676
Successfully built ase_dirac
Installing collected packages: ase_dirac
Successfully installed ase_dirac-1.0.0

(myenv) miroi@MIRO:~/work/software/dirac/trunk_cloned/ase_dirac/.pip show ase_dirac
Name: ase_dirac
Version: 1.0.0
Summary: DIRAC ASE calculator
Home-page:
Author: Carlos M. R. Rocha
Author-email: c.rocha@esciencecenter.nl
License: Apache-2.0
Location: /home/miroi/work/software/myenv/lib/python3.12/site-packages
Editable project location: /home/miroi/work/software/dirac/trunk_cloned/ase_dirac
Requires: ase
Required-by:

test
----
(myenv) miroi@MIRO:~/work/software/dirac/trunk_cloned/ase_dirac/tests/.ls
mp2.py  pam@  test_dirac_ase.py

(myenv) miroi@MIRO:~/work/software/dirac/trunk_cloned/ase_dirac/tests/.pam --show

  DIRAC pam script running:

  user           : miroi
  machine        : MIRO
  date and time  : 2026-04-25 18:38:09.371225
  input dir      : /home/miroi/work/software/dirac/trunk_cloned/ase_dirac/tests
  pam command    : /home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/pam
  all pam args   : ['--show']
  executable     : /home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/dirac.x
  scratch dir    : /home/miroi/DIRAC_scratch_directory/miroi/DIRAC_dirac_output.19837_19837 (availspace=870.253[GB])
  output file    : dirac_output.19837.out
  DIRAC run      : parallel (launcher: /usr/bin/mpirun)
  local disks    : False
  rsh/rcp        : ssh / scp
  machine file   : None

  Setting MKL and OPENMP environment to default values (if not set already)
   MKL_NUM_THREADS = 1
   MKL_DYNAMIC = "FALSE"
   OMP_NUM_THREADS = 1
   OMP_DYNAMIC="FALSE"
  Setting environment variables (as specified explicitly or in .diracrc)
Operating system:      Linux
Current settings:
  Basis directories    /home/miroi/work/software/dirac/trunk_cloned/ase_dirac/tests:.:/home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/basis:/home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/basis_dalton:/home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/basis_ecp
  Scratch directory    /home/miroi/DIRAC_scratch_directory/miroi/DIRAC_dirac_output.19837_19837 (avail=870.253[GB])
  Relevant for parallel builds:
    mpi launcher          /usr/bin/mpirun
    mpirun extra args     None
    global scratch disk   True
    Machine file          None
    own mpirun command    None
  Profiler             None
  Debugger             None
  Dirac command        None
  Dirac executable     /home/miroi/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/dirac.x

own ase test
~~~~~~~~~~~~
 starting DIRAC for molecule ./NR-MP2_H2O.xyz with input ./NR-MP2_H2O.inp
  creating archive file  NR-MP2_H2O.tgz
  archived working files: ['MOLECULE.XYZ', 'DIRAC.INP']
  Could not construct hdf5 checkpoint file
  exit           : ABNORMAL (CHECK DIRAC OUTPUT)
Calculation NR-MP2_H2O could not be run correctly, please check
 starting DIRAC for molecule ./X2Cmmf-MP2_H2O.xyz with input ./X2Cmmf-MP2_H2O.inp
  creating archive file  X2Cmmf-MP2_H2O.tgz
  archived working files: ['MOLECULE.XYZ', 'DIRAC.INP']
  Could not construct hdf5 checkpoint file
  exit           : ABNORMAL (CHECK DIRAC OUTPUT)
Calculation X2Cmmf-MP2_H2O could not be run correctly, please check
 starting DIRAC for molecule ./DCG-MP2_H2O.xyz with input ./DCG-MP2_H2O.inp
  creating archive file  DCG-MP2_H2O.tgz
  archived working files: ['MOLECULE.XYZ', 'DIRAC.INP']
  Could not construct hdf5 checkpoint file
  exit           : ABNORMAL (CHECK DIRAC OUTPUT)
Calculation DCG-MP2_H2O could not be run correctly, please check
 starting DIRAC for molecule ./NR-MP2_N2.xyz with input ./NR-MP2_N2.inp
  creating archive file  NR-MP2_N2.tgz
  archived working files: ['MOLECULE.XYZ', 'DIRAC.INP']
  Could not construct hdf5 checkpoint file
  exit           : ABNORMAL (CHECK DIRAC OUTPUT)
Calculation NR-MP2_N2 could not be run correctly, please check
 starting DIRAC for molecule ./X2Cmmf-MP2_N2.xyz with input ./X2Cmmf-MP2_N2.inp
  creating archive file  X2Cmmf-MP2_N2.tgz
  archived working files: ['MOLECULE.XYZ', 'DIRAC.INP']
  Could not construct hdf5 checkpoint file
  exit           : ABNORMAL (CHECK DIRAC OUTPUT)
Calculation X2Cmmf-MP2_N2 could not be run correctly, please check
 starting DIRAC for molecule ./DCG-MP2_N2.xyz with input ./DCG-MP2_N2.inp
  creating archive file  DCG-MP2_N2.tgz
  archived working files: ['MOLECULE.XYZ', 'DIRAC.INP']
  Could not construct hdf5 checkpoint file
  exit           : ABNORMAL (CHECK DIRAC OUTPUT)


