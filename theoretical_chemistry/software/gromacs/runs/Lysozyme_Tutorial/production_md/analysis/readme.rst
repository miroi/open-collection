===================
Step Nine: Analysis
===================

http://www.mdtutorials.com/gmx/lysozyme/09_analysis.html

~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi trjconv -s ../md_0_10.tpr -f ../md_0_10.xtc -o md_0_10_noPBC.xtc -pbc mol -center

...output manually harvested into   md_0_10_noPBC.xtc_logfile

big file 
-rw-r--r-- 1 miroi miroi 9625232 Dec  4 22:10 md_0_10_noPBC.xtc

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/production_md/analysis/.~/work/software/gromacs/gromacs_cloned/build_gnu/bin/gmx_mpi rms  -s ../md_0_10.tpr -f md_0_10_noPBC.xtc -o rmsd.xvg -tu ns

... output manually harvested into  rmsd.xvg_logfile


