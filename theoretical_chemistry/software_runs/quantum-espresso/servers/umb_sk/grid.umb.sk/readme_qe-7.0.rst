QE-7.0
======

module load mpi/openmpi3-x86_64

see https://gitlab.com/QEF/q-e/-/wikis/Developers/CMake-build-system


milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi/.cmake -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90 ..
.
.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi

milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi/.m -j4
.
.
milias@login.grid.umb.sk:~/Work/qch/software/quantum-espresso/qe-7.0/build_openmpi/.ls bin/
ZG.x*              cppp.x*          ev.x*              gww.x*            matdyn.x*              plotband.x*     pw.x*            scan_ibrav.x*          upfconv.x*
abcoeff_to_eps.x*  disca.x*         fd.x*              gww_fit.x*        memory_pw4gww.x*       plotproj.x*     pw2bgw.x*        simple.x*              virtual_v2.x*
all_currents.x*    dos.x*           fd_ef.x*           head.x*           molecularnexafs.x*     plotrho.x*      pw2critic.x*     simple_bse.x*          w90chk2chk.x*
alpha2f.x*         dos_sp.x*        fd_ifc.x*          hgh2qe.x*         molecularpdos.x*       pmw.x*          pw2gt.x*         simple_ip.x*           wannier_ham.x*
average.x*         dvscf_q2r.x*     fermi_int_0.x*     hp.x*             neb.x*                 postahc.x*      pw2gw.x*         spectra_correction.x*  wannier_plot.x*
bands.x*           dynmat.x*        fermi_int_1.x*     ibrav2cell.x*     open_grid.x*           postw90.x*      pw2wannier90.x*  sumpdos.x*             wannier_prog.x*
bands_unfold.x*    ef.x*            fermi_proj.x*      initial_state.x*  path_interpolation.x*  pp.x*           pw4gww.x*        turbo_davidson.x*      wfck2r.x*
bse_main.x*        epa.x*           fermi_velocity.x*  kpoints.x*        pawplot.x*             pp_disca.x*     pwcond.x*        turbo_eels.x*          wfdd.x*
casino2upf.x*      epsilon.x*       fqha.x*            lambda.x*         ph.x*                  pp_spctrlfn.x*  pwi2xsf.x*       turbo_lanczos.x*       xspectra.x*
cell2ibrav.x*      epsilon_Gaus.x*  fs.x*              ld1.x*            phcg.x*                ppacf.x*        q2qstar.x*       turbo_magnons.x*
cp.x*              epw.x*           graph.x*           manycp.x*         plan_avg.x*            projwfc.x*      q2r.x*           turbo_spectrum.x*



