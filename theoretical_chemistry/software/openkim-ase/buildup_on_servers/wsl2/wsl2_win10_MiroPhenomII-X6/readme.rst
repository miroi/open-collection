=======
kim api
=======

download
---------
miroi@MiroPhenomII-X6:~/software/kim-api/.wget https://s3.openkim.org/kim-api/kim-api-2.4.1.txz
miroi@MiroPhenomII-X6:~/software/kim-api/.wget  https://s3.openkim.org/kim-api/kim-api-2.4.1.txz.asc

miroi@MiroPhenomII-X6:~/software/kim-api/.wget https://z.umn.edu/relliott_asc


miroi@MiroPhenomII-X6:~/software/kim-api/.gpg --import relliott_asc
gpg: /home/miroi/.gnupg/trustdb.gpg: trustdb created
gpg: key 576D4997C4D51D92: public key "Ryan S. Elliott <relliott@umn.edu>" imported
gpg: Total number processed: 1
gpg:               imported: 1


miroi@MiroPhenomII-X6:~/software/kim-api/.gpg --verify kim-api-2.4.1.txz.asc kim-api-2.4.1.txz
gpg: Signature made Tue Apr 15 21:28:42 2025 CEST
gpg:                using RSA key DECADD04C80028FCA210F824576D4997C4D51D92
gpg:                issuer "relliott@umn.edu"
gpg: Good signature from "Ryan S. Elliott <relliott@umn.edu>" [unknown]
gpg: WARNING: The key's User ID is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: DECA DD04 C800 28FC A210  F824 576D 4997 C4D5 1D92
miroi@MiroPhenomII-X6:~/software/kim-api/.

miroi@MiroPhenomII-X6:~/software/kim-api/.tar Jxvf kim-api-2.4.1.txz

installation
------------

see https://openkim.org/doc/usage/obtaining-models/#source_install

miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/.mkdir build
miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/.cd build/
miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/build/.cmake .. -DCMAKE_BUILD_TYPE=Release
-- KIM-API Build Type: Release
-- The CXX compiler identification is GNU 13.3.0
-- The C compiler identification is GNU 13.3.0
-- The Fortran compiler identification is GNU 13.3.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /usr/bin/gfortran - skipped
-- Found Git: (/usr/bin/git)
-- Found bash-completion: (/usr/share/bash-completion/completions)
-- Performing Test cxx_support_for__Wall
-- Performing Test cxx_support_for__Wall - Success
-- Performing Test cxx_support_for__Wextra
-- Performing Test cxx_support_for__Wextra - Success
-- Performing Test cxx_support_for__pedantic
-- Performing Test cxx_support_for__pedantic - Success
-- Performing Test c_support_for__Wall
-- Performing Test c_support_for__Wall - Success
-- Performing Test c_support_for__Wextra
-- Performing Test c_support_for__Wextra - Success
-- Performing Test c_support_for__pedantic
-- Performing Test c_support_for__pedantic - Success
-- Performing Test fortran_support_for__std_f2003
-- Performing Test fortran_support_for__std_f2003 - Success
-- Performing Test fortran_support_for__Wall
-- Performing Test fortran_support_for__Wall - Success
-- Performing Test fortran_support_for__Wextra
-- Performing Test fortran_support_for__Wextra - Success
-- Performing Test fortran_support_for__Wimplicit_interface
-- Performing Test fortran_support_for__Wimplicit_interface - Success
-- Performing Test fortran_support_for__pedantic
-- Performing Test fortran_support_for__pedantic - Success
--

