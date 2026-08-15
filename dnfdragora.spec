# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

Summary:	Graphical frontend for installing and removing software
Name:		dnfdragora
Version:	2.99.5
Release:	1
License:	GPL-2.0-or-later
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdragora
Source0:	%url/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	cmake
BuildOption:	-DENABLE_COMPS:BOOL=OFF
BuildOption:	-DCHECK_RUNTIME_DEPENDENCIES=ON

BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sh)
BuildRequires:	python%{pyver}dist(notify2)
BuildRequires:	python%{pyver}dist(cairosvg)
BuildRequires:	python%{pyver}dist(pystray)
BuildRequires:  python%{pyver}dist(python-manatools)
Requires:	polkit
Requires:	dbus
Requires:	dnf
Requires:	dnf-plugins-core
Requires:	python-dnfdaemon
Requires:	dnf5daemon-client
Requires:	python-yui
Requires:	python-yaml
Requires:	python-dnf
Requires:	python-gi
Requires:	python-hawkey
Requires:	python-sh
Requires:	python-notify2
Requires:	python%{pyver}dist(pystray)
Requires:	python-manatools
# Some people start complains about error during launch due missing some gir/typelibs. This files should be auto-installed via g-ir scanner
# but looks like somethings goes wrong. So to be on safe side, let's pull needed packages manually.
Requires:	typelib(GLib)
Requires:	glib-gir
# FIXME split into qt/ncurses subpackages

# (crazy) FIXME split updater

%description
Graphical frontend for installing and removing software.

%patchlist
# ( crazy)
0001-znver1-support.patch
# patch to enable transaction logs
# enable-log.patch

%package updater
Summary:	Update notifier applet for %{name}
Requires:	%{name} = %{EVRD}
Requires:	typelib(Notify)
Requires:	python-notify2
Requires:	python-pyxdg
Requires:	python-cairosvg
Requires:	python-imaging
Requires:	python%{pyver}dist(pystray)

%description updater
Updating applet for %{name}

%conf -p
sed -i -e 's,/usr/bin/dbus-send,/bin/dbus-send,g' dnfdragora/misc.py

%install -a
sed -i '1s|#!/usr/bin/env python3|#!%{__python3}|' \
	    %{buildroot}%{_bindir}/dnfdragora \
    %{buildroot}%{_bindir}/dnfdragora-updater

for sz in 16x16 32x32 48x48 64x64 128x128 256x256; do
  h=%{buildroot}%{_datadir}/icons/hicolor/$sz/apps
  d=%{buildroot}%{_datadir}/dnfdragora/images/$sz

  ln -sf org.mageia.dnfdragora.png $h/dnfdragora.png

  ln -sf %{_datadir}/icons/hicolor/$sz/apps/org.mageia.dnfdragora.png $d/dnfdragora.png
  ln -sf %{_datadir}/icons/hicolor/$sz/apps/org.mageia.dnfdragora.png $d/dnfdragora-logo.png
done

ln -sf org.mageia.dnfdragora.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/dnfdragora.svg

ln -sf %{_datadir}/icons/hicolor/scalable/apps/org.mageia.dnfdragora.svg \
   %{buildroot}%{_datadir}/dnfdragora/images/dnfdragora.svg
ln -sf %{_datadir}/icons/hicolor/scalable/apps/org.mageia.dnfdragora.svg \
   %{buildroot}%{_datadir}/dnfdragora/images/dnfdragora-logo.svg
ln -sf %{_datadir}/icons/hicolor/128x128/apps/org.mageia.dnfdragora.png \
   %{buildroot}%{_datadir}/dnfdragora/images/dnfdragora.png
ln -sf %{_datadir}/icons/hicolor/128x128/apps/org.mageia.dnfdragora.png \
   %{buildroot}%{_datadir}/dnfdragora/images/dnfdragora-logo.png

%files -f %{name}.lang
%dir %{_sysconfdir}/dnfdragora
%config(noreplace) %{_sysconfdir}/dnfdragora/dnfdragora.yaml
%{_bindir}/dnfdragora
%{py_puresitedir}/dnfdragora
%exclude %{py_puresitedir}/%{name}/updater.py
%{_datadir}/%{name}
%{_metainfodir}/org.mageia.%name.metainfo.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/apps/%name.svg
%{_iconsdir}/hicolor/scalable/apps/org.mageia.%name.svg
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/applications/*%{name}-localinstall.desktop
%doc %{_mandir}/man5/*.5*
%doc %{_mandir}/man8/*.8*

%files updater
%{_bindir}/%{name}-updater
%{_datadir}/applications/*%{name}-updater.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/*%{name}*.desktop
%{py_puresitedir}/%{name}/updater.py
