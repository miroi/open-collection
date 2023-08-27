NWChem on ubuntu-kch
====================


Package installation
--------------------

See https://github.com/nwchemgit/nwchem/releases/tag/v7.0.2-release

milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/buildups_on_servers/ubuntu-kch_194.160.44.72/.curl -LJO https://github.com/nwchemgit/nwchem/releases/download/v7.0.2-release/nwchem-data_7.0.2-1_all.ubuntu_focal.deb
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   648  100   648    0     0   1424      0 --:--:-- --:--:-- --:--:--  1421
100 5980k  100 5980k    0     0  5461k      0  0:00:01  0:00:01 --:--:-- 15.7M
curl: Saved to filename 'nwchem-data_7.0.2-1_all.ubuntu_focal.deb'
milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/buildups_on_servers/ubuntu-kch_194.160.44.72/.curl -LJO https://github.com/nwchemgit/nwchem/releases/download/v7.0.2-release/nwchem_7.0.2-1_amd64.ubuntu_focal.deb
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   645  100   645    0     0   2519      0 --:--:-- --:--:-- --:--:--  2519
100 12.7M  100 12.7M    0     0  9257k      0  0:00:01  0:00:01 --:--:-- 13.9M
curl: Saved to filename 'nwchem_7.0.2-1_amd64.ubuntu_focal.deb'
milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/buildups_on_servers/ubuntu-kch_194.160.44.72/.ls
nwchem_7.0.2-1_amd64.ubuntu_focal.deb  nwchem-data_7.0.2-1_all.ubuntu_focal.deb  readme.rst
milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/buildups_on_servers/ubuntu-kch_194.160.44.72/.sudo dpkg -i nwchem*7.0.2*focal*.deb
(Reading database ... 365318 files and directories currently installed.)
Preparing to unpack nwchem_7.0.2-1_amd64.ubuntu_focal.deb ...
Unpacking nwchem (7.0.2-1) over (7.0.0-3) ...
Preparing to unpack nwchem-data_7.0.2-1_all.ubuntu_focal.deb ...
Unpacking nwchem-data (7.0.2-1) over (7.0.0-3) ...
Setting up nwchem-data (7.0.2-1) ...
Setting up nwchem (7.0.2-1) ...
Processing triggers for man-db (2.9.1-1) ...


Location
--------
/usr/bin/nwchem .. executable
/usr/share/nwchem/ ... libraries
