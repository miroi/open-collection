=======================
Au slab with Pt addatom
=======================

Experimental works:

Gotsis, H. J., I. Rivalta, Emilia Sicilia, and Nino Russo. "Pd, Rh, Ir and Pt adsorption on gold: A theoretical study of different surfaces." Chemical physics letters 442, no. 1-3 (2007): 105-109., doi: https://doi.org/10.1016/j.cplett.2007.05.064 (access https://sci-hub.ru/10.1021/jp5033228 )

Freire, Rafael LH, Adam Kiejna, and Juarez LF Da Silva. "Adsorption of Rh, Pd, Ir, and Pt on the Au (111) and Cu (111) surfaces: a density functional theory investigation." The Journal of Physical Chemistry C 118.33 (2014): 19051-19061., doi: https://doi.org/10.1021/jp5033228 (access https://www.researchgate.net/profile/Juarez-Da-Silva-2/publication/272128588_Adsorption_of_Rh_Pd_Ir_and_Pt_on_the_Au111_and_Cu111_Surfaces_A_Density_Functional_Theory_Investigation/links/6252bf34b0cee02d696130a1/Adsorption-of-Rh-Pd-Ir-and-Pt-on-the-Au111-and-Cu111-Surfaces-A-Density-Functional-Theory-Investigation.pdf)

correction : https://pubs.acs.org/doi/pdf/10.1021/acs.jpcc.5b08430?ref=article_openPDF

take Au(1 1 1) surface (Table 1)


WSL2 on own PC
---------------
python Pt_on_Au-slab_EMT.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 11.919323888148124
Pt single atom pot.energy = 5.85
      Step     Time          Energy          fmax
BFGS:    0 20:18:14       32.127305       50.281107
BFGS:    1 20:18:14       23.558299       35.343911
BFGS:    2 20:18:14       17.901652       21.653046
BFGS:    3 20:18:14       14.681555       11.138654
BFGS:    4 20:18:14       13.214539        4.070476
BFGS:    5 20:18:14       12.910904        1.348615
BFGS:    6 20:18:14       12.864584        0.305344
BFGS:    7 20:18:14       12.861773        0.033593
BFGS:    8 20:18:14       12.861738        0.000999
energy of atom plus surface system : 12.86173757059559
adsorption energy of Pt on Au fcc111 = -4.907586317552534


python Pt_on_Au-slab_relaxed_EMT.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 11.919323888148124
Pt single atom pot.energy = 5.85
      Step     Time          Energy          fmax
BFGS:    0 20:22:23       32.127305       50.281107
BFGS:    1 20:22:23       17.720941       18.915104
BFGS:    2 20:22:24       14.545823        9.485757
BFGS:    3 20:22:24       13.141869        3.559465
BFGS:    4 20:22:24       12.782951        1.103731
BFGS:    5 20:22:24       12.681206        0.564320
BFGS:    6 20:22:24       12.637930        0.682286
BFGS:    7 20:22:24       12.593923        0.684634
BFGS:    8 20:22:24       12.547228        0.602591
BFGS:    9 20:22:24       12.514263        0.232952
BFGS:   10 20:22:24       12.503288        0.207774
BFGS:   11 20:22:24       12.495994        0.370244
BFGS:   12 20:22:24       12.482113        0.486768
BFGS:   13 20:22:24       12.471751        0.369111
BFGS:   14 20:22:24       12.466105        0.159246
BFGS:   15 20:22:24       12.462508        0.147307
BFGS:   16 20:22:24       12.457988        0.172951
BFGS:   17 20:22:25       12.452723        0.188161
BFGS:   18 20:22:25       12.448562        0.115887
BFGS:   19 20:22:25       12.446760        0.041862
BFGS:   20 20:22:25       12.445971        0.067934
BFGS:   21 20:22:25       12.445074        0.103935
BFGS:   22 20:22:25       12.444130        0.090100
BFGS:   23 20:22:25       12.443576        0.035466
BFGS:   24 20:22:25       12.443336        0.027196
BFGS:   25 20:22:25       12.443127        0.037957
BFGS:   26 20:22:25       12.442768        0.065515
BFGS:   27 20:22:25       12.442261        0.073546
BFGS:   28 20:22:25       12.441812        0.046413
BFGS:   29 20:22:25       12.441591        0.015678
BFGS:   30 20:22:25       12.441484        0.016474
BFGS:   31 20:22:25       12.441361        0.033449
BFGS:   32 20:22:25       12.441184        0.041067
BFGS:   33 20:22:26       12.441020        0.029878
BFGS:   34 20:22:26       12.440919        0.012299
BFGS:   35 20:22:26       12.440849        0.011208
BFGS:   36 20:22:26       12.440761        0.021155
BFGS:   37 20:22:26       12.440650        0.026209
BFGS:   38 20:22:26       12.440566        0.016527
BFGS:   39 20:22:26       12.440530        0.004950
energy of atom plus surface system : 12.440530225023934
adsorption energy of Pt on Au fcc111 = -5.3287936631241895


display trajectory
~~~~~~~~~~~~~~~~~~
ase gui Pt_on_Au-slab.traj


