========
TsOO@Q-G
========

milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/theoretical_chemistry/software/wien2k/runs/TsOO_on_quartz_G/TsOOQg/.nohup lxir127_bash_wien2k_gnu_openmpi_openblas.01 & 

milias@lxir127.gsi.de:/data.local1/milias/scratch/wien2k.2f55a.7709/TsOOQg/.grep 'Matrix size' *
TsOOQg.output1_1: Matrix size        84052

http://zeus.theochem.tuwien.ac.at/pipermail/wien/2023-June/033271.html
b) You have 4x4x5 k-points, which is way too many. The default (23.2) uses
2x2x2 and I would suggest just using 1 without shift at first. This will be
40 times faster.
