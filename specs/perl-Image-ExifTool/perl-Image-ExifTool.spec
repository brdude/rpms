# $Id$
# Authority: dries
# Upstream: Phil Harvey <phil%20at%20owl,phy,queensu,ca>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-ExifTool

Summary: Read and write meta information in images
Name: perl-Image-ExifTool
Version: 6.90
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-ExifTool/

Source: http://search.cpan.org/CPAN/authors/id/E/EX/EXIFTOOL/Image-ExifTool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
ExifTool is a highly customizable Perl script for reading and writing meta
information in images.

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
%doc %{_mandir}/man1/*
%{_bindir}/exiftool
%{perl_vendorlib}/File/RandomAccess.p*
%{perl_vendorlib}/Image/ExifTool.p*
%{perl_vendorlib}/Image/ExifTool/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 6.90-1
- Updated to release 6.90.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 6.76-1
- Updated to release 6.76.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 6.66-1
- Updated to release 6.66.

* Sat Sep 23 2006 Dries Verachtert <dries@ulyssis.org> - 6.42-1
- Updated to release 6.42.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 6.36-1
- Updated to release 6.36.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 6.17-1
- Updated to release 6.17.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 6.00-1
- Updated to release 6.00.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 5.87-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 5.87-1
- Updated to release 5.87.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 5.77-1
- Initial package.
