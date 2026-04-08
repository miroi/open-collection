==============================================
ELPA buildup with openmpi-5.0.9-intelv2025.3.1
==============================================

export MODULEPATH=/cvmfs/nica.jinr.ru/sw/202309/MODULES/slc9_x86-64:$MODULEPATH
module add autotools

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/elpa/elpa-new_release_2026_02_001/intelmpi2025.3.1/elpa-new_release_2026_02_001/.module list

Currently Loaded Modules:
  1) autotools/v1.7.0-1

autoconf works...
https://github.com/marekandreas/elpa/issues/70#issuecomment-4202676609

autoreconf -f -i
libtoolize: putting auxiliary files in '.'.
libtoolize: copying file './ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
libtoolize: copying file 'm4/libtool.m4'
libtoolize: copying file 'm4/ltoptions.m4'
libtoolize: copying file 'm4/ltsugar.m4'
libtoolize: copying file 'm4/ltversion.m4'
libtoolize: copying file 'm4/lt~obsolete.m4'
configure.ac:351: warning: The macro `AC_PROG_CC_C99' is obsolete.
configure.ac:351: You should run autoupdate.
./lib/autoconf/c.m4:1659: AC_PROG_CC_C99 is expanded from...
configure.ac:351: the top level
configure.ac:349: installing './ar-lib'
configure.ac:197: installing './compile'
configure.ac:250: installing './config.guess'
configure.ac:250: installing './config.sub'
configure.ac:9: installing './install-sh'
configure.ac:9: installing './missing'
generated_headers.am:26: warning: call extract_interface,!c>: non-POSIX variable name
generated_headers.am:26: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:27: warning: call extract_interface,!c_o>: non-POSIX variable name
generated_headers.am:27: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:28: warning: call extract_interface,!c_no>: non-POSIX variable name
generated_headers.am:28: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:51: warning: call extract_interface,!c>: non-POSIX variable name
generated_headers.am:51: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:54: warning: filter-out $(wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:54: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:54: warning: wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:54: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:56: warning: call extract_interface,!f>: non-POSIX variable name
generated_headers.am:56: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:60: warning: filter-out $(wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:60: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:60: warning: wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:60: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
generated_headers.am:62: warning: call extract_interface,!pf>: non-POSIX variable name
generated_headers.am:62: (probably a GNU make extension)
Makefile.am:766:   'generated_headers.am' included from here
Makefile.am:771: warning: wildcard modules/*: non-POSIX variable name
Makefile.am:771: (probably a GNU make extension)
Makefile.am:969: warning: '%'-style pattern rules are a GNU make extension
Makefile.am:973: warning: '%'-style pattern rules are a GNU make extension
Makefile.am:983: warning: '%'-style pattern rules are a GNU make extension
Makefile.am:1279: warning: foreach p,$(bin_PROGRAMS: non-POSIX variable name
Makefile.am:1279: (probably a GNU make extension)
Makefile.am:1279: warning: foreach o,$($p_OBJECTS: non-POSIX variable name
Makefile.am:1279: (probably a GNU make extension)
Makefile.am:1279: warning: eval $(call require_elpa_lib,$o: non-POSIX variable name
Makefile.am:1279: (probably a GNU make extension)
Makefile.am: installing './depcomp'
Makefile.am:948: installing './py-compile'
parallel-tests: installing './test-driver'

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/elpa/elpa_git_cloned/openmpi5.0.9-intel2025.3.1/elpa_cloned/../configure --help
`configure' configures elpa 2026.02.001 to adapt to many kinds of systems.

Usage: ./configure [OPTION]... [VAR=VALUE]...
