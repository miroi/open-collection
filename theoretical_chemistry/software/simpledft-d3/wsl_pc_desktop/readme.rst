============
simple-dftd3
============

see https://github.com/dftd3/simple-dftd3


milias@DESKTOP-7OTLCGO:~/work/software/simple_dft-d3/.git clone git@github.com:dftd3/simple-dftd3.git

build
~~~~~

milias@DESKTOP-7OTLCGO:~/work/software/simple_dft-d3/simple-dftd3/.meson setup _build --prefix=~/work/software/simple_dft-d3/.

milias@DESKTOP-7OTLCGO:~/work/software/simple_dft-d3/simple-dftd3/.meson compile -C _build


tests
~~~~~

milias@DESKTOP-7OTLCGO:~/work/software/simple_dft-d3/simple-dftd3/.meson test -C _build --print-errorlogs
.
.
Summary of Failures:

52/55 mctc-lib / ncoord          TIMEOUT        30.08s   killed by signal 15 SIGTERM
53/55 s-dftd3:unit / dftd3       TIMEOUT        30.18s   killed by signal 15 SIGTERM
54/55 s-dftd3:unit / param       TIMEOUT        30.16s   killed by signal 15 SIGTERM
55/55 s-dftd3:unit / periodic    TIMEOUT        30.11s   killed by signal 15 SIGTERM

Ok:                 50
Expected Fail:      1
Fail:               0
Unexpected Pass:    0
Skipped:            0
Timeout:            4

Full log written to /home/milias/work/software/simple_dft-d3/simple-dftd3/_build/meson-logs/testlog.txt

executable
~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/simple_dft-d3/simple-dftd3/_build/app/.s-dftd3 --help

or 

~/work/software/simple_dft-d3/simple-dftd3/_build/app/s-dftd3 --help