###
#
#  kim-api configuration:
#
#    === C++ compile values =================
#    CMAKE_CXX_COMPILER: (GNU, 13.3.0, std=98)
#       /usr/bin/c++
#
#    === C compile values ===================
#    CMAKE_C_COMPILER: (GNU, 13.3.0, std=90)
#       /usr/bin/cc
#
#    === Fortran compile values =============
#    CMAKE_Fortran_COMPILER: (GNU, 13.3.0)
#       /usr/bin/gfortran
#
#    === Build type value ===================
#    CMAKE_BUILD_TYPE:                       Release
#
#    === Install directory values ===========
#    CMAKE_INSTALL_PREFIX:
#       /usr/local
#
#    CMAKE_INSTALL_INCLUDEDIR:               include
#    CMAKE_INSTALL_BINDIR:                   bin
#    CMAKE_INSTALL_LIBDIR:                   lib
#    CMAKE_INSTALL_LIBEXECDIR:               libexec
#
#    === kim-api option values ==============
#    KIM_API_PROJECT_NAME:                   kim-api
#    KIM_API_CONFIGURATION_TIMESTAMP:        2026-01-02-19-24-56
#
#    PROJECT_VERSION:                        2.4.1
#    PROJECT_VERSION_STRING:                 2.4.1+GNU.GNU.GNU
#    KIM_API_UID:                            2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56
#
#    KIM_API_LOG_MAXIMUM_LEVEL:              INFORMATION
#
#    KIM_API_BASE64_BUFFERSIZE:              16777216
#
#    KIM_API_BUILD_EXAMPLES:                 ON
#    KIM_API_ENABLE_SANITIZE:                OFF
#    KIM_API_ENABLE_COVERAGE:                OFF
#
#    KIM_API_USER_CONFIGURATION_FILE:
#       .kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/config
#
###

-- The above configuration information can also be found in:
--     /home/miroi/software/kim-api/kim-api-2.4.1/build/kim-api-configuration-summary.log
-- A more detailed configuration listing can be found in:
--     /home/miroi/software/kim-api/kim-api-2.4.1/build/kim-api-configuration-detailed.log
--
-- Configuring done (7.1s)
-- Generating done (0.1s)
-- Build files have been written to: /home/miroi/software/kim-api/kim-api-2.4.1/build
miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/build/.make -j4
.
.
[100%] Linking CXX shared module libkim-api-model-driver.so
[100%] Built target LennardJones612__MD_414112407348_003

miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/build/.ctest -j4
Test project /home/miroi/software/kim-api/kim-api-2.4.1/build
      Start  1: shared_library_test_ex_model_driver_P_LJ
      Start  2: shared_library_test_ex_model_driver_P_Morse
      Start  3: shared_library_test_LennardJones612__MD_414112407348_003
      Start  4: shared_library_test_ex_model_Ar_P_LJ
 1/46 Test  #1: shared_library_test_ex_model_driver_P_LJ ...................................................   Passed    0.01 sec
      Start  5: shared_library_test_ex_model_Ar_P_MLJ_Fortran
 2/46 Test  #2: shared_library_test_ex_model_driver_P_Morse ................................................   Passed    0.01 sec
      Start  6: shared_library_test_ex_model_Ar_P_Morse
 3/46 Test  #3: shared_library_test_LennardJones612__MD_414112407348_003 ...................................   Passed    0.01 sec
      Start  7: shared_library_test_ex_model_Ar_P_Morse_07C
 4/46 Test  #4: shared_library_test_ex_model_Ar_P_LJ .......................................................   Passed    0.02 sec
      Start  8: shared_library_test_ex_model_Ar_P_Morse_07C_w_Extensions
 5/46 Test  #5: shared_library_test_ex_model_Ar_P_MLJ_Fortran ..............................................   Passed    0.01 sec
      Start  9: shared_library_test_ex_model_Ar_P_Morse_MultiCutoff
 6/46 Test  #6: shared_library_test_ex_model_Ar_P_Morse ....................................................   Passed    0.02 sec
      Start 10: shared_library_test_ex_model_Ar_SLJ_MultiCutoff
 7/46 Test  #7: shared_library_test_ex_model_Ar_P_Morse_07C ................................................   Passed    0.02 sec
      Start 11: shared_library_test_LennardJones612_UniversalShifted__MO_959249795837_003
 8/46 Test  #8: shared_library_test_ex_model_Ar_P_Morse_07C_w_Extensions ...................................   Passed    0.01 sec
      Start 12: shared_library_test_LennardJones_Ar
 9/46 Test  #9: shared_library_test_ex_model_Ar_P_Morse_MultiCutoff ........................................   Passed    0.01 sec
      Start 13: shared_library_test_Sim_LAMMPS_LJcut_AkersonElliott_Alchemy_PbAu
