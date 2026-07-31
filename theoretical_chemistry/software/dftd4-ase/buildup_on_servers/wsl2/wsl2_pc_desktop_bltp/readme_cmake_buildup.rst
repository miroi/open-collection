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

list of functionals
~~~~~~~~~~~~~~~~~~~~
~/work/software/dft-d4/dftd4/_build/app/dftd4 param --list
List of available functionals:
am05
b-lyp blyp
b-p bp86 bp b-p86
b1b95
b1lyp b1-lyp
b1p b1-p b1p86
b1pw b1-pw b1pw91
b2gpplyp b2gp-plyp
b2plyp b2-plyp
b3-lyp b3lyp
b3p b3-p b3p86
b3pw b3-pw b3pw91
b97
b97d
b97m
bh-lyp bhlyp
bpbe
bpw b-pw
cam-b3lyp camb3lyp
cam-qtp01 camqtp01 camqtp(01) cam-qtp(01)
dftb(matsci)
dftb(mio)
dftb(pbc)
dftb3 dftb(3ob)
dodblyp dod-blyp
dodpbe dod-pbe
dodpbeb95 dod-pbeb95
dodpbep86 dod-pbep86
dodsvwn dod-svwn
dsdblyp dsd-blyp
dsdpbe dsd-pbe
dsdpbeb95 dsd-pbeb95
dsdpbep86 dsd-pbep86
dsdsvwn dsd-svwn
glyp g-lyp
hf
hse03
hse06
hse12
hse12s
hsesol
kpr2scan50 kpr²scan50 kpr2scan50 kpr²scan50
lb94
lc-blyp lcblyp
lc-dftb dftb(ob2)
lc-wpbe lcwpbe lc-ωpbe lcωpbe lc-omegapbe lcomegapbe
lc-wpbeh lcwpbeh lc-ωpbeh lcωpbeh lc-omegapbeh lcomegapbeh
lh07ssvwn lh07s-svwn
lh07tsvwn lh07t-svwn
lh12ctssifpw92 lh12ct-ssifpw92
lh12ctssirpw92 lh12ct-ssirpw92
lh14tcalpbe lh14t-calpbe
lh20t
m06
m06l
mn12sx mn12-sx
mpw1b95
mpw1lyp mpw1-lyp
mpw1pw mpw1-pw mpw1pw91
mpw2plyp
mpwb1k
mpwlyp mpw-lyp
mpwpw mpw-pw mpwpw91
o-lyp olyp
o3-lyp o3lyp
opbe
pbe
pbe0
pbe02 pbe0-2
pbe0dh pbe0-dh
pbesol
pr2scan50 pr²scan50 pr2scan50 pr²scan50
pr2scan69 pr²scan69 pr2scan69 pr²scan69
pw1pw pw1-pw
pw6b95
pw86pbe
pw91
pwp pw-p pw91p86
pwp1
pwpb95
r2scan r²scan
r2scan-3c r²scan-3c r2scan_3c r²scan_3c r2scan3c
r2scan-cidh r²scan-cidh r2scancidh r²scancidh
r2scan-qidh r²scan-qidh r2scanqidh r²scanqidh
r2scan0 r²scan0
r2scan0-2 r²scan0-2 r2scan02 r²scan02
r2scan0-dh r²scan0-dh r2scan0dh r²scan0dh
r2scan50 r²scan50
r2scanh r²scanh
revdod-pbep86 revdodpbep86
revdsd-blyp revdsdblyp
revdsd-pbe revdsd-pbepbe revdsdpbe revdsdpbepbe
revdsd-pbep86 revdsdpbep86
revpbe
revpbe0
revpbe0dh revpbe0-dh
revpbe38
revtpss
revtpss0
revtpssh
rpbe
rpw86pbe
rscan
scan
tpss
tpss0
tpssh
wb97 ωb97 omegab97
wb97m ωb97m omegab97m
wb97m-rev ωb97m-rev omegab97m-rev wb97m_rev ωb97m_rev omegab97m_rev
wb97x ωb97x omegab97x
wb97x-3c ωb97x-3c omegab97x-3c wb97x_3c ωb97x_3c omegab97x_3c
wb97x-rev ωb97x-rev omegab97x-rev wb97x_rev ωb97x_rev omegab97x_rev
wb97x_2008 ωb97x_2008 omegab97x_2008 wb97x-2008 ωb97x-2008 omegab97x-2008
wpr2scan50 wpr²scan50 wpr2scan50 wpr²scan50
wr2scan wr²scan
x-lyp xlyp
x3-lyp x3lyp
