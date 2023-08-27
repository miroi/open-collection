=======================
WebMO on lxg1213.gsi.de
=======================


milias@lxg1213.gsi.de:~/Work/qch/software/webmo/WebMO.install/.perl setup.pl 

WELCOME TO WEBMO BASIC VERSION 20.0.012 SETUP

In this portion of setup, you will be asked a few simple
questions about file locations.  The WebMO files will then
be copied onto this server.  After this is done you will log
into WebMO to finish configuration.
Enter to continue
>==========================================================<

ENTER LICENSE INFORMATION

It is time to enter your WebMO license information.
Please enter your license information exactly as it was
received by you.  If you do not yet have a WebMO license
number, you can obtain one for free at www.webmo.net, or
this script can automatically obtain one for you now.

Have you previously obtained a WebMO license number [y/n]:y
License number: 2007-2505-4283
>==========================================================<

SET UP THE PATH TO PERL

It is time to determine where the Perl interpreters are
on your system.  We recommend selecting Perl 5 if
it is available.

The following Perl installations were detected on your server.
You may choose to use one of these or you may specify another
Perl installation that does not appear on the list.

1)  /usr/bin/perl
2)  /etc/perl
3)  /usr/share/perl
4)  [Select a different Perl]

Please choose which Perl to use by entering a number from 1 to 4.

Your choice [1-4]: 1
>==========================================================<

SET UP WEBSERVER NAME

The script has determined that the webserver name of this computer
to be:

   lxg1213.gsi.de

IMPORTANT: This must represent the correct FULLY QUALIFIED webserver name
(computer.domain.edu) for this computer.

Is this webserver name fully qualified and correct [y/n]:y
>==========================================================<

SET UP HTML DIRECTORY

The script will now create a directory into which the WebMO HTML
files will be copied.  The directory should meet the following
requirements:
  - Directory is in the server's webspace
  - The directory is NOT in a cgi-bin directory
  - You need to have permission to write to this directory
  - The parent of the specified directory must already exist

Example:  /home/milias/public_html/webmo

Directory: /u/milias/web-docs

Please enter the URL corresponding to the specified directory.
Example:  /~milias/webmo

URL: /~milias/webmo
>==========================================================<

SET UP CGI DIRECTORY

The script will now create a directory into which the WebMO cgi
scripts will be copied.  The directory should meet the following
requirements:
  - Directory is in the server's webspace
  - Execution of CGI scripts is permitted in directory
  - You need to have permission to write to this directory
  - The parent of the specified directory must already exist

Example:  /home/milias/public_html/cgi-bin/webmo

Directory: /u/milias/web-docs/cgi-bin/webmo
That directory does not exist.
Create directory [y/n]:y
Unable to create directory: No such file or directory
Directory: /home/milias/public_html/cgi-bin/webmo
That directory does not exist.
Create directory [y/n]:y
Unable to create directory: No such file or directory
Directory: /u/milias/web-docs/cgi-bin/webmo

Please enter the URL corresponding to the specified directory.
Example:  /~milias/cgi-bin/webmo

URL: /~milias/cgi-bin/webmo
>==========================================================<

SET UP USER DIRECTORY

The script will now create a directory that will be used to store
user profiles, passwords, jobs, and other private data.  This directory
should meet the following requirements:
  - Directory is NOT in the server's webspace
  - You need to have permission to write to this directory
  - The parent of the specified directory must already exists

Example:  /u/milias/webmo

Directory: /u/milias/webmo
That directory does not exist.
Create directory [y/n]:y
>==========================================================<

Here are the configuration options that you have chosen
License number:       2007-2505-4283
Path to perl:         /usr/bin/perl
Webserver name:       lxg1213.gsi.de
HTML directory:       /u/milias/web-docs
HTML URL:             /~milias/webmo
CGI script directory: /u/milias/web-docs/cgi-bin/webmo
CGI script URL:       /~milias/cgi-bin/webmo
User files directory: /u/milias/webmo

Continue with installation [y/n]:y
Setting up CGI scripts...finished
Setting up interface files...finished
Setting up HTML source files...finished
Setting up user directory...finished

Setting up system scratch directory...finished
Locating system files...finished
Setting up `ps`...PSCHECK will attempt to determine your `ps` version
PSCHECK successful
finished
Running diagnostic tests...finished
Errors were detected during diagnostic tests; view diagnose.html for details
Do you wish to open this file in your browser now?y
>==========================================================<

FINISH SETUP

The remainder of the WebMO setup will be done through the WebMO
administrative tools.  The administrative tools facilitate configuration
of system preferences, configuration of any packages (GAMESS, Gaussian,
MOPAC, MolPro, NWChem, Firefly, Orca, PQS, PSI4, QChem, TeraChem, Tinker,
Quantum Espresso, VASP, etc.) and adding/editing of users.

Access WebMO with your web browser at the following URL: 
	http://lxg1213.gsi.de/~milias/cgi-bin/webmo/login.cgi

Login as the user 'admin' with a blank password. You will be prompted
to change your password at that time.  After changing the admin password,
you will be prompted to register your copy of WebMO.  You will then be
brought to the administration home page.

Enter to continue
Click on the 'System Manager' and check the location of the scratch
directory, which you may change if desired.  Click 'Return to Admin'
to return to the administration home page.

Click on the 'Interface Manager' and enable the interfaces to any
computational chemistry packages that you have already installed on your
system by clicking the corresponding 'Enable interface' icon.
Configure the interfaces by clicking the 'Edit interface' icon, and make any
neccessary changes in the interface configuration, and then click 'Submit'
to commit the changes and 'Return' to get back to the Interface Manager.
Click 'Return to Admin' to return to the administration home page.

Click on the 'User Manager' and then the 'New User' button to create WebMO
users. Click 'Return to User Manager' to return to the user manager.
Click 'Return to Admin' to return to the administration home page.

Setup is now complete.  Click the 'Logout' button to logout of WebMO.
You may now login as a WebMO user and run a test job.

