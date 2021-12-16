%global debug_package %{nil}
%define yui_major 15

Summary:	Graphical frontend for installing and removing software
Name:		dnfdragora
Version:	2.1.2
Release:	2
License:	GPLv2+
Group:		System/Configuration
Url:		https://github.com/manatools/dnfdragora
Source0:	https://github.com/manatools/dnfdragora/archive/%{name}-%{version}.tar.gz
# ( crazy)  https://issues.openmandriva.org/show_bug.cgi?id=2422
Patch1:		0001-znver1-support.patch
# patch to enable transaction logs https://issues.openmandriva.org/show_bug.cgi?id=2454  (penguin)
Patch2:		enable-log.patch
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
Requires:	dnf-plugins-core
Requires:	python-dnfdaemon
Requires:	dnfdaemon
Requires:	python-libyui
Requires:	python-yaml
Requires:	python-dnf
Requires:	python-gi
Requires:	python-hawkey
Requires:	python-sh
Requires:	python-notify2
Requires:	python3dist(pystray)
Requires:	python-manatools
# FIXME split into qt/ncurses subpackages
Requires:	%{_lib}yui%{yui_major}-qt
Requires:	%{_lib}yui%{yui_major}-mga-qt
Requires:	%{_lib}yui%{yui_major}-ncurses
Requires:	%{_lib}yui%{yui_major}-mga-ncurses

# (crazy) FIXME split updater

%description
Graphical frontend for installing and removing software.

%package updater
Summary:	Update notifier applet for %{name}
Requires:	%{name} = %{EVRD}
Requires:	libnotify
Requires:	python-notify2
Requires:	python-pyxdg
Requires:	python-cairosvg
Requires:	python-imaging
Requires:	python3dist(pystray)

%description updater
Updating applet for %{name}

%prep
%autosetup -p1
sed -i -e 's,/usr/bin/dbus-send,/bin/dbus-send,g' dnfdragora/misc.py
%cmake -G Ninja \
	-DENABLE_COMPS:BOOL=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}

%check
#make test

%files -f %{name}.lang
%dir %{_sysconfdir}/dnfdragora
%{_sysconfdir}/dnfdragora/dnfdragora.yaml
%{_bindir}/dnfdragora
%{py_puresitedir}/dnfdragora
%exclude %{py_puresitedir}/%{name}/updater.py
%exclude %{py_puresitedir}/%{name}/__pycache__/updater.cpython*.py?
%{_datadir}/appdata/org.mageia.dnfdragora.appdata.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/applications/*%{name}-localinstall.desktop
%doc %{_mandir}/man5/*.5*
%doc %{_mandir}/man8/*.8*

%files updater
%{_bindir}/%{name}-updater
%{_datadir}/applications/*%{name}-updater.desktop
%{_sysconfdir}/xdg/autostart/*%{name}*.desktop
%{py_puresitedir}/%{name}/updater.py
%{py_puresitedir}/%{name}/__pycache__/updater.cpython*.py?
