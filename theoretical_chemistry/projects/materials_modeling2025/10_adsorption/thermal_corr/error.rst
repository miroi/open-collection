
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/10_adsorption/thermal_corr/.mpirun -np 4 /usr/bin/pw.x < Hg_on_C8.scf.in

     Program PWSCF v.6.7MaX starts on  3Sep2025 at  6:48: 9

     This program is part of the open-source Quantum ESPRESSO suite
     for quantum simulation of materials; please cite
         "P. Giannozzi et al., J. Phys.:Condens. Matter 21 395502 (2009);
         "P. Giannozzi et al., J. Phys.:Condens. Matter 29 465901 (2017);
          URL http://www.quantum-espresso.org",
     in publications or presentations arising from this work. More details at
     http://www.quantum-espresso.org/quote

     Parallel version (MPI), running on     4 processors

     MPI processes distributed on     1 nodes
     R & G space division:  proc/nbgrp/npool/nimage =       4
     Waiting for input...
     Reading input from standard input
Warning: card &CELL ignored
Warning: card / ignored
Warning: card &FCP ignored
Warning: card / ignored
Warning: card &RISM ignored
Warning: card / ignored

     Current dimensions of program PWSCF are:
     Max number of different atomic species (ntypx) = 10
     Max number of k-points (npk) =  40000
     Max angular momentum in pseudopotentials (lmaxx) =  3
     Message from routine read_pp_mesh:
     mesh size missing, using the one in header
*** buffer overflow detected ***: terminated

Program received signal SIGABRT: Process abort signal.

Backtrace for this error:
*** buffer overflow detected ***: terminated

Program received signal SIGABRT: Process abort signal.

Backtrace for this error:
*** buffer overflow detected ***: terminated

Program received signal SIGABRT: Process abort signal.

Backtrace for this error:
*** buffer overflow detected ***: terminated

Program received signal SIGABRT: Process abort signal.

Backtrace for this error:
#0  0x7378dfe23e59 in ???
#1  0x7378dfe22e75 in ???
#2  0x7378dfa4532f in ???
        at ./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c:0
#3  0x7378dfa9eb2c in __pthread_kill_implementation
        at ./nptl/pthread_kill.c:44
#4  0x7378dfa9eb2c in __pthread_kill_internal
        at ./nptl/pthread_kill.c:78
#5  0x7378dfa9eb2c in __GI___pthread_kill
        at ./nptl/pthread_kill.c:89
#6  0x7378dfa4527d in __GI_raise
        at ../sysdeps/posix/raise.c:26
#7  0x7378dfa288fe in __GI_abort
        at ./stdlib/abort.c:79
#0  0x70f688023e59 in ???
#1  0x70f688022e75 in ???
#8  0x7378dfa297b5 in __libc_message_impl
        at ../sysdeps/posix/libc_fatal.c:134
#9  0x7378dfb36c18 in __GI___fortify_fail
        at ./debug/fortify_fail.c:24
#10  0x7378dfb365d3 in __GI___chk_fail
        at ./debug/chk_fail.c:28
#11  0x7378dfb37db4 in ___snprintf_chk
        at ./debug/snprintf_chk.c:29
#2  0x70f687c4532f in ???
        at ./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c:0
#12  0x61e55ca8196e in ???
#13  0x61e55c89f1d7 in ???
#14  0x61e55c903007 in ???
#15  0x61e55c7830c7 in ???
#16  0x61e55c781f22 in ???
#17  0x7378dfa2a1c9 in __libc_start_call_main
        at ../sysdeps/nptl/libc_start_call_main.h:58
#18  0x7378dfa2a28a in __libc_start_main_impl
        at ../csu/libc-start.c:360
#19  0x61e55c781f54 in ???
#20  0xffffffffffffffff in ???
#0  0x702100623e59 in ???
#1  0x702100622e75 in ???
#2  0x70210024532f in ???
        at ./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c:0
#3  0x70f687c9eb2c in __pthread_kill_implementation
        at ./nptl/pthread_kill.c:44
#4  0x70f687c9eb2c in __pthread_kill_internal
        at ./nptl/pthread_kill.c:78
#5  0x70f687c9eb2c in __GI___pthread_kill
        at ./nptl/pthread_kill.c:89
#6  0x70f687c4527d in __GI_raise
        at ../sysdeps/posix/raise.c:26
#7  0x70f687c288fe in __GI_abort
        at ./stdlib/abort.c:79
