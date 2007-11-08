# $Id$
# Authority: dag
# Upstream: DeWitt Clinton <dewitt$unto,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cache-Cache

Summary: Cache-Cache module for perl
Name: perl-Cache-Cache
Version: 1.05
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Cache/

Source: http://www.cpan.org/modules/by-module/Cache/Cache-Cache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 2:5.8.0
Requires: perl >= 2:5.8.0
Requires: perl(Error), perl(Storable), perl(IPC::ShareLite)

%description
The Cache modules are designed to assist a developer in persisting data for a
specified period of time.  Often these modules are used in web applications to
store data locally to save repeated and redundant expensive calls to remote
machines or databases.  People have also been known to use Cache::Cache for
its straightforward interface in sharing data between runs of an application
or invocations of a CGI-style script or simply as an easy to use abstraction
of the filesystem or shared memory.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Cache/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 1.02-3
- Rebuilt for Fedora Core 2.

* Fri Apr  2 2004 Matthias Saou <http://freshrpms.net/> 1.02-2
- Change the explicit package deps to perl package style ones to fix the
  perl-Storable obsoletes problem.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 1.02-1
- Initial RPM release.

