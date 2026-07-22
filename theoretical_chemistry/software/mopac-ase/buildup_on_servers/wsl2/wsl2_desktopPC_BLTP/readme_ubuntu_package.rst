MOPAC as Ubuntu package
=======================


sudo apt-get install mopac


milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/.dpkg -l mopac
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version       Architecture Description
+++-==============-=============-============-=================================
ii  mopac          22.0.6+dfsg-1 amd64        Molecular Orbital PACkage (MOPAC)


milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/.dpkg -S mopac
mopac: /usr/bin/mopac
mopac: /usr/bin/mopac-param
mopac: /usr/share/doc/mopac/changelog.Debian.gz
mopac: /usr/share/doc/mopac/CITATION.cff
libopenbabel7: /usr/lib/x86_64-linux-gnu/openbabel/3.1.1/mopacformat.so
mopac: /usr/share/doc/mopac/copyright
mopac: /usr/share/doc/mopac
mopac: /usr/share/doc/mopac/AUTHORS.rst.gz

milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/.ldd  /usr/bin/mopac
        linux-vdso.so.1 (0x000077a6ffc24000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x000077a6ffba3000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x000077a6fe800000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x000077a6fe400000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000077a6fef17000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x000077a6fe307000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x000077a6feec1000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x000077a6ffb73000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000077a6fe000000)
        libopenblas.so.0 => /lib/x86_64-linux-gnu/libopenblas.so.0 (0x000077a6fbc20000)
        /lib64/ld-linux-x86-64.so.2 (0x000077a6ffc26000)

milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/software/mopac-ase/buildup_on_servers/wsl2/wsl2_desktopPC_BLTP/.dpkg -s mopac
Package: mopac
Status: install ok installed
Priority: optional
Section: science
Installed-Size: 9310
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Version: 22.0.6+dfsg-1
Depends: libblas3 | libblas.so.3, libc6 (>= 2.34), libgcc-s1 (>= 4.0), libgfortran5 (>= 10), libgomp1 (>= 4.2.1), liblapack3 | liblapack.so.3
Description: Molecular Orbital PACkage (MOPAC)
 MOPAC is a general-purpose semiempirical molecular orbital package for the
 study of solid state and molecular structures and reactions.
 .
 The semiempirical Hamiltonians MNDO, AM1, PM3, PM6, RM1, MNDO-d and PM7 are
 used in the electronic part of the calculation to obtain molecular orbitals,
 the heat of formation and its derivative with respect to molecular geometry.
 .
 Using these results MOPAC calculates the vibrational spectra, thermodynamic
 quantities, isotopic substitution effects and force constants for molecules,
 radicals, ions, and polymers. For studying chemical reactions, a transition
 state location routine and two transition state optimizing routines are
 available. For users to get the most out of the program, they must understand
 how the program works, how to enter data, how to interpret the results, and
 what to do when things go wrong.
Original-Maintainer: Debichem Team <debichem-devel@lists.alioth.debian.org>
Homepage: http://openmopac.net



