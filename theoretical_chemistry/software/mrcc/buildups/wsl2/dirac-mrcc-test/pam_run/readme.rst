=====================
Simple DIRAC-MRCC run
=====================

based on https://mrcc.hu/MRCC/manual/html/single/manual_sp.xhtml#S5.SS3 :

/home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/pam --get="MRCONEE MDCINT" --inp=ccsd.inp --mol=CO_C2v.mol

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/./home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64/dirac_mointegral_export.x

  Initialized reading from MRCONEE (version DIRAC20 and later)
  Core energy:   -80.273643033914084
  Breit interaction:  F
  Group type (1:real, 2:complex, 4:quaternion) :                    1
  Initialized reading from MDCINT
  MDCINT created:  20251020   12:48:22


new
---

source  /opt/intel/oneapi/2025.3/oneapi-vars.sh

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/.~/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/pam  --get="MRCONEE MDCINT" --inp=ccsd.inp --mol=CO_C2v.mol

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/.~/work/software/dirac/trunk_cloned/build_intelmpi_mkl_ilp64/dirac_mointegral_export.x

  Initialized reading from MRCONEE (version DIRAC20 and later)
  Core energy:   -80.2736430339140
  Breit interaction:  F
  Group type (1:real, 2:complex, 4:quaternion) :                     1
  Initialized reading from MDCINT
  MDCINT created:  20260606   21:19:08


better
------
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/.export PATH=/home/miroi/work/software/mrcc:$PATH
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/.dirac_mointegral_export
  Initialized reading from MRCONEE
  Core energy:   -80.2736430339140
  Breit interaction:  F
  Initialized reading from MDCINT
  MDCINT created:  20260606   21:19:08
  Writing sample MINP CCSD input file for mrcc...
  MINP file ready: can be modified by user
  Writing fort.55 interface file for mrcc...
  fort.55 file ready


MINP created !!!

goldstone run
~~~~~~~~~~~~~
goldstone
forrtl: No such file or directory
forrtl: severe (29): file not found, unit 75, file /home/miroi/work/projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/KEYWD

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mrcc/buildups/wsl2/dirac-mrcc-test/pam_run/.dmrcc > dmrcc.logfile

Total CCSD energy [au]:                     -122.356754196691

@ Total CCSD energy :                       -113.117918449391453
