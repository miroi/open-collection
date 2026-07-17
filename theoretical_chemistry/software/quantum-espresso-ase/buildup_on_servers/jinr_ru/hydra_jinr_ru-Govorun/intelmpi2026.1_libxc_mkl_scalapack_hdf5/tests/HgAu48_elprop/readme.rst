Hg@Au48(111)
============

IntelMPI 2026.1

HDF5 QE

charge-density.dat → charge-density.hdf5

works, see https://gitlab.com/QEF/q-e/-/work_items/866

Files 
-----
proper big files:

ls -lt tmp/El_Hg.save/
total 106789603
-rw-r--r--. 1 milias hybrilit   483952101 Jul 16 07:53 atomic_proj.xml
-rw-r--r--. 1 milias hybrilit 11087949620 Jul 16 07:39 wfc9.hdf5
-rw-r--r--. 1 milias hybrilit 11088343288 Jul 16 07:26 wfc8.hdf5
-rw-r--r--. 1 milias hybrilit 11090132688 Jul 16 07:12 wfc7.hdf5
-rw-r--r--. 1 milias hybrilit 11086911768 Jul 16 06:57 wfc6.hdf5
-rw-r--r--. 1 milias hybrilit 11092065240 Jul 16 06:42 wfc5.hdf5
-rw-r--r--. 1 milias hybrilit 11086911768 Jul 16 06:29 wfc4.hdf5
-rw-r--r--. 1 milias hybrilit 11090132688 Jul 16 06:16 wfc3.hdf5
-rw-r--r--. 1 milias hybrilit 11088343288 Jul 16 06:02 wfc2.hdf5
-rw-r--r--. 1 milias hybrilit 11087949620 Jul 16 05:48 wfc1.hdf5
-rw-r--r--. 1 milias hybrilit      348124 Jul 16 05:34 Au_fr_pbesol.upf
-rw-r--r--. 1 milias hybrilit      326579 Jul 16 05:34 Hg_fr_pbesol.upf
-rw-r--r--. 1 milias hybrilit    69417492 Jul 16 05:34 charge-density.hdf5
-rw-r--r--. 1 milias hybrilit      531629 Jul 16 05:34 data-file-schema.xml

ls -lt tmp/El_Hg_NSCF.save/
total 291424211
-rw-r--r--. 1 milias hybrilit  1344311075 Jul 16 22:19 atomic_proj.xml
-rw-r--r--. 1 milias hybrilit 11089882172 Jul 16 21:34 wfc25.hdf5
-rw-r--r--. 1 milias hybrilit 11088343288 Jul 16 21:21 wfc24.hdf5
-rw-r--r--. 1 milias hybrilit 11090705296 Jul 16 21:08 wfc23.hdf5
-rw-r--r--. 1 milias hybrilit 11088987472 Jul 16 20:54 wfc22.hdf5
-rw-r--r--. 1 milias hybrilit 11090812660 Jul 16 20:40 wfc21.hdf5
-rw-r--r--. 1 milias hybrilit 11088200136 Jul 16 20:27 wfc20.hdf5
-rw-r--r--. 1 milias hybrilit 11088880108 Jul 16 20:14 wfc19.hdf5
-rw-r--r--. 1 milias hybrilit 11086482312 Jul 16 20:00 wfc18.hdf5
-rw-r--r--. 1 milias hybrilit 11086947556 Jul 16 19:47 wfc17.hdf5
-rw-r--r--. 1 milias hybrilit 11088200136 Jul 16 19:33 wfc16.hdf5
-rw-r--r--. 1 milias hybrilit 11087448588 Jul 16 19:19 wfc15.hdf5
-rw-r--r--. 1 milias hybrilit 11086482312 Jul 16 19:05 wfc14.hdf5
-rw-r--r--. 1 milias hybrilit 11092065240 Jul 16 18:52 wfc13.hdf5
-rw-r--r--. 1 milias hybrilit 11086482312 Jul 16 18:38 wfc12.hdf5
-rw-r--r--. 1 milias hybrilit 11087448588 Jul 16 18:24 wfc11.hdf5
-rw-r--r--. 1 milias hybrilit 11088200136 Jul 16 18:09 wfc10.hdf5
-rw-r--r--. 1 milias hybrilit 11086947556 Jul 16 17:57 wfc9.hdf5
-rw-r--r--. 1 milias hybrilit 11086482312 Jul 16 17:44 wfc8.hdf5
-rw-r--r--. 1 milias hybrilit 11088880108 Jul 16 17:30 wfc7.hdf5
-rw-r--r--. 1 milias hybrilit 11088200136 Jul 16 17:17 wfc6.hdf5
-rw-r--r--. 1 milias hybrilit 11090812660 Jul 16 17:03 wfc5.hdf5
-rw-r--r--. 1 milias hybrilit 11088987472 Jul 16 16:49 wfc4.hdf5
-rw-r--r--. 1 milias hybrilit 11090705296 Jul 16 16:35 wfc3.hdf5
-rw-r--r--. 1 milias hybrilit 11088343288 Jul 16 16:21 wfc2.hdf5
-rw-r--r--. 1 milias hybrilit 11089882172 Jul 16 16:08 wfc1.hdf5
-rw-r--r--. 1 milias hybrilit      348124 Jul 16 15:55 Au_fr_pbesol.upf
-rw-r--r--. 1 milias hybrilit      326579 Jul 16 15:55 Hg_fr_pbesol.upf
-rw-r--r--. 1 milias hybrilit     1403799 Jul 16 15:55 data-file-schema.xml
-rw-r--r--. 1 milias hybrilit    69417492 Jul 16 05:34 charge-density.hdf5

