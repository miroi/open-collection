======================
Avogadro2 with flatpak
======================

https://two.avogadro.cc/install/flatpak
https://discuss.avogadro.cc/t/avogadro2-inserting-fragments-window-frozen-wsl/7042/10?u=miroslav_ilias

install flatpak
~~~~~~~~~~~~~~~
sudo apt install flatpak

sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

miroi@MIRO:~/work/software/avogadro2/.sudo flatpak install flathub org.kde.Platform
Looking for matches…
Similar refs found for ‘org.kde.Platform’ in remote ‘flathub’ (system):

   1) runtime/org.kde.Platform/x86_64/5.15-21.08
   2) runtime/org.kde.Platform/x86_64/5.9
   3) runtime/org.kde.Platform/x86_64/5.15-22.08
   4) runtime/org.kde.Platform/x86_64/5.15-23.08
   5) runtime/org.kde.Platform/x86_64/5.15-24.08
   6) runtime/org.kde.Platform/x86_64/5.10
   7) runtime/org.kde.Platform/x86_64/5.11
   8) runtime/org.kde.Platform/x86_64/5.12
   9) runtime/org.kde.Platform/x86_64/5.13
  10) runtime/org.kde.Platform/x86_64/5.14
  11) runtime/org.kde.Platform/x86_64/5.15
  12) runtime/org.kde.Platform/x86_64/6.2
  13) runtime/org.kde.Platform/x86_64/6.3
  14) runtime/org.kde.Platform/x86_64/6.4
  15) runtime/org.kde.Platform/x86_64/6.5
  16) runtime/org.kde.Platform/x86_64/6.6
  17) runtime/org.kde.Platform/x86_64/6.7
  18) runtime/org.kde.Platform/x86_64/6.8
  19) runtime/org.kde.Platform/x86_64/6.9

Which do you want to use (0 to abort)? [0-19]: 18

        ID                                             Branch                Op            Remote             Download
 1. [✓] org.freedesktop.Platform.GL.default            24.08                 i             flathub            154.9 MB / 155.4 MB
 2. [✓] org.freedesktop.Platform.GL.default            24.08extra            i             flathub             23.7 MB / 155.4 MB
 3. [✓] org.freedesktop.Platform.openh264              2.5.1                 i             flathub            913.7 kB / 971.4 kB
 4. [✓] org.kde.KStyle.Adwaita                         6.8                   i             flathub              8.2 MB / 8.2 MB
 5. [✓] org.kde.Platform.Locale                        6.8                   i             flathub            195.3 MB / 402.5 MB
 6. [✓] org.kde.Platform                               6.8                   i             flathub            310.5 MB / 384.9 MB

Installation complete.

miroi@MIRO:~/work/software/avogadro2/.flatpak run org.kde.Platform
[📦 org.kde.Platform ~]$
[📦 org.kde.Platform ~]$
exit

miroi@MIRO:~/work/software/avogadro2/.sudo flatpak install org.openchemistry.Avogadro2//beta
Looking for matches…

org.openchemistry.Avogadro2 permissions:
    ipc     network     fallback-x11     wayland     x11     dri     file access [1]     dbus access [2]

    [1] xdg-config/kdeglobals:ro
    [2] com.canonical.AppMenu.Registrar, org.kde.KGlobalSettings, org.kde.kconfig.notify, org.kde.kdeconnect


        ID                                    Branch           Op           Remote                 Download
 1. [✓] org.openchemistry.Avogadro2           beta             i            flathub-beta           79.6 MB / 87.3 MB

Installation complete.
miroi@MIRO:~/work/software/avogadro2/.



