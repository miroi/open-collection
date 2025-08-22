============================
DFT-D3 on adsorption systems
============================


milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/simpledft-d3/wsl_pc_desktop/runs/tutorial_cases/adsorbate_on_surface/.~/work/software/simple_dft-d3/simple-dftd3/_build/app/s-dftd3 Pb_on_Se54_100.geopt_sozora_blyp-d3bj_tzp_sc_converged_geometry.xyz --bj PBE0

-----------------------------------
 s i m p l e   D F T - D 3  v1.2.1
-----------------------------------

Rational (Becke-Johnson) damping: PBE0-D3(BJ)
---------------------
  s6         1.0000
  s8         1.2177
  s9         0.0000
  a1         0.4145
  a2         4.8593
 alp        14.0000
--------------------

Dispersion energy:      -3.6342575019937E-01 Eh


milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/simpledft-d3/wsl_pc_desktop/runs/tutorial_cases/adsorbate_on_surface/.~/work/software/simple_dft-d3/simple-dftd3/_build/app/s-dftd3  Fl_on_Se54_100.geopt_sozora-collz_blyp-d3bj_tzp_sc_converged_geometry.xyz   --bj PBE0
-----------------------------------
 s i m p l e   D F T - D 3  v1.2.1
-----------------------------------

Rational (Becke-Johnson) damping: PBE0-D3(BJ)
---------------------
  s6         1.0000
  s8         1.2177
  s9         0.0000
  a1         0.4145
  a2         4.8593
 alp        14.0000
--------------------


Program received signal SIGSEGV: Segmentation fault - invalid memory reference.

Backtrace for this error:
#0  0x75b8c4623960 in ???
#1  0x75b8c4622ac5 in ???
#2  0x75b8c424251f in ???
#3  0x75b8c43a0d30 in ???
#4  0x75b8c4a4106b in __dftd3_model_MOD_new_d3_model
        at ../src/dftd3/model.f90:125
#5  0x591dc4de2ed6 in run_driver
        at ../app/driver.f90:203
#6  0x591dc4ddb6ad in dftd3_main
        at ../app/main.f90:29
#7  0x591dc4ddb6ad in main
        at ../app/main.f90:19