10/46 Test #10: shared_library_test_ex_model_Ar_SLJ_MultiCutoff ............................................   Passed    0.01 sec
      Start 14: Run_collections-example
11/46 Test #11: shared_library_test_LennardJones612_UniversalShifted__MO_959249795837_003 ..................   Passed    0.01 sec
      Start 15: Run_collections-example-c
12/46 Test #12: shared_library_test_LennardJones_Ar ........................................................   Passed    0.01 sec
      Start 16: Run_collections-example-fortran
13/46 Test #13: shared_library_test_Sim_LAMMPS_LJcut_AkersonElliott_Alchemy_PbAu ...........................   Passed    0.01 sec
      Start 17: Run_ex_test_Ar_fcc_cluster_LennardJones612_UniversalShifted__MO_959249795837_003
14/46 Test #14: Run_collections-example ....................................................................   Passed    0.02 sec
      Start 18: Run_ex_test_Ar_fcc_cluster_LennardJones_Ar
15/46 Test #15: Run_collections-example-c ..................................................................   Passed    0.02 sec
      Start 19: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_LJ
16/46 Test #16: Run_collections-example-fortran ............................................................   Passed    0.02 sec
      Start 20: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_MLJ_Fortran
17/46 Test #18: Run_ex_test_Ar_fcc_cluster_LennardJones_Ar .................................................   Passed    0.01 sec
      Start 21: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse
18/46 Test #17: Run_ex_test_Ar_fcc_cluster_LennardJones612_UniversalShifted__MO_959249795837_003 ...........   Passed    0.02 sec
      Start 22: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse_07C
19/46 Test #19: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_LJ ................................................   Passed    0.02 sec
      Start 23: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse_07C_w_Extensions
20/46 Test #20: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_MLJ_Fortran .......................................   Passed    0.02 sec
      Start 24: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse_MultiCutoff
21/46 Test #21: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse .............................................   Passed    0.02 sec
      Start 25: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_SLJ_MultiCutoff
22/46 Test #22: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse_07C .........................................   Passed    0.02 sec
      Start 26: Run_ex_test_Ar_fcc_cluster_cpp_LennardJones612_UniversalShifted__MO_959249795837_003
23/46 Test #23: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse_07C_w_Extensions ............................   Passed    0.02 sec
      Start 27: Run_ex_test_Ar_fcc_cluster_cpp_LennardJones_Ar
24/46 Test #24: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_P_Morse_MultiCutoff .................................   Passed    0.01 sec
      Start 28: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_LJ
25/46 Test #25: Run_ex_test_Ar_fcc_cluster_ex_model_Ar_SLJ_MultiCutoff .....................................   Passed    0.01 sec
      Start 29: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_MLJ_Fortran
26/46 Test #27: Run_ex_test_Ar_fcc_cluster_cpp_LennardJones_Ar .............................................   Passed    0.01 sec
      Start 30: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse
27/46 Test #29: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_MLJ_Fortran ...................................   Passed    0.01 sec
      Start 31: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse_07C
28/46 Test #28: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_LJ ............................................   Passed    0.02 sec
      Start 32: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse_07C_w_Extensions
29/46 Test #26: Run_ex_test_Ar_fcc_cluster_cpp_LennardJones612_UniversalShifted__MO_959249795837_003 .......   Passed    0.03 sec
      Start 33: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse_MultiCutoff
30/46 Test #30: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse .........................................   Passed    0.02 sec
      Start 34: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_SLJ_MultiCutoff
31/46 Test #31: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse_07C .....................................   Passed    0.01 sec
      Start 35: Run_ex_test_Ar_fcc_cluster_fortran_LennardJones612_UniversalShifted__MO_959249795837_003
32/46 Test #33: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse_MultiCutoff .............................   Passed    0.01 sec
      Start 36: Run_ex_test_Ar_fcc_cluster_fortran_LennardJones_Ar
33/46 Test #34: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_SLJ_MultiCutoff .................................   Passed    0.01 sec
      Start 37: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_LJ
34/46 Test #32: Run_ex_test_Ar_fcc_cluster_cpp_ex_model_Ar_P_Morse_07C_w_Extensions ........................   Passed    0.02 sec
      Start 38: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_MLJ_Fortran
