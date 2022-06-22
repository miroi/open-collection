QE-devel with GPU
=================

Login interactively onto GPU-node
---------------------------------
mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu-compile -t 1:00:00  -A m2_jgu-gpu-qe-calcs bash -i

better is longer time for compilation

mirilias@login22.mogon:~/work/software/quantum_espresso/qe-devel/.srun --pty -p m2_gpu -t 4:00:00  -A m2_jgu-gpu-qe-calcs bash -i

Loading necessary modules
-------------------------
mirilias@s0026.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ml load devel/CMake/3.21.1 mpi/impi/2021.5.1-intel-compilers-2022.0.2  system/CUDA/11.4.2 compiler/PGI/20.4-GCC-8.3.0  compiler/NVHPC/21.7   numlib/imkl/2022.0.2

mirilias@s0014.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ml

Currently Loaded Modules:
  1) numlib/imkl/2022.0.2
  2) devel/CMake/3.21.1
  3) system/CUDA/11.4.2
  4) compiler/PGI/20.4-GCC-8.3.0
  5) system/CUDAcore/11.2.2
  6) compiler/NVHPC/21.7
  7) compiler/GCCcore/11.2.0
  8) compiler/intel-compilers/2022.0.2
  9) lib/UCX/1.11.2-GCCcore-11.2.0
 10) mpi/impi/2021.5.1-intel-compilers-2022.0.2


see https://gitlab.com/QEF/q-e/-/issues/513#note_999729587

Buildup and compilation
------------------------
 mirilias@s0014.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.cmake -D QE_ENABLE_CUDA=ON -D QE_ENABLE_MPI_GPU_AWARE=ON -D CMAKE_Fortran_COMPILER=nvfortran -D CMAKE_C_COMPILER=nvc    ..
.
.
[100%] Building Fortran object EPW/CMakeFiles/qe_epw.dir/src/eliashberg.f90.o
[100%] Linking Fortran static library ../lib/libqe_epw.a
[100%] Built target qe_epw
Scanning dependencies of target qe_epw_exe
[100%] Building Fortran object EPW/CMakeFiles/qe_epw_exe.dir/src/epw.f90.o
[100%] Linking Fortran executable ../bin/epw.x
[100%] Built target qe_epw_exe
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.

mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ls bin/
abcoeff_to_eps.x*  dynmat.x*          fs.x*             manycp.x*              pmw.x*           pwcond.x*              turbo_spectrum.x*
all_currents.x*    ef.x*              graph.x*          matdyn.x*              postahc.x*       pwi2xsf.x*             upfconv.x*
alpha2f.x*         epa.x*             gww_fit.x*        memory_pw4gww.x*       postw90.x*       pw.x*                  virtual_v2.x*
average.x*         epsilon_Gaus.x*    gww.x*            molecularnexafs.x*     ppacf.x*         q2qstar.x*             w90chk2chk.x*
bands_unfold.x*    epsilon.x*         head.x*           molecularpdos.x*       pp_disca.x*      q2r.x*                 wannier90.x*
bands.x*           epw.x*             hgh2qe.x*         neb.x*                 pprism.x*        scan_ibrav.x*          wannier_ham.x*
bse_main.x*        ev.x*              hp.x*             open_grid.x*           pp_spctrlfn.x*   simple_bse.x*          wannier_plot.x*
casino2upf.x*      fd_ef.x*           ibrav2cell.x*     path_interpolation.x*  pp.x*            simple_ip.x*           wfck2r.x*
cell2ibrav.x*      fd_ifc.x*          initial_state.x*  pawplot.x*             projwfc.x*       simple.x*              wfdd.x*
cppp.x*            fd.x*              kcwpp_interp.x*   phcg.x*                pw2bgw.x*        spectra_correction.x*  xspectra.x*
cp.x*              fermi_int_0.x*     kcwpp_sh.x*       ph.x*                  pw2critic.x*     sumpdos.x*             ZG.x*
disca.x*           fermi_int_1.x*     kcw.x*            plan_avg.x*            pw2gt.x*         turbo_davidson.x*
dos_sp.x*          fermi_proj.x*      kpoints.x*        plotband.x*            pw2gw.x*         turbo_eels.x*
dos.x*             fermi_velocity.x*  lambda.x*         plotproj.x*            pw2wannier90.x*  turbo_lanczos.x*
dvscf_q2r.x*       fqha.x*            ld1.x*            plotrho.x*             pw4gww.x*        turbo_magnon.x*