#3  0x70210029eb2c in __pthread_kill_implementation
        at ./nptl/pthread_kill.c:44
#4  0x70210029eb2c in __pthread_kill_internal
        at ./nptl/pthread_kill.c:78
#5  0x70210029eb2c in __GI___pthread_kill
        at ./nptl/pthread_kill.c:89
#6  0x70210024527d in __GI_raise
        at ../sysdeps/posix/raise.c:26
#7  0x7021002288fe in __GI_abort
        at ./stdlib/abort.c:79
#8  0x70f687c297b5 in __libc_message_impl
        at ../sysdeps/posix/libc_fatal.c:134
#9  0x70f687d36c18 in __GI___fortify_fail
        at ./debug/fortify_fail.c:24
#10  0x70f687d365d3 in __GI___chk_fail
        at ./debug/chk_fail.c:28
#11  0x70f687d37db4 in ___snprintf_chk
        at ./debug/snprintf_chk.c:29
#12  0x5aaadfa8c96e in ???
#13  0x5aaadf8aa1d7 in ???
#14  0x5aaadf90e007 in ???
#15  0x5aaadf78e0c7 in ???
#16  0x5aaadf78cf22 in ???
#8  0x7021002297b5 in __libc_message_impl
        at ../sysdeps/posix/libc_fatal.c:134
#9  0x702100336c18 in __GI___fortify_fail
        at ./debug/fortify_fail.c:24
#10  0x7021003365d3 in __GI___chk_fail
        at ./debug/chk_fail.c:28
#11  0x702100337db4 in ___snprintf_chk
        at ./debug/snprintf_chk.c:29
#12  0x5d539b8cb96e in ???
#13  0x5d539b6e91d7 in ???
#14  0x5d539b74d007 in ???
#15  0x5d539b5cd0c7 in ???
#16  0x5d539b5cbf22 in ???
#17  0x70f687c2a1c9 in __libc_start_call_main
        at ../sysdeps/nptl/libc_start_call_main.h:58
#18  0x70f687c2a28a in __libc_start_main_impl
        at ../csu/libc-start.c:360
#19  0x5aaadf78cf54 in ???
#20  0xffffffffffffffff in ???
#17  0x70210022a1c9 in __libc_start_call_main
        at ../sysdeps/nptl/libc_start_call_main.h:58
#18  0x70210022a28a in __libc_start_main_impl
        at ../csu/libc-start.c:360
#19  0x5d539b5cbf54 in ???
#20  0xffffffffffffffff in ???
#0  0x7dba5e023e59 in ???
#1  0x7dba5e022e75 in ???
#2  0x7dba5dc4532f in ???
        at ./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c:0
#3  0x7dba5dc9eb2c in __pthread_kill_implementation
        at ./nptl/pthread_kill.c:44
#4  0x7dba5dc9eb2c in __pthread_kill_internal
        at ./nptl/pthread_kill.c:78
#5  0x7dba5dc9eb2c in __GI___pthread_kill
        at ./nptl/pthread_kill.c:89
#6  0x7dba5dc4527d in __GI_raise
        at ../sysdeps/posix/raise.c:26
#7  0x7dba5dc288fe in __GI_abort
        at ./stdlib/abort.c:79
#8  0x7dba5dc297b5 in __libc_message_impl
        at ../sysdeps/posix/libc_fatal.c:134
#9  0x7dba5dd36c18 in __GI___fortify_fail
        at ./debug/fortify_fail.c:24
#10  0x7dba5dd365d3 in __GI___chk_fail
        at ./debug/chk_fail.c:28
#11  0x7dba5dd37db4 in ___snprintf_chk
        at ./debug/snprintf_chk.c:29
#12  0x5bf4e80ce96e in ???
#13  0x5bf4e7eec1d7 in ???
#14  0x5bf4e7f50007 in ???
#15  0x5bf4e7dd00c7 in ???
#16  0x5bf4e7dcef22 in ???
#17  0x7dba5dc2a1c9 in __libc_start_call_main
        at ../sysdeps/nptl/libc_start_call_main.h:58
#18  0x7dba5dc2a28a in __libc_start_main_impl
        at ../csu/libc-start.c:360
#19  0x5bf4e7dcef54 in ???
#20  0xffffffffffffffff in ???
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
mpirun noticed that process rank 1 with PID 0 on node MIRO exited on signal 6 (Aborted).
--------------------------------------------------------------------------
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/10_adsorption/thermal_corr/.
