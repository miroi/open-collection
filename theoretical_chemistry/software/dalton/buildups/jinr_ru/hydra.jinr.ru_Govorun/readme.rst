==============
DALTON program
==============

web
---
https://daltonproject.readthedocs.io/en/latest/#

https://gitlab.com/dalton/dalton

download
--------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dalton/.git clone git@gitlab.com:dalton/dalton.git dalton_cloned

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dalton/dalton_cloned/.gsu
Submodule 'external/gen1int' (https://gitlab.com/bingao/gen1int.git) registered for path 'external/gen1int'
Submodule 'external/pelib' (https://gitlab.com/pe-software/pelib.git) registered for path 'external/pelib'
Cloning into '/lustre/projects/m/milias/work/software/dalton/dalton_cloned/external/gen1int'...
Cloning into '/lustre/projects/m/milias/work/software/dalton/dalton_cloned/external/pelib'...
Submodule path 'external/gen1int': checked out 'a9893e074d4f51357b0ea95b2af33a5ee601dd61'
Submodule path 'external/pelib': checked out '79f54ecf9c4268d3e98a8bdbdb1bccc0744cdaa6'


buildup with ctests
-------------------
sbatch hydra_slurm_dalton_buildup_ctest.01


passed ctests
~~~~~~~~~~~~~
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dalton/dalton_cloned/build_intelmpi2026_mkl_i8/test/.ls
aba_prop_file/           dft_open_b3lyp/         geoopt_numgrd/            prop_exci_aosopcc_direct/       prop_spinspin5/         rsp_g_rohfx/
dft_ac_grac/             dft_open_lr/            geoopt_preopt2/           prop_exci_aosoppa/              prop_spinspin_aosoppa/  rsp_g_rohfx_direct/
dft_ac_multpole/         dft_optimize/           geoopt_prop3_ex/          prop_exci_aosoppa_sing/         prop_spinspin_aotoppa/  rsp_g_rohfx_direcths/
dft_b3lyp_cart/          dft_pbe/                hf_cube/                  prop_exci_aosoppa_trip/         prop_vibana/            rsp_g_rohfx_hs/
dft_b3lyp_magsus_nosym/  dft_polar/              prop_alpha_aorpa/         prop_exci_aosoppa_trip_direct/  prop_vibg1/             rsp_hfc/
dft_b3lyp_molhes_nosym/  dft_properties_nosym/   prop_alpha_aosoppa/       prop_exci_aosoppcc/             prop_vibg2/             rsp_hyperpolar/
dft_b3lyp_nosym/         dft_properties_sym/     prop_alpha_aotoppa/       prop_exci_aotoppa/              prop_vibvcd/            rsp_hyperpolar_oit/
dft_b3lyp_sym/           dft_qr/                 prop_atmmom/              prop_expgrad/                   rsp_2ndharm/            rsp_lrso/
dft_blyp_nosym/          dft_qr_qlop/            prop_cirespon/            prop_lanczos_aosoppa/           rsp_3rdharm/            rsp_mnf/
dft_blyp_sym/            dft_rpbe/               prop_cpp_ecd/             prop_lresc_efg/                 rsp_3rdmom/             rsp_polar/
dft_camb3lyp/            dft_rspexci/            prop_ctocd/               prop_lresc_shielding/           rsp_abslrs/             rsp_quadrupole_polar/
dft_camb3lyp_magsus/     dft_spin_local/         prop_ecd/                 prop_newtramcscf/               rsp_absorp/             rsp_rohf_lr/
dft_camb3lyp_molgrad/    dft_stex/               prop_exci/                prop_newtrasoppa/               rsp_cpp_2ndhyperpolar/  rsp_soppa1excinosymm/
dft_cr_sym/              energy_corehole/        prop_exci_ao/             prop_newtrasoppacc/             rsp_cpp_mcd/            rsp_sosingci/
dft_disp_d2/             energy_fcktra/          prop_exci_aohrpa_sing/    prop_nolondon/                  rsp_cpp_mchd/           rsp_sosingorb/
dft_disp_d3/             energy_nosymm/          prop_exci_aohrpa_trip/    prop_nolondon_soppacc/          rsp_cpp_nscd/           rsp_sotripci/
dft_disp_d3bj/           energy_restart/         prop_exci_aohrpad/        prop_nucquad/                   rsp_cpp_veloci/         rsp_sotriporb/
dft_energy_sym/          energy_restart_scf/     prop_exci_aorpa/          prop_roa/                       rsp_dipvel_aosoppa/     rsp_zfs_mc2/
dft_hcth120/             energy_stex/            prop_exci_aorpa_direct/   prop_socvir/                    rsp_esr/                runtest_dalton.py
dft_hsrohf/              energy_symm/            prop_exci_aorpa_trip/     prop_soppa_vibavg_twobas/       rsp_esr2/               runtest_v1.py
dft_lb94/                energy_zmat/            prop_exci_aorpad/         prop_soppactocd/                rsp_exsm/               tddft_tda/
dft_lda_cart/            gen1int_fluorobenzene/  prop_exci_aorpad_trip/    prop_spinspin1/                 rsp_fullhfc/            walk_solvmag/
dft_lda_molhes_nosym/    gen1int_water/          prop_exci_aoshrpad/       prop_spinspin2/                 rsp_g_b3lypx/           walk_vibave/
dft_lda_nosym/           geoopt_freeze/          prop_exci_aosoc_trip/     prop_spinspin3/                 rsp_g_cas/
dft_lda_sym/             geoopt_mp2froz/         prop_exci_aosopcc2_sing/  prop_spinspin4/                 rsp_g_ldax/


