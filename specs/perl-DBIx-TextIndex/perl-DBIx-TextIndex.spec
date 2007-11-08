# $Id$
# Authority: dries
# Upstream: Daniel Koch <dkoch$bizjournals,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-TextIndex

Summary: full-text searching in SQL databases
Name: perl-DBIx-TextIndex
Version: 0.25
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-TextIndex/

Source: http://search.cpan.org/CPAN/authors/id/D/DK/DKOCH/DBIx-TextIndex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
DBIx::TextIndex was developed for doing full-text searches on BLOB
columns stored in a database. Almost any database with BLOB and DBI
support should work with minor adjustments to SQL statements in the
module. MySQL, PostgreSQL, and SQLite are currently supported.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/DBIx/
%{perl_vendorarch}/DBIx/TextIndex.pm
%{perl_vendorarch}/DBIx/TextIndex
%dir %{perl_vendorarch}/auto/DBIx/
%{perl_vendorarch}/auto/DBIx/TextIndex/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
