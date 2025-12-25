=============================
GAMESS-US testing with Python
=============================

install Python from Microsoft store

follow https://www.msg.chem.iastate.edu/GAMESS/download/GAMESS-Windows-64-Bit-README-THEN-README-AGAIN.pdf

Launch the WindowsCommand-Prompt shortcut:

C:\Users\Public\gamess-64>python tests\runtest.py --version=2023.R1.intel --folder=travis-ci
C:\Users\Public\gamess-64>python tests\runtest.py --version=2023.R1.intel --folder=travis-ci
C:\Users\Public\gamess-64\tests\runtest.py:32: SyntaxWarning: invalid escape sequence '\*'
  input_file_path = re.sub("(\*|\?| |!|\$|#|&|\"|\'|\(|\)|\||<|>|\\\|;)", r"\\\1", input_file_path)
C:\Users\Public\gamess-64\tests\checkgms_parsers.py:31: SyntaxWarning: invalid escape sequence '\.'
  """
[             Run parameters             ]
{
  "dryrun": false,
  "filter_filepath": "",
  "filter_file": "",
  "filter_folder": "travis-ci",
  "debug": false,
  "skip_file": "",
  "skip_folder": "",
  "test_type": "",
  "ncpus": "1",
  "pre": "",
  "post": "",
  "no_counter": false,
  "path": "",
  "version": "2023.R1.intel",
  "coverage": false,
  "print_to_stdout": false,
  "breakdown": false,
  "no_accumulate": false,
  "sourcefile": "",
  "threads": "1",
  "output_extension": ".log",
  "mpi": false,
  "hpe-cray-ex": false,
  "hpe-cray-cs": false,
  "cray-xt": false,
  "cray-xc": false,
  "stderr": false,
  "skip_log": false,
  "no_skip": false,
  "queue": "compute",
  "bwrap": false
}
[  17:45:19.710670   ] [Running input file  ] [ 1 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam05.inp
[  17:45:25.789057   ] [Running input file  ] [ 2 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam32.inp
[  17:45:33.453644   ] [Running input file  ] [ 3 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam39.inp
[  17:45:40.553284   ] [Running input file  ] [ 4 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam42.inp
[  17:45:52.852560   ] [Running input file  ] [ 5 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam45.inp
[  17:46:01.498041   ] [Running input file  ] [ 6 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam46.inp
[  17:46:11.774791   ] [Running input file  ] [ 7 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\exam47.inp
[  17:46:22.815502   ] [Running input file  ] [ 8 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam01.inp
[  17:46:28.668349   ] [Running input file  ] [ 9 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam02.inp
[  17:46:34.628577   ] [Running input file  ] [10 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam03.inp
[  17:46:40.240514   ] [Running input file  ] [11 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam04.inp
[  17:46:45.949408   ] [Running input file  ] [12 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam06.inp
[  17:46:51.783010   ] [Running input file  ] [13 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam07.inp
[  17:46:57.555674   ] [Running input file  ] [14 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam08.inp
[  17:47:03.255286   ] [Running input file  ] [15 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam09.inp
[  17:47:09.169757   ] [Running input file  ] [16 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam10.inp
[  17:47:14.871594   ] [Running input file  ] [17 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam11.inp
[  17:47:20.655119   ] [Running input file  ] [18 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam12.inp
[  17:47:27.414774   ] [Running input file  ] [19 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam13.inp
[  17:47:33.206486   ] [Running input file  ] [20 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam14.inp
[  17:47:39.240256   ] [Running input file  ] [21 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam15.inp
[  17:47:45.052988   ] [Running input file  ] [22 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam16.inp
[  17:47:50.789049   ] [Running input file  ] [23 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam17.inp
[  17:47:56.619654   ] [Running input file  ] [24 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam18.inp
[  17:48:02.359869   ] [Running input file  ] [25 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam19.inp
[  17:48:08.205508   ] [Running input file  ] [26 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam20.inp
[  17:48:13.994984   ] [Running input file  ] [27 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam21.inp
[  17:48:19.734621   ] [Running input file  ] [28 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam22.inp
[  17:48:25.845691   ] [Running input file  ] [29 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam23.inp
[  17:48:31.617042   ] [Running input file  ] [30 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam24.inp
[  17:48:37.745771   ] [Running input file  ] [31 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam25.inp
[  17:48:43.899663   ] [Running input file  ] [32 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam26.inp
[  17:48:49.788054   ] [Running input file  ] [33 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam27.inp
[  17:48:55.634515   ] [Running input file  ] [34 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam28.inp
[  17:49:01.562862   ] [Running input file  ] [35 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam29.inp
[  17:49:07.584726   ] [Running input file  ] [36 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam30.inp
[  17:49:14.106269   ] [Running input file  ] [37 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam31.inp
[  17:49:20.711440   ] [Running input file  ] [38 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam33.inp
[  17:49:28.550363   ] [Running input file  ] [39 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam34.inp
[  17:49:34.490727   ] [Running input file  ] [40 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam35-protect.inp
[  17:49:41.376032   ] [Running input file  ] [41 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam36-protect.inp
[  17:49:49.260734   ] [Running input file  ] [42 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam37.inp
[  17:49:55.160188   ] [Running input file  ] [43 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam38.inp
[  17:50:03.546812   ] [Running input file  ] [44 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam40.inp
[  17:50:10.675321   ] [Running input file  ] [45 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam41.inp
[  17:50:18.999174   ] [Running input file  ] [46 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam43.inp
[  17:50:26.050445   ] [Running input file  ] [47 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam44.inp
[  17:50:32.544067   ] [Running input file  ] [48 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam48.inp
[  17:50:40.904439   ] [Running input file  ] [49 / 49] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam49.inp

C:\Users\Public\gamess-64>


validating tests
~~~~~~~~~~~~~~~~
cd tests
python checkgms.py --verbose_validation > tests_validation.log


C:\Users\Public\gamess-64>python tests\runtest.py --version=2023.R1.intel --folder=travis-ci\parallel -n 2
C:\Users\Public\gamess-64>python tests\runtest.py --version=2023.R1.intel --folder=travis-ci\parallel -n 2
C:\Users\Public\gamess-64\tests\runtest.py:32: SyntaxWarning: invalid escape sequence '\*'
  input_file_path = re.sub("(\*|\?| |!|\$|#|&|\"|\'|\(|\)|\||<|>|\\\|;)", r"\\\1", input_file_path)
[             Run parameters             ]
{
  "dryrun": false,
  "filter_filepath": "",
  "filter_file": "",
  "filter_folder": "travis-ci\\parallel",
  "debug": false,
  "skip_file": "",
  "skip_folder": "",
  "test_type": "",
  "ncpus": "2",
  "pre": "",
  "post": "",
  "no_counter": false,
  "path": "",
  "version": "2023.R1.intel",
  "coverage": false,
  "print_to_stdout": false,
  "breakdown": false,
  "no_accumulate": false,
  "sourcefile": "",
  "threads": "1",
  "output_extension": ".log",
  "mpi": false,
  "hpe-cray-ex": false,
  "hpe-cray-cs": false,
  "cray-xt": false,
  "cray-xc": false,
  "stderr": false,
  "skip_log": false,
  "no_skip": false,
  "queue": "compute",
  "bwrap": false
}
[  18:01:41.793150   ] [Running input file  ] [ 1 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam01.inp
[  18:01:47.859025   ] [Running input file  ] [ 2 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam02.inp
[  18:01:53.959507   ] [Running input file  ] [ 3 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam03.inp
[  18:02:00.364435   ] [Running input file  ] [ 4 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam04.inp
[  18:02:06.490763   ] [Running input file  ] [ 5 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam06.inp
[  18:02:12.594662   ] [Running input file  ] [ 6 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam07.inp
[  18:02:18.742569   ] [Running input file  ] [ 7 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam08.inp
[  18:02:24.956562   ] [Running input file  ] [ 8 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam09.inp
[  18:02:30.885400   ] [Running input file  ] [ 9 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam10.inp
[  18:02:36.943214   ] [Running input file  ] [10 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam11.inp
[  18:02:43.030934   ] [Running input file  ] [11 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam12.inp
[  18:02:49.548388   ] [Running input file  ] [12 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam13.inp
[  18:02:55.497335   ] [Running input file  ] [13 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam14.inp
[  18:03:01.789714   ] [Running input file  ] [14 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam15.inp
[  18:03:08.008641   ] [Running input file  ] [15 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam16.inp
[  18:03:14.061397   ] [Running input file  ] [16 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam17.inp
[  18:03:19.899511   ] [Running input file  ] [17 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam18.inp
[  18:03:25.974576   ] [Running input file  ] [18 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam19.inp
[  18:03:32.254253   ] [Running input file  ] [19 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam20.inp
[  18:03:38.378133   ] [Running input file  ] [20 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam21.inp
[  18:03:44.403575   ] [Running input file  ] [21 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam22.inp
[  18:03:50.692289   ] [Running input file  ] [22 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam23.inp
[  18:03:56.633975   ] [Running input file  ] [23 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam24.inp
[  18:04:02.985268   ] [Running input file  ] [24 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam25.inp
[  18:04:09.078104   ] [Running input file  ] [25 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam26.inp
[  18:04:15.058302   ] [Running input file  ] [26 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam27.inp
[  18:04:20.986173   ] [Running input file  ] [27 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam28.inp
[  18:04:26.831234   ] [Running input file  ] [28 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam29.inp
[  18:04:32.809973   ] [Running input file  ] [29 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam30.inp
[  18:04:39.061970   ] [Running input file  ] [30 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam31.inp
[  18:04:45.476972   ] [Running input file  ] [31 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam33.inp
[  18:04:52.528016   ] [Running input file  ] [32 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam34.inp
[  18:04:58.697116   ] [Running input file  ] [33 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam35-protect.inp
[  18:05:05.879419   ] [Running input file  ] [34 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam36-protect.inp
[  18:05:13.537508   ] [Running input file  ] [35 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam37.inp
[  18:05:19.691942   ] [Running input file  ] [36 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam38.inp
[  18:05:27.286646   ] [Running input file  ] [37 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam40.inp
[  18:05:35.221357   ] [Running input file  ] [38 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam41.inp
[  18:05:42.764536   ] [Running input file  ] [39 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam43.inp
[  18:05:49.549221   ] [Running input file  ] [40 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam44.inp
[  18:05:55.792678   ] [Running input file  ] [41 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam48.inp
[  18:06:03.472488   ] [Running input file  ] [42 / 42] C:\\Users\\Public\\gamess-64\\tests\\travis-ci\\parallel\\exam49.inp

C:\Users\Public\gamess-64>

validation
~~~~~~~~~~
cd tests
C:\Users\Public\gamess-64\tests>python checkgms.py --verbose_validation > parallel_test_python_validation.log
cd ..
C:\Users\Public\gamess-64>clean-runall-files.bat

Finish removing exam*log, scratch\exam*.*, and restart\exam*.* files

Press any key to continue . . .

