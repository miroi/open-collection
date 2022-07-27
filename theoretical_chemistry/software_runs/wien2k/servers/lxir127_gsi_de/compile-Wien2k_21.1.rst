Wien2k on @lxir127.gsi.de
=========================

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_21.1/.tar xvf WIEN2k_21.1.tar 

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_21.1/.gunzip *

milias@lxir127.gsi.de:/data.local1/milias/software/wien2k/WIEN2k_21.1/../expand_lapw 

.
.
case.win   linked to   template.win
python found at /usr/bin/python.

WIEN is now expanded. The shell-script commands were copied and links created.
To configure your Fortran-executables run:

./siteconfig_lapw

source /cvmfs/vae.gsi.de/debian10/spack-0.17/vaesoft/spack/share/spack/setup-env.sh
spack load intel-parallel-studio@professional.2020.1

.
.
serial compilation done


Please check in SRC_*/compile.msg if any serious errors were encountered 
   during compilation. In case of errors fix the compiler options, check the 
   system configuation, and rerun ./siteconfig_lapw.

   If no errors occured, your WIEN2k site is now configured.
   
   The options you specified during this procedure (compilers, flags, paths)
   are saved in files in your WIENROOT directory (WIEN2k_MPI, WIEN2k_OPTIONS,
   WIEN2k_SYSTEM, and WIEN2k_COMPILER). You can modify them there directly, 
   however, in that case, you have to use siteconfig again to accordingly 
   adapt the Makefiles (just enter the corresponding menu and save changes).

   To setup the environment for WIEN users, each user should execute: 
   /data.local1/milias/software/wien2k/WIEN2k_21.1/userconfig_lapw !


   We wish you GOOD LUCK with your calculations.

