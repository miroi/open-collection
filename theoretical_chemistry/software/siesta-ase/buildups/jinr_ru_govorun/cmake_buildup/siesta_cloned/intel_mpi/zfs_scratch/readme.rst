============================
SIESTA buildup with IntelMPI
============================

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/.git log .
commit 0d97129a2aa615d6ef3371dfcdfa9fcc0c869113
Author: Jos<C3><A9> Mar<C3><AD>a Escart<C3><AD>n Esteban <jm.escartin@icn2.cat>
Date:   Tue Dec 16 11:04:07 2025 +0100

    Manual format change to 5.4.2 release notes.



milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/.git submodule update --init --recursive
Submodule 'External/DFTD3/mctc-lib' (https://github.com/grimme-lab/mctc-lib.git) registered for path 'External/DFTD3/mctc-lib'
Submodule 'External/DFTD3/mstore' (https://github.com/grimme-lab/mstore.git) registered for path 'External/DFTD3/mstore'
Submodule 'External/DFTD3/s-dftd3' (https://github.com/dftd3/simple-dftd3.git) registered for path 'External/DFTD3/s-dftd3'
Submodule 'External/DFTD3/test-drive' (https://github.com/fortran-lang/test-drive.git) registered for path 'External/DFTD3/test-drive'
Submodule 'External/DFTD3/toml-f' (https://github.com/toml-f/toml-f.git) registered for path 'External/DFTD3/toml-f'
Submodule 'External/ELSI-project/elsi_interface' (https://gitlab.com/elsi_project/elsi_interface.git) registered for path 'External/ELSI-project/elsi_interface'
Submodule 'External/Lua-Engine/flook' (https://github.com/ElectronicStructureLibrary/flook.git) registered for path 'External/Lua-Engine/flook'
Submodule 'External/libfdf' (https://gitlab.com/siesta-project/libraries/libfdf.git) registered for path 'External/libfdf'
Submodule 'External/libgridxc' (https://gitlab.com/siesta-project/libraries/libgridxc.git) registered for path 'External/libgridxc'
Submodule 'External/libpsml' (https://gitlab.com/siesta-project/libraries/libpsml.git) registered for path 'External/libpsml'
Submodule 'External/xmlf90' (https://gitlab.com/siesta-project/libraries/xmlf90.git) registered for path 'External/xmlf90'
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/DFTD3/mctc-lib'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/DFTD3/mstore'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/DFTD3/s-dftd3'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/DFTD3/test-drive'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/DFTD3/toml-f'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/ELSI-project/elsi_interface'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/Lua-Engine/flook'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/libfdf'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/libgridxc'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/libpsml'...
Cloning into '/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/External/xmlf90'...
Submodule path 'External/DFTD3/mctc-lib': checked out '87a46cdf5281ad75909083c4f72354d54abdf95d'
Submodule path 'External/DFTD3/mstore': checked out '974fb59092f74c7db86a1a11b1aafb3cbf311aa3'
Submodule path 'External/DFTD3/s-dftd3': checked out 'f147b265d8b53dcf1666d7b0aba579ec02233fe8'
Submodule path 'External/DFTD3/test-drive': checked out '9c3401e30dbd2da1add77aaa252a4c6928fe39a1'
Submodule path 'External/DFTD3/toml-f': checked out 'e49f5523e4ee67db6628618864504448fb8c8939'
Submodule path 'External/ELSI-project/elsi_interface': checked out '2f2ead063700fab39d2253d81928ebb03baefb9f'
Submodule path 'External/Lua-Engine/flook': checked out '7b644a2ace47e43772006764a58166b6635e8941'
Submodule path 'External/libfdf': checked out '206a3d6c4628e584743bd5cd483d0e2e66e95b7c'
Submodule path 'External/libgridxc': checked out '022d2a6371eed0db272ac6922289921f62f30c21'
Submodule path 'External/libpsml': checked out 'b7049e4de25333fe8bd2dbf9a3495ef0f77ba168'
Submodule path 'External/xmlf90': checked out '963fe5d11487233d43ac59dd0c1340a7b2cc3dc5'

MKL
~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/.module load intel/oneapi
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/siesta/git_cloned/siesta/.elp
$LD_LIBRARY_PATH: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/vpl/latest/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/libfabric/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/lib/release:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/itac/latest/slib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/ippcp/latest/lib/intel64:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/ipp/latest/lib/intel64:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/dnnl/latest/cpu_dpcpp_gpu_dpcpp/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/debugger/latest/dep//lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/debugger/10.1.2/libipt/intel64/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/debugger/10.1.2/gdb/intel64/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/dal/latest/lib/intel64:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/lib:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/lib/x64:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/lib/emu:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/clck/latest/lib/intel64:/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/ccl/latest/lib/cpu_gpu_dpcpp


ls /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_*
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_ilp64.a
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_ilp64.so@
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_ilp64.so.1*
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_lp64.a
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_lp64.so@
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_scalapack_lp64.so.1*