35/46 Test #36: Run_ex_test_Ar_fcc_cluster_fortran_LennardJones_Ar .........................................   Passed    0.01 sec
      Start 39: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse
36/46 Test #35: Run_ex_test_Ar_fcc_cluster_fortran_LennardJones612_UniversalShifted__MO_959249795837_003 ...   Passed    0.02 sec
      Start 40: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse_07C
37/46 Test #37: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_LJ ........................................   Passed    0.02 sec
      Start 41: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse_07C_w_Extensions
38/46 Test #39: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse .....................................   Passed    0.02 sec
      Start 42: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse_MultiCutoff
39/46 Test #38: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_MLJ_Fortran ...............................   Passed    0.03 sec
      Start 43: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_SLJ_MultiCutoff
40/46 Test #40: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse_07C .................................   Passed    0.02 sec
      Start 44: Run_simulator-model-example
41/46 Test #41: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse_07C_w_Extensions ....................   Passed    0.02 sec
      Start 45: Run_simulator-model-example-c
42/46 Test #42: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_P_Morse_MultiCutoff .........................   Passed    0.01 sec
      Start 46: Run_simulator-model-example-fortran
43/46 Test #43: Run_ex_test_Ar_fcc_cluster_fortran_ex_model_Ar_SLJ_MultiCutoff .............................   Passed    0.01 sec
44/46 Test #44: Run_simulator-model-example ................................................................   Passed    0.02 sec
45/46 Test #45: Run_simulator-model-example-c ..............................................................   Passed    0.02 sec
46/46 Test #46: Run_simulator-model-example-fortran ........................................................   Passed    0.01 sec

100% tests passed, 0 tests failed out of 46

Total Test time (real) =   0.22 sec

miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/build/.sudo make install
[sudo] password for miroi:
[ 52%] Built target kim-api
[ 53%] Built target portable-model-info
[ 54%] Built target simulator-model
[ 55%] Built target collections-info
[ 56%] Built target base64-encode
[ 57%] Built target shared-library-test
[ 59%] Built target ex_model_driver_P_LJ
[ 61%] Built target ex_model_driver_P_Morse
[ 64%] Built target LennardJones612__MD_414112407348_003
[ 67%] Built target ex_model_Ar_P_LJ
[ 69%] Built target ex_model_Ar_P_MLJ_Fortran
[ 72%] Built target ex_model_Ar_P_Morse
[ 74%] Built target ex_model_Ar_P_Morse_07C
[ 76%] Built target ex_model_Ar_P_Morse_07C_w_Extensions
[ 79%] Built target ex_model_Ar_P_Morse_MultiCutoff
[ 81%] Built target ex_model_Ar_SLJ_MultiCutoff
[ 83%] Built target LennardJones612_UniversalShifted__MO_959249795837_003
[ 85%] Built target LennardJones_Ar
[ 90%] Built target Sim_LAMMPS_LJcut_AkersonElliott_Alchemy_PbAu
[ 91%] Built target collections-example
[ 92%] Built target collections-example-c
[ 93%] Built target collections-example-fortran
[ 94%] Built target ex_test_Ar_fcc_cluster
[ 95%] Built target ex_test_Ar_fcc_cluster_cpp
[ 96%] Built target ex_test_Ar_fcc_cluster_fortran
[ 97%] Built target simulator-model-example
[ 98%] Built target simulator-model-example-c
[ 99%] Built target simulator-model-example-fortran
[100%] Built target utility_forces_numer_deriv
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/lib/libkim-api.so.2.4.1
-- Installing: /usr/local/lib/libkim-api.so.2
-- Installing: /usr/local/lib/libkim-api.so
-- Installing: /usr/local/share/doc/kim-api/README.md
-- Installing: /usr/local/share/doc/kim-api/NEWS
-- Installing: /usr/local/share/doc/kim-api/LICENSE.LGPL
-- Installing: /usr/local/include/kim-api/KIM_ChargeUnit.hpp
-- Installing: /usr/local/include/kim-api/KIM_Collection.hpp
-- Installing: /usr/local/include/kim-api/KIM_CollectionItemType.hpp
-- Installing: /usr/local/include/kim-api/KIM_Collections.hpp
-- Installing: /usr/local/include/kim-api/KIM_ComputeArgumentName.hpp
-- Installing: /usr/local/include/kim-api/KIM_ComputeArguments.hpp
-- Installing: /usr/local/include/kim-api/KIM_ComputeCallbackName.hpp
-- Installing: /usr/local/include/kim-api/KIM_DataType.hpp
-- Installing: /usr/local/include/kim-api/KIM_EnergyUnit.hpp
-- Installing: /usr/local/include/kim-api/KIM_FunctionTypes.hpp
-- Installing: /usr/local/include/kim-api/KIM_LanguageName.hpp
-- Installing: /usr/local/include/kim-api/KIM_LengthUnit.hpp
-- Installing: /usr/local/include/kim-api/KIM_Log.hpp
-- Installing: /usr/local/include/kim-api/KIM_LogMacros.hpp
-- Installing: /usr/local/include/kim-api/KIM_LogVerbosity.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelComputeArgumentsCreate.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelComputeArgumentsDestroy.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelComputeArguments.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelCompute.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelCreate.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelExtension.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelDestroy.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelDriverCreate.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelDriverHeaders.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelHeaders.hpp
-- Installing: /usr/local/include/kim-api/KIM_Model.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelRefresh.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelRoutineName.hpp
-- Installing: /usr/local/include/kim-api/KIM_ModelWriteParameterizedModel.hpp
-- Installing: /usr/local/include/kim-api/KIM_Numbering.hpp
-- Installing: /usr/local/include/kim-api/KIM_SemVer.hpp
-- Installing: /usr/local/include/kim-api/KIM_SimulatorHeaders.hpp
-- Installing: /usr/local/include/kim-api/KIM_SimulatorModel.hpp
-- Installing: /usr/local/include/kim-api/KIM_SpeciesName.hpp
-- Installing: /usr/local/include/kim-api/KIM_SupportedExtensions.hpp
-- Installing: /usr/local/include/kim-api/KIM_SupportStatus.hpp
-- Installing: /usr/local/include/kim-api/KIM_TemperatureUnit.hpp
-- Installing: /usr/local/include/kim-api/KIM_TimeUnit.hpp
-- Installing: /usr/local/include/kim-api/KIM_UnitSystem.hpp
-- Installing: /usr/local/include/kim-api/KIM_LOG_DEFINES.inc
-- Installing: /usr/local/include/kim-api/KIM_Version.hpp
-- Installing: /usr/local/include/kim-api/KIM_ChargeUnit.h
-- Installing: /usr/local/include/kim-api/KIM_Collection.h
-- Installing: /usr/local/include/kim-api/KIM_Collections.h
-- Installing: /usr/local/include/kim-api/KIM_CollectionItemType.h
-- Installing: /usr/local/include/kim-api/KIM_ComputeArgumentName.h
-- Installing: /usr/local/include/kim-api/KIM_ComputeArguments.h
-- Installing: /usr/local/include/kim-api/KIM_ComputeCallbackName.h
-- Installing: /usr/local/include/kim-api/KIM_DataType.h
-- Installing: /usr/local/include/kim-api/KIM_EnergyUnit.h
-- Installing: /usr/local/include/kim-api/KIM_FunctionTypes.h
-- Installing: /usr/local/include/kim-api/KIM_LanguageName.h
-- Installing: /usr/local/include/kim-api/KIM_LengthUnit.h
-- Installing: /usr/local/include/kim-api/KIM_Log.h
-- Installing: /usr/local/include/kim-api/KIM_LogMacros.h
-- Installing: /usr/local/include/kim-api/KIM_LogVerbosity.h
-- Installing: /usr/local/include/kim-api/KIM_Model.h
-- Installing: /usr/local/include/kim-api/KIM_ModelCompute.h
-- Installing: /usr/local/include/kim-api/KIM_ModelComputeArgumentsCreate.h
-- Installing: /usr/local/include/kim-api/KIM_ModelComputeArgumentsDestroy.h
-- Installing: /usr/local/include/kim-api/KIM_ModelComputeArguments.h
-- Installing: /usr/local/include/kim-api/KIM_ModelCreate.h
-- Installing: /usr/local/include/kim-api/KIM_ModelExtension.h
-- Installing: /usr/local/include/kim-api/KIM_ModelDestroy.h
-- Installing: /usr/local/include/kim-api/KIM_ModelDriverCreate.h
-- Installing: /usr/local/include/kim-api/KIM_ModelDriverHeaders.h
-- Installing: /usr/local/include/kim-api/KIM_ModelHeaders.h
-- Installing: /usr/local/include/kim-api/KIM_ModelRefresh.h
-- Installing: /usr/local/include/kim-api/KIM_ModelRoutineName.h
-- Installing: /usr/local/include/kim-api/KIM_ModelWriteParameterizedModel.h
-- Installing: /usr/local/include/kim-api/KIM_Numbering.h
-- Installing: /usr/local/include/kim-api/KIM_SemVer.h
-- Installing: /usr/local/include/kim-api/KIM_SimulatorHeaders.h
-- Installing: /usr/local/include/kim-api/KIM_SimulatorModel.h
-- Installing: /usr/local/include/kim-api/KIM_SpeciesName.h
-- Installing: /usr/local/include/kim-api/KIM_SupportStatus.h
-- Installing: /usr/local/include/kim-api/KIM_SupportedExtensions.h
-- Installing: /usr/local/include/kim-api/KIM_TemperatureUnit.h
-- Installing: /usr/local/include/kim-api/KIM_TimeUnit.h
-- Installing: /usr/local/include/kim-api/KIM_UnitSystem.h
-- Installing: /usr/local/include/kim-api/KIM_Version.h
-- Installing: /usr/local/lib/kim-api/mod/kim_charge_unit_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_collection_item_type_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_collection_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_collections_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_compute_argument_name_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_compute_arguments_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_compute_callback_name_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_data_type_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_energy_unit_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_language_name_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_length_unit_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_log_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_log_verbosity_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_compute_arguments_create_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_compute_arguments_destroy_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_compute_arguments_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_compute_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_create_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_extension_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_destroy_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_driver_create_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_driver_headers_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_headers_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_refresh_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_routine_name_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_model_write_parameterized_model_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_numbering_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_sem_ver_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_simulator_headers_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_simulator_model_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_species_name_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_support_status_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_supported_extensions_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_temperature_unit_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_time_unit_module.mod
-- Installing: /usr/local/lib/kim-api/mod/kim_unit_system_module.mod
-- Installing: /usr/local/share/cmake/kim-api/kim-api-config.cmake
-- Installing: /usr/local/share/cmake/kim-api/kim-api-macros.cmake
-- Installing: /usr/local/share/cmake/kim-api/kim-api-config-version.cmake
-- Installing: /usr/local/share/cmake/kim-api/kim-api-targets.cmake
-- Installing: /usr/local/share/cmake/kim-api/kim-api-targets-release.cmake
-- Installing: /usr/local/share/cmake/kim-api/kim-api-pre-2.2-compatibility.cmake
-- Installing: /usr/local/share/cmake/kim-api-items/kim-api-items-config.cmake
-- Installing: /usr/local/share/cmake/kim-api-items/kim-api-items-macros.cmake
-- Installing: /usr/local/share/cmake/kim-api-items/kim-api-items-config-version.cmake
-- Installing: /usr/local/share/cmake/kim-api-items/KIM_SharedLibrarySchema.hpp
-- Installing: /usr/local/share/cmake/kim-api-items/item-wrapper.cpp.in
-- Installing: /usr/local/share/cmake/kim-api-items/item-info.txt.in
-- Installing: /usr/local/share/cmake/kim-api-items/item-compiled-with-version.txt
-- Installing: /usr/local/libexec/kim-api/kim-api-portable-model-info
-- Set non-toolchain portion of runtime path of "/usr/local/libexec/kim-api/kim-api-portable-model-info" to ""
-- Installing: /usr/local/libexec/kim-api/kim-api-simulator-model
-- Set non-toolchain portion of runtime path of "/usr/local/libexec/kim-api/kim-api-simulator-model" to ""
-- Installing: /usr/local/libexec/kim-api/kim-api-collections-info
-- Set non-toolchain portion of runtime path of "/usr/local/libexec/kim-api/kim-api-collections-info" to ""
-- Installing: /usr/local/libexec/kim-api/kim-api-base64-encode
-- Installing: /usr/local/libexec/kim-api/kim-api-shared-library-test
-- Installing: /usr/local/bin/kim-api-collections-management
-- Installing: /usr/share/bash-completion/completions/kim-api-collections-management.bash
-- Installing: /usr/local/etc/zsh_completion.d/_kim-api-collections-management
-- Installing: /usr/local/share/emacs/site-lisp/kim-api/kim-api-c-style.el
-- Installing: /usr/local/lib/pkgconfig/libkim-api.pc
-- Installing: /usr/local/lib/kim-api/model-drivers/ex_model_driver_P_LJ/libkim-api-model-driver.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/model-drivers/ex_model_driver_P_LJ/libkim-api-model-driver.so" to ""
-- Installing: /usr/local/lib/kim-api/model-drivers/ex_model_driver_P_Morse/libkim-api-model-driver.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/model-drivers/ex_model_driver_P_Morse/libkim-api-model-driver.so" to ""
-- Installing: /usr/local/lib/kim-api/model-drivers/LennardJones612__MD_414112407348_003/libkim-api-model-driver.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/model-drivers/LennardJones612__MD_414112407348_003/libkim-api-model-driver.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_P_LJ/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_P_LJ/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_P_MLJ_Fortran/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_P_MLJ_Fortran/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse_07C/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse_07C/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse_07C_w_Extensions/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse_07C_w_Extensions/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse_MultiCutoff/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_P_Morse_MultiCutoff/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/ex_model_Ar_SLJ_MultiCutoff/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/ex_model_Ar_SLJ_MultiCutoff/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/LennardJones612_UniversalShifted__MO_959249795837_003/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/LennardJones612_UniversalShifted__MO_959249795837_003/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/portable-models/LennardJones_Ar/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/portable-models/LennardJones_Ar/libkim-api-portable-model.so" to ""
-- Installing: /usr/local/lib/kim-api/simulator-models/Sim_LAMMPS_LJcut_AkersonElliott_Alchemy_PbAu/libkim-api-simulator-model.so
-- Set non-toolchain portion of runtime path of "/usr/local/lib/kim-api/simulator-models/Sim_LAMMPS_LJcut_AkersonElliott_Alchemy_PbAu/libkim-api-simulator-model.so" to ""
miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/build/.
miroi@MiroPhenomII-X6:~/software/kim-api/kim-api-2.4.1/build/.sudo ldconfig
/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link


