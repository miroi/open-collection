Gromacs on WSL
==============

installation
~~~~~~~~~~~~~
as package

milias@DESKTOP-7OTLCGO:~/.sudo apt install gromacs


check
~~~~~

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/gromacs/buildup_on_servers/wsl_pc_desktop/.gmx --help

Copyright (c) 2001-2019, The GROMACS development team at
Uppsala University, Stockholm University and
the Royal Institute of Technology, Sweden.
check out http://www.gromacs.org for more information.

GROMACS is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation; either version 2.1
of the License, or (at your option) any later version.

GROMACS:      gmx, version 2021.4-Ubuntu-2021.4-2
Executable:   /usr/bin/gmx
Data prefix:  /usr
Working dir:  /home/milias/work/git-projects/open-collection/theoretical_chemistry/software/gromacs/buildup_on_servers/wsl_pc_desktop
Command line:
  gmx --help

Program:     gmx, version 2021.4-Ubuntu-2021.4-2
Source file: src/gromacs/commandline/cmdlineparser.cpp (line 275)
Function:    void gmx::CommandLineParser::parse(int*, char**)

Error in user input:
Invalid command-line options
    Unknown command-line option --help

For more information and tips for troubleshooting, please check the GROMACS
website at http://www.gromacs.org/Documentation/Errors

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/gromacs/buildup_on_servers/wsl_pc_desktop/.ldd /usr/bin/gmx
        linux-vdso.so.1 (0x00007ffe944bc000)
        libgromacs.so.6 => /lib/x86_64-linux-gnu/libgromacs.so.6 (0x00007593da600000)
        libX11.so.6 => /lib/x86_64-linux-gnu/libX11.so.6 (0x00007593da4c0000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007593da200000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007593da119000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007593db49b000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007593d9e00000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007593da462000)
        libfftw3f.so.3 => /lib/x86_64-linux-gnu/libfftw3f.so.3 (0x00007593d9a00000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x00007593da073000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x00007593d9200000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007593da446000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007593da029000)
        libxcb.so.1 => /lib/x86_64-linux-gnu/libxcb.so.1 (0x00007593d9dd6000)
        /lib64/ld-linux-x86-64.so.2 (0x00007593db500000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007593d9dac000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007593d8e00000)
        libXau.so.6 => /lib/x86_64-linux-gnu/libXau.so.6 (0x00007593da43e000)
        libXdmcp.so.6 => /lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007593da436000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007593d9d64000)
        libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007593d9d4c000)
        libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0 (0x00007593d9d3f000)

