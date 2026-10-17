====================
Elk in conda-channel
====================

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/elk-ase/buildup_on_servers/wsl2/.conda search elk
2 channel Terms of Service accepted
Loading channels: done
# Name                       Version           Build  Channel
elk                           10.2.4 pl5321h3a7a38a_0  conda-forge
elk                           10.2.4 pl5321h3a7a38a_1  conda-forge


installation
-------------
(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/elk-ase/buildup_on_servers/wsl2/.conda install -c conda-forge elk
2 channel Terms of Service accepted
Retrieving notices: done
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - package elk-10.2.4-pl5321h3a7a38a_0 requires libxc >=6.2.2,<7.0a0 cpu_*, but none of the providers can be installed

Could not solve for environment specs
The following packages are incompatible
├─ elk =* * is installable and it requires
│  └─ libxc >=6.2.2,<7.0a0 cpu_*, which can be installed;
└─ libxc =7.1.2 * is not installable because it conflicts with any installable versions previously reported.

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/elk-ase/buildup_on_servers/wsl2/.


fixed installation
------------------

(mace_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/elk-ase/buildup_on_servers/wsl2/.conda create -n elk_env -c conda-forge elk
2 channel Terms of Service accepted
Retrieving notices: done
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/miroi/miniconda3/envs/elk_env

  added / updated specs:
    - elk


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    elk-10.2.4                 | pl5321h3a7a38a_1         1.3 MB  conda-forge
    libblas-3.11.0             | 11_h4a7cf45_openblas          18 KB  conda-forge
    libgcc-16.2.0              |       ha9f2e26_7         1.0 MB  conda-forge
    libgfortran-16.2.0         |       h69a702a_7          28 KB  conda-forge
    libgfortran5-16.2.0        |       h6b99dfc_7         2.4 MB  conda-forge
    libgomp-16.2.0             |       he0feb66_7         626 KB  conda-forge
    liblapack-3.11.0           |11_h47877c9_openblas          18 KB  conda-forge
    libopenblas-0.3.34         |pthreads_hf13c14d_2         6.5 MB  conda-forge
    libstdcxx-16.2.0           |       h934c35e_7         6.3 MB  conda-forge
    libxc-6.2.2                |   cpu_h5ef0af7_6          77 KB  conda-forge
    libxc-c-6.2.2              |   cpu_h20a523f_6        54.5 MB  conda-forge
    perl-5.32.1                |10_h7cc23a3_perl5        12.9 MB  conda-forge
    ------------------------------------------------------------
                                           Total:        85.6 MB

The following NEW packages will be INSTALLED:

  _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-20_gnu
  elk                conda-forge/linux-64::elk-10.2.4-pl5321h3a7a38a_1
  fftw               conda-forge/linux-64::fftw-3.3.11-nompi_h3b011a4_100
  libblas            conda-forge/linux-64::libblas-3.11.0-11_h4a7cf45_openblas
  libgcc             conda-forge/linux-64::libgcc-16.2.0-ha9f2e26_7
  libgfortran        conda-forge/linux-64::libgfortran-16.2.0-h69a702a_7
  libgfortran5       conda-forge/linux-64::libgfortran5-16.2.0-h6b99dfc_7
  libgomp            conda-forge/linux-64::libgomp-16.2.0-he0feb66_7
  liblapack          conda-forge/linux-64::liblapack-3.11.0-11_h47877c9_openblas
  libopenblas        conda-forge/linux-64::libopenblas-0.3.34-pthreads_hf13c14d_2
  libstdcxx          conda-forge/linux-64::libstdcxx-16.2.0-h934c35e_7
  libxc              conda-forge/linux-64::libxc-6.2.2-cpu_h5ef0af7_6
  libxc-c            conda-forge/linux-64::libxc-c-6.2.2-cpu_h20a523f_6
  libxcrypt          conda-forge/linux-64::libxcrypt-4.4.38-h280c20c_0
  perl               conda-forge/linux-64::perl-5.32.1-10_h7cc23a3_perl5


Proceed ([y]/n)?


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate elk_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate


Channel "defaults" has the following notices:
  [warning] -- Wed Sep 30 00:00:00 2026
  Anaconda will stop building new Python 3.10 packages on the main channel after October 31, 2026. Existing Python 3.10 packages will stay available but will no longer get new builds or security fixes. We recommend upgrading to Python 3.11 or later. Details: https://www.anaconda.com/docs/reference/policies-practices/python-version-support?utm_source=channel_notices

  [info] -- Thu Aug  6 00:00:00 2026
  main-x (Anaconda's new authenticated channel) is now generally available, with thousands of additional packages from our secure supply chain. Get started at: https://anaconda.com/docs/getting-started/main-x?utm_source=channel_notices


Elk is OpenMP, which is OK for single node with multiple CPUs

(elk_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/elk-ase/buildup_on_servers/wsl2/.which elk
/home/miroi/miniconda3/envs/elk_env/bin/elk
(elk_env) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/elk-ase/buildup_on_servers/wsl2/.ldd /home/miroi/miniconda3/envs/elk_env/bin/elk
        linux-vdso.so.1 (0x000073f7bc3e6000)
        libblas.so.3 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/libblas.so.3 (0x000073f7b9998000)
        libfftw3.so.3 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/libfftw3.so.3 (0x000073f7b9600000)
        libfftw3f.so.3 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/libfftw3f.so.3 (0x000073f7b9200000)
        libgfortran.so.5 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/libgfortran.so.5 (0x000073f7b8e00000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000073f7b98af000)
        libgomp.so.1 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/libgomp.so.1 (0x000073f7bc366000)
        libgcc_s.so.1 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/libgcc_s.so.1 (0x000073f7b9881000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000073f7b8a00000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x000073f7bc361000)
        /lib64/ld-linux-x86-64.so.2 (0x000073f7bc3e8000)
        libquadmath.so.0 => /home/miroi/miniconda3/envs/elk_env/bin/../lib/./libquadmath.so.0 (0x000073f7b95b7000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x000073f7bc35a000)
