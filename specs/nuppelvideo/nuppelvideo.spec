# $Id$

# Authority: dag

# Upstream: Roman Hochleitner <roman$mars,tuwien,ac,at>

%define real_name NuppelVideo
%define real_version 0.52a

Summary: NuppelVideo recording tool
Name: nuppelvideo
Version: 0.51.81
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://frost.htu.tuwien.ac.at/~roman/nuppelvideo/

Source: http://frost.htu.tuwien.ac.at/~roman/%{name}/%{real_name}-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
NuppelVideo recording tool.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__perl} -pi -e 's|/usr/local/bin|%{buildroot}%{_bindir}|' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE* README*
%{_bindir}/*

%changelog
* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 0.51.81
- Initial package. (using DAR)
