%define yui_major 8

Summary:	Graphical frontend for installing and removing software
Name:		dnfdragora
Version:	1.1.1
Release:	3
License:	GPLv2+
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdragora
Source0:	https://github.com/manatools/dnfdragora/archive/%{version}.tar.gz
Patch0:		dnfdragora-icon.patch
# ( crazy)  https://issues.openmandriva.org/show_bug.cgi?id=2422
Patch1:		0001-znver1-support.patch
# From crazy
# https://bugzilla.redhat.com/show_bug.cgi?id=1505587
Patch2:		dnfdragora-workaround-for-crashes.patch
# (bero) Fix armv7hnl the same way as znver1
Patch3:		dnfdragora-1.1.1-armv7hnl.patch
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python-sphinx
BuildRequires:	python-sh
BuildRequires:	python-notify2
Requires:	polkit
Requires:	dbus
Requires:	dnf
Requires:	python-dnfdaemon dnfdaemon
Requires:	python-libyui
Requires:	python-yaml
Requires:	python-dnf
Requires:	python-gi
Requires:	python-hawkey
Requires:	python-sh
Requires:	python-notify2
Requires:	python3dist(pystray)
# FIXME split into qt/ncurses subpackages
Requires:	%{_lib}yui%{yui_major}-qt
Requires:	%{_lib}yui%{yui_major}-mga-qt
Requires:	%{_lib}yui%{yui_major}-ncurses
Requires:	%{_lib}yui%{yui_major}-mga-ncurses

# (crazy) FIXME split updater

%description
Graphical frontend for installing and removing software.

%prep
%autosetup -p1
sed -i -e 's,/usr/bin/dbus-send,/bin/dbus-send,g' dnfdragora/misc.py
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}

%check
#make test

%files -f %{name}.lang
%{_sysconfdir}/dnfdragora/dnfdragora.yaml
%{_sysconfdir}/xdg/autostart/org.mageia.dnfdragora-updater.desktop
%{_bindir}/dnfdragora
%{_bindir}/dnfdragora-updater
%{py_puresitedir}/dnfdragora
%{_datadir}/appdata/org.mageia.dnfdragora.appdata.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/applications/*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*
