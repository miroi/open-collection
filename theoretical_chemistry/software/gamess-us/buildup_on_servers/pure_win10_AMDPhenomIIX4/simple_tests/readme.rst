===============================
GAMESS-US on MS WIndows10 tests
===============================

run in the GMS Windows command prompt from C:\Users\Public\gamess-64
needs rungms.gms file, copied from C:\Users\Public\gamess-64


dft-lead
--------
test from C:\Users\Public\gamess-64\tests\dft\parallel

C:\Users\Miro Ilias\Desktop\git-projects\open-collection\theoretical_chemistry\software\gamess-us\buildup_on_servers\pure_win10_AMDPhenomIIX4\simple_tests>C:\Users\Public\gamess-64\rungms.bat dft-lead.inp  2023.R1.intel 4 > dft-lead.logfile


nmr-nh3
-------
from C:\Users\Public\gamess-64\tests\spectra

only serial run is possible 

C:\Users\Miro Ilias\Desktop\git-projects\open-collection\theoretical_chemistry\software\gamess-us\buildup_on_servers\pure_win10_AMDPhenomIIX4\simple_tests>C:\Users\Public\gamess-64\rungms.bat nmr-nh3.inp  2023.R1.intel 1 > nmr-nh3.logfile


ch3br-dft_opt
-------------
input built using MacMolPlt

C:\Users\Miro Ilias\Desktop\git-projects\open-collection\theoretical_chemistry\software\gamess-us\buildup_on_servers\pure_win10_AMDPhenomIIX4\simple_tests>C:\Users\Public\gamess-64\rungms.bat ch3br-dft_opt.inp   2023.R1.intel 4 > ch3br-dft_opt.logfile