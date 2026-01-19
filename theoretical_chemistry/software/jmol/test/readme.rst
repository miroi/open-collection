====================
Simple JMOl tutorial
====================


https://hpc-forge.cineca.it/files/CoursesDev/public/2017/Scientific_Visualization_for_Computational_Chemistry/Roma/jmol_printable.pdf


in 2D editor draw 2,4-ditmethylpentane, save as mol file

open it in JMol

console:
~~~~~~~~
This model is 2D. Its 3D structure has not been generated; use LOAD "" FILTER "2D" to optimize 3D.

$ LOAD "" FILTER "2D"
Minimized by Jmol using MMFF2D
This model is 2D. Its 3D structure was generated.


geometry optimization
~~~~~~~~~~~~~~~~~~~~~~

C:\Users\miroi\Desktop\git-projects\open-collection\theoretical_chemistry\software\jmol\test\alkane3Doptim.mol
 forcefield is MMFF
 Initial MMFF E =    128.113 kJ/mol criterion = 0.004187 max steps = 100
MMFF Step 10   E =  57.599285    dE = -16.639858 
MMFF Step 20   E =  45.757629    dE = -0.456446 
MMFF Step 30   E =  42.673302    dE = -0.178066 
MMFF Step 40   E =  40.887169    dE = -0.083395 
MMFF Step 50   E =  39.837780    dE = -0.034391 
MMFF Step 60   E =  39.339039    dE = -0.001583 
MMFF Step 62   E =  39.275150    dE = 0.000000 

    MMFF STEEPEST DESCENT HAS CONVERGED: E = 39.27515 kJ/mol after 62 steps

in console:  write  C:\Users\miroi\Desktop\git-projects\open-collection\theoretical_chemistry\software\jmol\test\alkane3Dopt.mol


