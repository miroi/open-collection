milias@lxir127.gsi.de:/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/.make run-tests-parallel
env QE_USE_MPI=1 /data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/..//test-suite/testcode/bin/testcode.py --verbose --category=pw_all
Using executable: /data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/..//test-suite/run-pw.sh.
Test id: 060720.
Benchmark: git.

pw_atom - atom.in: Passed.

pw_atom - atom-lsda.in: Passed.

pw_atom - atom-occ1.in: Passed.

pw_atom - atom-occ2.in: Passed.

pw_atom - atom-pbe.in: Passed.

pw_atom - atom-sigmapbe.in: Passed.

pw_b3lyp - b3lyp-O.in: Passed.

pw_b3lyp - b3lyp-h2o.in: Passed.

pw_b3lyp - x3lyp-O.in: Passed.

pw_b3lyp - x3lyp-h2o.in: Passed.

pw_berry - berry.in: Passed.

pw_berry - berry-1.in: Passed.

pw_berry - berry-2.in: Passed.

pw_cluster - cluster1.in: Passed.

pw_cluster - cluster2.in: Passed.

pw_cluster - cluster3.in: Passed.

pw_cluster - cluster4.in: Passed.

pw_dft - dft1.in: Passed.

pw_dft - dft10.in: Passed.

pw_dft - dft11.in: Passed.

pw_dft - dft2.in: Passed.

pw_dft - dft3.in: Passed.

pw_dft - dft4.in: Passed.

pw_dft - dft5.in: Passed.

pw_dft - dft6.in: Passed.

pw_dft - dft7.in: Passed.

pw_dft - dft8.in: Passed.

pw_dft - dft9.in: Passed.

pw_dipole - dipole.in: Passed.

pw_electric - electric0.in: Passed.

pw_electric - electric1.in: Passed.

pw_electric - electric2.in: Passed.

pw_eval - eval_infix-2.in: Passed.

pw_eval - eval_infix.in: Passed.

pw_gau-pbe - gau-pbe-si111.in: Passed.

pw_gau-pbe - gau-pbe-si222.in: Passed.

pw_gau-pbe - gau-pbe-si444.in: Passed.

pw_hse - hse-si111.in: Passed.

pw_hse - hse-si222.in: Passed.

.
.

All done. ERROR: only 15 out of 32 tests passed (57 skipped).
Failed tests in:
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_base/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_metal/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob_ibte/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob_ibte_sym/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob_polar/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_pl/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_polar/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_scdm/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_soc/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_super/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_trev/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_trev_uspp/
Skipped tests in:
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_base/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob_ibte/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob_ibte_sym/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_mob_polar/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_pl/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_polar/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_scdm/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_super/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_trev/
	/data.local1/milias/software/quantum-epresso/q-e-qe-6.5/test-suite/epw_trev_uspp/
Makefile:75: recipe for target 'run-tests-epw-parallel' failed
make: *** [run-tests-epw-parallel] Error 1





