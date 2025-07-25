Example of DFTD4
=================

https://dftd4.readthedocs.io/en/latest/reference/fortran.html#complete-example


WSL-Notebook
~~~~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/test_fortran_api/complete_example/.gfortran -I /home/miroi/work/software/dftd4/dftd4_cloned/_build/include -I /home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mctc-lib-build/include  demo.f90 -L/home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mctc-lib-build  -lmctc-lib
/usr/bin/ld: /tmp/ccv3vRoE.o: warning: relocation against `__dftd4_model_type_MOD___vtab_dftd4_model_type_Dispersion_model' in read-only section `.text'
 /usr/bin/ld: /tmp/ccv3vRoE.o: in function `calc_dftd4.0':
demo.f90:(.text+0x13e): undefined reference to `__dftd4_model_type_MOD___vtab_dftd4_model_type_Dispersion_model'
/usr/bin/ld: demo.f90:(.text+0x151): undefined reference to `__dftd4_damping_MOD___vtab_dftd4_damping_Damping_param'
/usr/bin/ld: demo.f90:(.text+0x1e6): undefined reference to `__dftd4_damping_MOD___vtab_dftd4_damping_Damping_param'
/usr/bin/ld: demo.f90:(.text+0x20b): undefined reference to `__dftd4_param_MOD_get_rational_damping_name'
/usr/bin/ld: demo.f90:(.text+0x464): undefined reference to `__dftd4_model_type_MOD___vtab_dftd4_model_type_Dispersion_model'
/usr/bin/ld: demo.f90:(.text+0x4be): undefined reference to `__dftd4_model_MOD_new_dispersion_model'
/usr/bin/ld: demo.f90:(.text+0x70f): undefined reference to `__dftd4_disp_MOD_get_dispersion'
/usr/bin/ld: warning: creating DT_TEXTREL in a PIE
 collect2: error: ld returned 1 exit status


 miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/test_fortran_api/complete_example/.gfortran  -I /home/miroi/work/software/dftd4/dftd4_cloned/_build/include -I /home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mctc-lib-build/include  demo.f90 -L/home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mctc-lib-build -L/home/miroi/work/software/dftd4/dftd4_cloned/_build  -L/home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/multicharge-build -L/home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mstore-build   -ldftd4  -lmctc-lib  -lmstore -lmulticharge


only compilation
~~~~~~~~~~~~~~~~

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/dft-dispersion-corr/dft-d4/runs/test_fortran_api/complete_example/.gfortran -c demo.f90 -I/home/miroi/work/software/dftd4/dftd4_cloned/_build/_deps/mctc-lib-build/include -I/home/miroi/work/software/dftd4/dftd4_cloned/_build/include

