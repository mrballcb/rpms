%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MongoDBx-Class
%define perl_prefix %{buildroot}%{_prefix}

Summary: flexible object relational mapper (ORM) for MongoDB databases
Name: perl-%{real_name}
Version: 0.91
Release: 1%{?dist}
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/~idoperel/%{real_name}-%{version}/

Source0: http://search.cpan.org/CPAN/authors/id/I/ID/IDOPEREL/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl
Requires: perl(Moose)
Requires: perl(Carp)
Requires: perl(DateTime::Format::W3CDTF)
Requires: perl(Module::Load)
Requires: perl(Module::Pluggable)
Requires: perl(MongoDB) >= 0.40
Requires: perl(MongoDB::Collection)
Requires: perl(MongoDB::Connection)
Requires: perl(MongoDB::Cursor)
Requires: perl(MongoDB::Database)
Requires: perl(Moose::Exporter)
Requires: perl(Moose::Role)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(Try::Tiny)
Requires: perl(namespace::autoclean)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
MongoDBx::Class is a flexible object relational mapper (ORM) for MongoDB
databases. Given a schema-like collection of document classes,
MongoDBx::Class expands MongoDB objects (hash-refs in Perl) from the
database into objects of those document classes, and collapses such
objects back to the database.

MongoDBx::Class takes advantage of the fact that Perl's MongoDB driver
is Moose-based to extend and tweak the driver's behavior, instead of
wrapping it. This means MongoDBx::Class does not define its own syntax,
so you simply use it exactly as you would the MongoDB driver directly.
That said, MongoDBx::Class adds some sugar that enhances and simplifies
the syntax unobtrusively (either use it or don't).

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX="%{perl_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} pure_install
find $RPM_BUILD_ROOT -type f -name .packlist -exec %{__rm} -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Changes README
%{perl_vendorlib}/MongoDBx/
%{_mandir}/man3/*.3*

%changelog
* Thu Sep 15 2011 Todd Lyons <tlyons@ivenue.com> - 0:0.91-1iv
- Initial package.
