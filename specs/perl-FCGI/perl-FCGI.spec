# $Id$
# Authority: dries
# Upstream: Sven Verdoolaege <skimo$kotnet,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FCGI

Summary: Fast CGI module
Name: perl-FCGI
Version: 0.67
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI/

Source: http://www.cpan.org/modules/by-module/FCGI/FCGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a Fast CGI module for perl. It's based on the FCGI module
that comes with Open Market's FastCGI Developer's Kit, but does
not require you to recompile perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/FCGI/.packlist
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.TERMS README
%{_mandir}/man3/*.3pm*
%{perl_vendorarch}/FCGI.pm
%{perl_vendorarch}/auto/FCGI/

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Initial package.