All files in the directory:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
ls -lt
total 250798
-rw-r--r--. 1 milias hybrilit      3246 Jul 17 10:50 readme.rst
drwxr-xr-x. 2 milias hybrilit     11264 Jul 17 10:48 one-tmp_diskio-high/
-rw-r--r--. 1 milias hybrilit     33352 Jul 16 22:20 hydra_ase_intel2026_N1_n05p_log_slurm_job.625564.n05p032.std_out_err
drwxr-xr-x. 2 milias hybrilit     49152 Jul 16 22:20 pdos_results/
-rw-r--r--. 1 milias hybrilit  70108125 Jul 16 22:20 projwfc.out
-rw-r--r--. 1 milias hybrilit      2420 Jul 16 21:35 dos.out
-rw-r--r--. 1 milias hybrilit       200 Jul 16 21:35 projwfc.in
-rw-r--r--. 1 milias hybrilit    132088 Jul 16 21:35 total_dos.dat
-rw-r--r--. 1 milias hybrilit       175 Jul 16 21:34 dos.in
-rw-r--r--. 1 milias hybrilit       904 Jul 16 21:34 espresso.err
-rw-r--r--. 1 milias hybrilit    277525 Jul 16 21:34 espresso.pwo
drwxr-xr-x. 4 milias hybrilit     11264 Jul 16 21:34 tmp/
-rw-r--r--. 1 milias hybrilit      3425 Jul 16 07:54 espresso.pwi
-rw-r--r--. 1 milias hybrilit      8381 Jul 16 07:54 lowdin.out
drwxr-xr-x. 2 milias hybrilit     49152 Jul 16 07:54 scf_files/
-rw-r--r--. 1 milias hybrilit  79990400 Jul 16 07:39 charge_density.cube
-rw-r--r--. 1 milias hybrilit 104493410 Jul 16 07:39 charge_density
-rw-r--r--. 1 milias hybrilit     15849 Jul 15 22:24 electronic_properties.py
-rw-r--r--. 1 milias hybrilit      5342 Jul 15 22:22 hydra_ase_intel2026_N1_n05p
-rw-r--r--. 1 milias hybrilit    326579 Jul 15 21:38 Hg_fr_pbesol.upf
-rw-r--r--. 1 milias hybrilit    348124 Jul 15 21:38 Au_fr_pbesol.upf
-rw-r--r--. 1 milias hybrilit      3247 Jul 15 21:38 final_relaxed_structure_15062026.vasp


