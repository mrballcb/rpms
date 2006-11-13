# $Id$
# Authority: dries
# Upstream: <scandum$hotmail,com>

Summary: Console MUD client
Name: tintin
Version: 1.96.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://tintin.sourceforge.net/

Source: http://dl.sf.net/tintin/tintin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel

%description
TinTin++ is a MUD client that runs in console mode. A MUD is a
text based multi user dungeon.

%prep
%setup -n tt
%{__perl} -pi -e "s| /usr/bin| %{buildroot}%{_bindir}|g;" src/Makefile*

%build
cd src
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%{__install} -d %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS FAQ INSTALL README TODO
%{_bindir}/tt++

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.96.3-1
- Updated to release 1.96.3.

* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.96.1-1
- Updated to release 1.96.1.

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.9-1
- Updated to release 1.95.9.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.8-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.8-1
- Updated to release 1.95.8.

* Wed Jan  11 2006 Dries Verachtert <dries@ulyssis.org> - 1.95.7-1
- Updated to release 1.95.7.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.95.6-1
- Initial package.