Installing KIM Models
---------------------

https://openkim.org/doc/usage/obtaining-models/#installing_models

miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/buildup_on_servers/wsl2/wsl2_win10_MiroPhenomII-X6/.kim-api-collections-management install user SW_StillingerWeber_1985_Si__MO_405512056662_005
Downloading.............. SW_StillingerWeber_1985_Si__MO_405512056662_005
This item needs its driver 'SW__MD_335816936951_004', but it is not currently installed.
Trying to find it at openkim.org.
Downloading.............. SW__MD_335816936951_004
[100%] Built target SW__MD_335816936951_004
Install the project...
-- Install configuration: "Release"
-- Installing: /home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/model-drivers-dir/SW__MD_335816936951_004/libkim-api-model-driver.so
-- Set non-toolchain portion of runtime path of "/home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/model-drivers-dir/SW__MD_335816936951_004/libkim-api-model-driver.so" to ""
[100%] Built target SW_StillingerWeber_1985_Si__MO_405512056662_005
Install the project...
-- Install configuration: "Release"
-- Installing: /home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/portable-models-dir/SW_StillingerWeber_1985_Si__MO_405512056662_005/libkim-api-portable-model.so
-- Set non-toolchain portion of runtime path of "/home/miroi/.kim-api/2.4.1+GNU.GNU.GNU.2026-01-02-19-24-56/portable-models-dir/SW_StillingerWeber_1985_Si__MO_405512056662_005/libkim-api-portable-model.so" to ""

Success!
miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/buildup_on_servers/wsl2/wsl2_win10_MiroPhenomII-X6/.

miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/openkim-ase/buildup_on_servers/wsl2/wsl2_win10_MiroPhenomII-X6/.kim-api-collections-management list > kim-api-collections-management-list.log_SAVED


