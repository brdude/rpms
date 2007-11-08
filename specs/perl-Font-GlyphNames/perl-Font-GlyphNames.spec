# $Id$
# Authority: dries
# Upstream: Father Chrysostomos <$_%20=%20'spro%5e%5e*%25*%5e6ut%23$&$%25*c%3e%23!%5e!%23&!pan,org'%3b%20y/a-z,$//cd%3b%20print>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-GlyphNames

Summary: Convert between glyph names and characters
Name: perl-Font-GlyphNames
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-GlyphNames/

Source: http://search.cpan.org//CPAN/authors/id/S/SP/SPROUT/Font-GlyphNames-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Convert between glyph names and characters.

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
%doc %{_mandir}/man3/Font::GlyphNames*
%{perl_vendorlib}/Font/GlyphNames.pm
%{perl_vendorlib}/Font/GlyphNames/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
