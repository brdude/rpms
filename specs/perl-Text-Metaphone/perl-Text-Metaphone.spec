# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Metaphone

Summary: Modern soundex, phonetic encoding of words
Name: perl-Text-Metaphone
Version: 1.96
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Metaphone/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/Text-Metaphone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Metaphone() is a function whereby a string/word is broken down into
a rough approximation of its english phonetic pronunciation.  Very
similar in concept and purpose to soundex, but much more
comprehensive in its approach.

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
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/Metaphone.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/Metaphone/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.96-1
- Initial package.
