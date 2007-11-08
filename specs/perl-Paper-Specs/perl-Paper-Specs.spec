# $Id$
# Authority: dries
# Upstream: Jon Allen <perl$jonallen,info>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Paper-Specs

Summary: Specifications of paper stock, labels and other print media
Name: perl-Paper-Specs
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Paper-Specs/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JONALLEN/Paper-Specs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A module to provide general purpose access to specifications on paper stock, labels and other
well known print media.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Paper/Specs.pm
%{perl_vendorlib}/Paper/Specs/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.

