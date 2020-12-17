
LiCl(+) with NWChem
===================

 ROHF, doublet

 Does not work in DFT :
# see https://nwchemgit.github.io/Density-Functional-Theory-for-Molecules.html#restricted
  fon partial 2 electrons 3 filled 1


see https://groups.google.com/g/nwchem-forum/c/Hj_jLUMKjrk/m/5RGj44pZAAAJ

"RODFT does not have the same functionality as the default Unrestricted DFT code. FON is one of them.
The code should have stopped with a more meaningful error message"

https://github.com/nwchemgit/nwchem/issues/283


Effectivity of parallel runs
----------------------------
  bash_run-labs.01 #CPU

  #CPU    wall time
   1        
   2       
   4      
   6     
  10
  12
