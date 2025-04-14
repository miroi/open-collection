================
QE buildup on NB
================


miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_openmpi/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON -DCMAKE_Fortran_COMPILER=mpif90  -DQE_FFTW_VENDOR=Intel_FFTW3 ..

make -j6

miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_openmpi/.ls bin/
ZG.x*              dvscf_q2r.x*       fs.x*             matdyn.x*              pmw.x*           pwcond.x*              ups.x*
abcoeff_to_eps.x*  dynmat.x*          graph.x*          memory_pw4gww.x*       postahc.x*       pwi2xsf.x*             virtual_v2.x*
all_currents.x*    ef.x*              gww.x*            merge_wann.x*          postw90.x*       q2qstar.x*             w90chk2chk.x*
alpha2f.x*         epa.x*             gww_fit.x*        molecularnexafs.x*     pp.x*            q2r.x*                 wannier2pw.x*
average.x*         epsilon.x*         head.x*           molecularpdos.x*       pp_disca.x*      scan_ibrav.x*          wannier90.x*
bands.x*           epsilon_Gaus.x*    hgh2qe.x*         neb.x*                 pp_spctrlfn.x*   simple.x*              wannier_ham.x*
bands_unfold.x*    epw.x*             hp.x*             nscf2supercond.x*      ppacf.x*         simple_bse.x*          wannier_plot.x*
bse_main.x*        ev.x*              ibrav2cell.x*     open_grid.x*           pprism.x*        simple_ip.x*           wfck2r.x*
casino2upf.x*      fd.x*              initial_state.x*  path_interpolation.x*  projwfc.x*       spectra_correction.x*  wfdd.x*
cell2ibrav.x*      fd_ef.x*           kcw.x*            pawplot.x*             pw.x*            sumpdos.x*             xspectra.x*
cp.x*              fd_ifc.x*          kcwpp_interp.x*   ph.x*                  pw2bgw.x*        turbo_davidson.x*
cppp.x*            fermi_int_0.x*     kcwpp_sh.x*       phcg.x*                pw2critic.x*     turbo_eels.x*
d3hess.x*          fermi_int_1.x*     kpoints.x*        plan_avg.x*            pw2gt.x*         turbo_lanczos.x*
disca.x*           fermi_proj.x*      lambda.x*         plotband.x*            pw2gw.x*         turbo_magnon.x*
dos.x*             fermi_velocity.x*  ld1.x*            plotproj.x*            pw2wannier90.x*  turbo_spectrum.x*
dos_sp.x*          fqha.x*            manycp.x*         plotrho.x*             pw4gww.x*        upfconv.x*


miroi@MIRO:~/work/software/quantum_espresso/q-e/build_gnu_openmpi/.ctest -j 6
99% tests passed, 1 tests failed out of 361
