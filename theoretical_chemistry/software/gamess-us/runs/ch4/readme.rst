GAMESS-US on Victus NB
======================

add GAMESS-US location do system PATH

copy rungms.gms to the current directory

launch via Windows cmd shell, for the full logfile:

rungms.bat .\ch4_geopt_b3lyp_6-31Gdp.inp 2023.R1.intel 2 > .\ch4_geopt_b3lyp_6-31Gdp_2cpu.logfile

launch via Windows cmd shell, for the wxMacMolPlt reading:

rungms.bat .\ch4_geopt_b3lyp_6-31Gdp.inp 2023.R1.intel 2 .\ch4_geopt_b3lyp_6-31Gdp_2cpu.log

new run in MS Windows directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c:\Users\miroi\Documents\gamess-runs>C:\Users\Public\gamess-64\rungms.bat   ch4_geopt_b3lyp_6-31Gdp.inp     2023.R1.intel  4  ch4_geopt_b3lyp_6-31Gdp.logfile_np4
