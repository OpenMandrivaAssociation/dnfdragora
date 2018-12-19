%define yui_major 8

Summary:	Graphical frontend for installing and removing software
Name:		dnfdragora
Version:	1.1.0
Release:	3
License:	GPLv2+
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdragora
Source0:	https://github.com/manatools/dnfdragora/archive/%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(python)
Requires:	polkit
Requires:	dbus
Requires:	dnf
Requires:	%{_lib}yui%{yui_major}-ncurses
Requires:	%{_lib}yui%{yui_major}-mga-ncurses
Requires:	python-dnfdaemon dnfdaemon
Requires:	python-libyui
Recommends:	%{_lib}yui%{yui_major}-qt
Recommends:	%{_lib}yui%{yui_major}-mga-qt

%description
Graphical frontend for installing and removing software

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
