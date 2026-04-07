=============
ELPA buildups
=============

own  intel/v2025.3.1 autotools/v1.7.0-1 build of ELPA

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/elpa/elpa-2025.01.002/elpa-2025.01.002/.module list

Currently Loaded Modules:
  1) intel/v2025.3.1   2) autotools/v1.7.0-1


milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/elpa/elpa-2025.01.002/elpa-2025.01.002/.autoreconf -f -i
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
configure.ac:197: installing './compile'
configure.ac:9: installing './missing'
generated_headers.am:26: warning: call extract_interface,!c>: non-POSIX variable name
generated_headers.am:26: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:27: warning: call extract_interface,!c_o>: non-POSIX variable name
generated_headers.am:27: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:28: warning: call extract_interface,!c_no>: non-POSIX variable name
generated_headers.am:28: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:51: warning: call extract_interface,!c>: non-POSIX variable name
generated_headers.am:51: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:54: warning: filter-out $(wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:54: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:54: warning: wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:54: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:56: warning: call extract_interface,!f>: non-POSIX variable name
generated_headers.am:56: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:60: warning: filter-out $(wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:60: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:60: warning: wildcard $(top_srcdir: non-POSIX variable name
generated_headers.am:60: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
generated_headers.am:62: warning: call extract_interface,!pf>: non-POSIX variable name
generated_headers.am:62: (probably a GNU make extension)
Makefile.am:764:   'generated_headers.am' included from here
Makefile.am:769: warning: wildcard modules/*: non-POSIX variable name
Makefile.am:769: (probably a GNU make extension)
Makefile.am:967: warning: '%'-style pattern rules are a GNU make extension
Makefile.am:971: warning: '%'-style pattern rules are a GNU make extension
Makefile.am:981: warning: '%'-style pattern rules are a GNU make extension
Makefile.am:1270: warning: foreach p,$(bin_PROGRAMS: non-POSIX variable name
Makefile.am:1270: (probably a GNU make extension)
Makefile.am:1270: warning: foreach o,$($p_OBJECTS: non-POSIX variable name
Makefile.am:1270: (probably a GNU make extension)
Makefile.am:1270: warning: eval $(call require_elpa_lib,$o: non-POSIX variable name
Makefile.am:1270: (probably a GNU make extension)
Makefile.am: installing './depcomp'


  --disable-avx-kernels   do not build AVX kernels, default: enabled
  --disable-avx2-kernels  do not build AVX2 kernels, default: enabled
  --disable-avx512-kernels


In file included from src/elpa2/kernels/complex_sse_1hv_double_precision.c:54:
src/elpa2/kernels/complex_128bit_256bit_512bit_BLOCK_template.c:2201:49: error: always_inline function '_mm_addsub_pd' requires target feature 'sse3', but would be inlined into function 'hh_trafo_complex_kernel_6_SSE_1hv_double' that is compiled without support for 'sse3'
 2201 |         x1 = _SIMD_ADD( ADDITIONAL_ARGUMENT x1, _ADDSUB( _SIMD_MUL( ADDITIONAL_ARGUMENT h1_real, q1), _SIMD_SHUFFLE(tmp1, tmp1, _SHUFFLE_VAL)));
      |                                                 ^