Linked objects
---------------
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.ldd bin/pw.x
        linux-vdso.so.1 (0x00007ffebe3c5000)
        libmpifort.so.12 => /cluster/easybuild/broadwell/software/impi/2021.5.1-intel-compilers-2022.0.2/mpi/2021.5.1/lib/libmpifort.so.12 (0x00007f48703c4000)
        libmpi.so.12 => /cluster/easybuild/broadwell/software/impi/2021.5.1-intel-compilers-2022.0.2/mpi/2021.5.1/lib/release/libmpi.so.12 (0x00007f486eb8f000)
        librt.so.1 => /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/librt.so.1 (0x00007f486e987000)
        libpthread.so.0 => /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libpthread.so.0 (0x00007f486e767000)
        libdl.so.2 => /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libdl.so.2 (0x00007f486e563000)
        libacchost.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libacchost.so (0x00007f486e2f3000)
        libmkl_intel_lp64.so.2 => /cluster/easybuild/broadwell/software/imkl/2022.0.2/mkl/2022.0.2/lib/intel64/libmkl_intel_lp64.so.2 (0x00007f486d453000)
        libmkl_intel_thread.so.2 => /cluster/easybuild/broadwell/software/imkl/2022.0.2/mkl/2022.0.2/lib/intel64/libmkl_intel_thread.so.2 (0x00007f4869cf1000)
        libmkl_core.so.2 => /cluster/easybuild/broadwell/software/imkl/2022.0.2/mkl/2022.0.2/lib/intel64/libmkl_core.so.2 (0x00007f486593c000)
        libiomp5.so => /cluster/easybuild/broadwell/software/imkl/2022.0.2/compiler/2022.0.2/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007f486551b000)
        libm.so.6 => /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so.6 (0x00007f4865199000)
        libcufft.so.10 => /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib64/libcufft.so.10 (0x00007f48599ea000)
        libcudaforwraprand.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libcudaforwraprand.so (0x00007f48597e7000)
        libcurand.so.10 => /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib64/libcurand.so.10 (0x00007f4854080000)
        libcusolver.so.11 => /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib64/libcusolver.so.11 (0x00007f483bfca000)
        libcublas.so.11 => /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib64/libcublas.so.11 (0x00007f4835007000)
        libcublasLt.so.11 => /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib64/libcublasLt.so.11 (0x00007f4829426000)
        libcudaforwrapblas.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libcudaforwrapblas.so (0x00007f48291e9000)
        libcudart.so.11.0 => /cluster/easybuild/broadwell/software/CUDAcore/11.2.2/lib64/libcudart.so.11.0 (0x00007f4828f5a000)
        libcudafor_110.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libcudafor_110.so (0x00007f48253a7000)
        libcudafor.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libcudafor.so (0x00007f482518a000)
        libaccdevaux.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libaccdevaux.so (0x00007f4824f7e000)
        libacccuda.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libacccuda.so (0x00007f4824c4c000)
        libcudadevice.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libcudadevice.so (0x00007f4824a39000)
        libcudafor2.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libcudafor2.so (0x00007f4824836000)
        libnvf.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libnvf.so (0x00007f482420c000)
        libnvomp.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libnvomp.so (0x00007f4823592000)
        libnvcpumath.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libnvcpumath.so (0x00007f482315d000)
        libnvc.so => /cluster/easybuild/broadwell/software/NVHPC/21.7/Linux_x86_64/21.7/compilers/lib/libnvc.so (0x00007f4822f05000)
        libc.so.6 => /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libc.so.6 (0x00007f4822b40000)
        libgcc_s.so.1 => /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libgcc_s.so.1 (0x00007f4822928000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f4870778000)
        libstdc++.so.6 => /cluster/easybuild/broadwell/software/compiler/GCCcore/8.3.0/lib64/libstdc++.so.6 (0x00007f4870805000)
mirilias@s0021.mogon:~/work/software/quantum_espresso/qe-devel/build_gpu/.


