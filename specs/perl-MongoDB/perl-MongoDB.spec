%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MongoDB
%define perl_prefix %{buildroot}%{_prefix}

Summary: Perl driver for MongoDB, a document-oriented database
Name: perl-%{real_name}
Version: 0.44
Release: 1%{?dist}
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/~kristina/%{real_name}-%{version}/

Source0: http://search.cpan.org/CPAN/authors/id/K/KR/KRISTINA/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 5.8.7
Requires: perl(Any::Moose)
Requires: perl(Class::Method::Modifiers)
Requires: perl(DateTime)
Requires: perl(Digest::MD5)
Requires: perl(Tie::IxHash)
Requires: perl(XSLoader)
Requires: perl(boolean)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This is the Perl driver for MongoDB, a document-oriented database.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX="%{perl_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} pure_install
find $RPM_BUILD_ROOT -type f -name .packlist -exec %{__rm} -f {} ';'
find $RPM_BUILD_ROOT -type f -name *.bs -exec %{__rm} -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Changes README
%{perl_vendorarch}/MongoDB/
%{perl_vendorarch}/MongoDB.pm
%{perl_vendorarch}/auto/MongoDB/
%{_mandir}/man3/*.3*

%changelog
* Thu Sep 15 2011 Todd Lyons <tlyons@ivenue.com> - 0:0.44-1iv
- Initial package.
