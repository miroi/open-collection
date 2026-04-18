====================================================
Quantum Espresso buildup openmpi-5.0.9-intel2025.3.1
====================================================

inspiration from /lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/openmpi/buildup_on_servers/jinr_ru/hydra_jinr_ru/build_openmpi-5.0.9-intelv2025.3.1/openmpi_examples

works for icelake ! not for cascade nodes !

    Building Fortran object CMakeFiles/cmTC_bd45e.dir/testFortranCompiler.f.o
    /lustre/projects/m/milias/work/software/openmpi/openmpi-5.0.9-intelv2025.3.1/install_openmpi5.0.9-intel2025.3.1_c/bin/mpif90   -march=core-avx2 -g -traceback  -c /lustre/project
s/m/milias/work/software/quantum-espresso/git_cloned/q-e/build_intel2025.3.1-openmpi5.0.9_libxc_mkl_scalapack/CMakeFiles/CMakeScratch/TryCompile-SqEcgC/testFortranCompiler.f -o CMak
eFiles/cmTC_bd45e.dir/testFortranCompiler.f.o

    Please verify that both the operating system and the processor support Intel(R) AVX512VBMI, AVX512_VPOPCNTDQ, AVX512_BITALG and AVX512_VBMI2 instructions.

    gmake[1]: *** [CMakeFiles/cmTC_bd45e.dir/build.make:78: CMakeFiles/cmTC_bd45e.dir/testFortranCompiler.f.o] Error 1
