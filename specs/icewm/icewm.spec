# $Id$
# Authority: dag
# Upstream: <icewm-devel$lists,sourceforge,net>

### FIXME: Building icewm adds build env. stuff inside /usr/share/icewm/menu (Jonathan Underwood)

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_gnome2 1}
%{?el2:%define _without_gnome2 1}
%{?rh6:%define _without_gnome2 1}

Summary: Fast and small X11 window manager
Name: icewm
Version: 1.2.20
Release: 1
License: LGPL
Group: User Interface/Desktops
URL: http://www.icewm.org/

Source: http://dl.sf.net/sourceforge/icewm/icewm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake, libtool
BuildRequires: XFree86-devel, XFree86-font-utils
BuildRequires: imlib-devel, libpng-devel, kdelibs
%{!?_without_gnome2:BuildRequires: gnome-desktop-devel}
Obsoletes: icewm-common <= %{version}
Obsoletes: icewm-l10n <= %{version}
Obsoletes: icewm-menu-gnome2 <= %{version}
Obsoletes: icewm-themes <= %{version}

%description
A lightweight window manager for the X Window System. Optimized for
"feel" and speed, not looks. Features multiple workspaces, opaque
move/resize, task bar, window list, clock, mailbox, CPU, Network, APM
status. 

%prep
%setup

%build
%configure \
   --enable-gradients \
   --enable-shaped-decorations \
   --with-docdir="%{_docdir}" \
%{!?_without_gnome2:--enable-menus-gnome2}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/icewm/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING README doc/*.html doc/icewm.sgml
%config %{_datadir}/icewm/keys
%config %{_datadir}/icewm/menu
%config %{_datadir}/icewm/preferences
%config %{_datadir}/icewm/toolbar
%config %{_datadir}/icewm/winoptions
%config(noreplace) %{_sysconfdir}/icewm/
%{_bindir}/ice*
%{_datadir}/icewm/

%changelog
* Tue Jan 11 2005 Dag Wieers <dag@wieers.com> - 1.2.20-1
- Updated to release 1.2.20.

* Thu Jan 06 2005 Dag Wieers <dag@wieers.com> - 1.2.19-1
- Updated to release 1.2.19.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 1.2.16-1
- Initial package. (using DAR)
