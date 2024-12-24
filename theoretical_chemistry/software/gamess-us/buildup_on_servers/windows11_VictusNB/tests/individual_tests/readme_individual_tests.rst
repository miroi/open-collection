==========================
GAMESS-US individual tests
==========================

running only in MS Windows  CMD prompt, and in MS Windows directories ! (not in WSL)

clean files
~~~~~~~~~~~
C:\Users\miroi\Documents\gamess-runs>C:\Users\Public\gamess-64\clean-runall-files.bat

Finish removing exam*log, scratch\exam*.*, and restart\exam*.* files

Press any key to continue . . .

C:\Users\miroi\Documents\gamess-runs>

running individual tests
~~~~~~~~~~~~~~~~~~~~~~~~

from Windows   C:\Users\Public\gamess-64\Windows-Command-Prompt !

C:\Users\miroi\Documents\gamess-runs>C:\Users\Public\gamess-64\rungms.bat    C:\Users\Public\gamess-64\tests\travis-ci\exam05.inp  2023.R1.intel  1    exam05.log

C:\Users\miroi\Documents\gamess-runs>C:\Users\Public\gamess-64\rungms.bat    C:\Users\Public\gamess-64\tests\travis-ci\parallel\exam01.inp  2023.R1.intel  1  exam01.log



