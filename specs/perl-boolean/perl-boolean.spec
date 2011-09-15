# $Id$
# Authority: cmr
# Upstream: Ingy döt Net <ingy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name boolean
%define perl_prefix %{buildroot}%{_prefix}

Summary: Boolean support for Perl
Name: perl-%{real_name}
Version: 0.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/boolean/

Source: http://www.cpan.org/authors/id/I/IN/INGY/boolean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.005003
BuildRequires: rpm-macros-rpmforge
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 5.005003

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Most programming languages have a native "Boolean" data type. Perl does
not.  This module provides basic Boolean support, by defining two
special objects: "true" and "false".

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{perl_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/boolean.3pm*
%{perl_vendorlib}/boolean.pm

%changelog
* Thu Sep 15 2011 Todd Lyons <tlyons@ivenue.com> - 0.28-1
- Update to new version.

* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Initial package. (using DAR)
