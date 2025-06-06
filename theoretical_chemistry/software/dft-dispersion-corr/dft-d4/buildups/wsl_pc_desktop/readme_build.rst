======
DFT-D4
======


milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/.git clone git@github.com:dftd4/dftd4.git

mkdir _build

milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/dftd4/_build/.cmake ..
.
.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/dft-d4/dftd4/_build

milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/dftd4/_build/.make
.
.
[ 96%] Built target dftd4-api-tester
Scanning dependencies of target dftd4-tester
[ 97%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_dftd4.f90.o
[ 97%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_model.f90.o
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_pairwise.f90.o
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_param.f90.o
[ 99%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_periodic.f90.o
[100%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/main.f90.o
[100%] Linking Fortran executable dftd4-tester
[100%] Built target dftd4-tester

check executable
~~~~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/dftd4/_build/.ldd app/dftd4
        linux-vdso.so.1 (0x00007ffe00bfb000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x0000727742c00000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x000072774347c000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x0000727743432000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x0000727742800000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000072774334b000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000727742400000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x0000727742be0000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x0000727742b98000)
        /lib64/ld-linux-x86-64.so.2 (0x0000727743630000)


.~/work/software/dft-d4/dftd4/_build/app/dftd4 -h
Usage: dftd4 [run|param] [options] ...

Generally Applicable Atomic-Charge Dependent London Dispersion Correction.
Takes an geometry input to calculate the D4(S) dispersion correction.
Periodic calculations are performed automatically for periodic input formats.
Reads .CHRG file (if present) from the same directory as the input.
Specify the functional to select the correct parameters.

Commands

  run       Evaluate dispersion correction on the provided input structure.
            Periodic calculations are performed automatically for periodic inputs
            If no command is specified run is selected by default.

  param     Inspect damping parameters.

Options

-c,--charge <real>       Set charge to molecule, overwrites .CHRG file
-i,--input <format>      Hint for the format of the input file
-f,--func <method>       Use damping parameters for given functional
   --param <list>        Specify parameters for rational damping,
                         expected order is s6, s8, a1, a2 (requires four arguments)
   --mbdscale <s9>       Use scaled ATM three-body dispersion
   --zeta <list>         Adjust charge scaling parameters, takes two reals,
                         expected order is ga, gc (default: 3.0, 2.0)
   --wfactor <real>      Adjust weighting factor for interpolation (only D4)
                         (default: 6.0)
-m,--model <model>       Use specific D4 model (options: D4 (default), D4S)
-g,--grad [file]         Evaluate molecular gradient and virial,
                         write results to file (default: dftd4.txt),
                         attempts to add to Turbomole gradient and gradlatt files
   --hessian             Evaluate molecular hessian
   --property            Show dispersion related atomic and system properties
   --pair-resolved       Calculate pairwise representation of dispersion energy
   --noedisp             Disable writing of dispersion energy to .EDISP file
   --json [file]         Dump results to JSON output (default: dftd4.json)
-v,--verbose             Show more, can be used multiple times
-s,--silent              Show less, use twice to supress all output
   --version             Print program version and exit
   --citation            Print citation information and exit
   --license             Print license header and exit
-h,--help                Show this help message

