# $Id$
# Authority: dag
# Upstream: 

Summary: Quick network topology scanner
Name: nttlscan
Version: 0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.honeyd.org/

Source: http://www.honeyd.org/data/nttlscan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, libdnet, libevent-devel 

%description
Nttlscan is a quick network topology scanner and functions as a highly
parallel traceroute. It randomly picks destination IP addresses and
sends TCP or UDP probes. Returing ICMP messages are interpreted to
reconstruct the route that packets take to their respective destination.
Nttlscan can be used to construct virtual routing topologies for Honeyd.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/nttlscan.1*
%{_bindir}/nttlscan

%changelog
* Fri Sep 03 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Added missing BuildRequires. (Robert Hardy)

* Sat Jul 10 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
