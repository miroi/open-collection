Vitamin C with GAMESS-US
=========================

https://pubchem.ncbi.nlm.nih.gov/compound/54670067

download sdf into \\wsl.localhost\Ubuntu\home\miroi\work\projects\open-collection\theoretical_chemistry\software\gamess-us\runs\vitamin_c

load Conformer3D_COMPOUND_CID_54670067.sdf into MacMolPlt

set computation params like DFT, STO-3G, single energy point/optimization 

run in Gamess command window
----------------------------

single step
~~~~~~~~~~~
C:\Users\Public\gamess-64\rungms.bat  vit_c.b3lyp_sto3g.inp   2023.R1.intel  4 > vit_c.b3lyp_sto3g.n4_out


geometry optimization
~~~~~~~~~~~~~~~~~~~~~
geometry optimization did not converge for default N=20 geometry steps, but it is sufficient ...
todo: less printout, add more steps

C:\Users\Public\gamess-64\rungms.bat   vit_c.geopt_b3lyp_6-31.inp   2023.R1.intel  4 >  vit_c.geopt_b3lyp_6-31.n4_out


