===================
QE 7.3.1 on Govorun
===================

download
~~~~~~~~

https://www.quantum-espresso.org/download-page/

wget https://www.quantum-espresso.org/rdm-download/488/v7-3-1/328289162201bd6a785ae7620be3eb71/qe-7.3.1-ReleasePack.tar.gz


modules
~~~~~~~

milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/quantum-espresso/buildup_on_servers/jinr_ru/hydra_jinr_ru/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1               3) gcc/v11.2.0              5) LAPACK/v3.9.0
  2) BASE/1.0                 4) fftw/v3.3.10_gcc1120     6) openmpi/v4.1.1_gcc1120



installation
------------
milias@hydra.jinr.ru:~/work/software/quantum-espresso/openmpi/qe-7.3.1/.
./configure --enable-parallel --enable-openmp --with-scalapack --prefix=$PWD/bin
.
.
configure: success .. this takes gfortran 

milias@hydra.jinr.ru:~/work/software/quantum-espresso/qe-7.3.1/.less install/config.log

m -j4 all
ls -l bin/

milias@hydra.jinr.ru:~/work/software/quantum-espresso/openmpi/qe-7.3.1/.ls bin/
alpha2f.x@             fermi_velocity.x@  matdyn.x@              ppacf.x@         simple_ip.x@
average.x@             fqha.x@            molecularnexafs.x@     pprism.x@        simple.x@
band_interpolation.x@  fs.x@              molecularpdos.x@       pp.x@            spectra_correction.x@
bands.x@               gww_fit.x@         neb.x@                 projwfc.x@       sumpdos.x@
bse_main.x@            gww.x@             open_grid.x@           pw2bgw.x@        turbo_davidson.x@
cell2ibrav.x@          head.x@            oscdft_et.x@           pw2critic.x@     turbo_eels.x@
cppp.x@                hp.x@              oscdft_pp.x@           pw2gw.x@         turbo_lanczos.x@
cp.x@                  ibrav2cell.x@      path_interpolation.x@  pw2wannier90.x@  turbo_magnon.x@
d3hess.x@              initial_state.x@   phcg.x@                pw4gww.x@        turbo_spectrum.x@
dist.x@                kcwpp_interp.x@    ph.x@                  pwcond.x@        wannier90.x@
dos.x@                 kcwpp_sh.x@        plan_avg.x@            pwi2xsf.x@       wannier_ham.x@
dvscf_q2r.x@           kcw.x@             plotband.x@            pw.x@            wannier_plot.x@
dynmat.x@              kpoints.x@         plotproj.x@            q2qstar.x@       wfck2r.x@
epa.x@                 lambda.x@          plotrho.x@             q2r.x@           wfdd.x@
epsilon.x@             ld1.x@             pmw.x@                 rism1d.x@        xspectra.x@
ev.x@                  manycp.x@          postahc.x@             scan_ibrav.x@
fermi_proj.x@          manypw.x@          postw90.x@             simple_bse.x@
milias@hydra.jinr.ru:~/work/software/quantum-espresso/openmpi/qe-7.3.1/.



