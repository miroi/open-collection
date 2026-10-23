================
Run via AppImage
================

download
--------
https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-x86_64.AppImage

miroi@MIRO:~/work/software/avogadro2/.mv /mnt/c/Users/miroi/Downloads/Avogadro2-x86_64.AppImage .

miroi@MIRO:~/work/software/avogadro2/.ls -lt Avogadro2-x86_64.AppImage
-rwxrwxrwx 1 miroi miroi 112665792 Oct 23 22:45 Avogadro2-x86_64.AppImage*
miroi@MIRO:~/work/software/avogadro2/.ldd Avogadro2-x86_64.AppImage
        not a dynamic executable


run
---
chmod +x Avogadro2*.AppImage

miroi@MIRO:~/.LIBGL_ALWAYS_SOFTWARE=1 ~/work/software/avogadro2/Avogadro2-x86_64.AppImage
Avogadroapp version:  2.1.0
Avogadrolibs version:  2.1.0
Qt version:  6.8.3
qt.core.qobject.connect: QObject::connect(QObject, Unknown): invalid nullptr parameter
SSL version:  "OpenSSL 3.0.2 15 Mar 2022"
Using locale:  "C"
 registering GPL plugins
"/tmp/.mount_AvogadKFfjnN/usr/bin/obabel"  found:  "/tmp/.mount_AvogadKFfjnN/usr/bin/obabel: Open Babel 3.2.1 -- Oct 23 2026 -- 12:45:35"
RPC server listening on: "/tmp/avogadro"
Open Babel formats ready:  143


