# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

Summary: RPMforge release file and package configuration
Name: rpmforge-release
Version: 0.1
Release: 3
License: GPL
Group: System Environment/Base
URL: http://rpmforge.net/

Source0: mirrors-dag
Source1: RPM-GPG-KEY-rpmforge-dag
Source2: RPM-GPG-KEY-rpmforge-dries
Source3: RPM-GPG-KEY-rpmforge-matthias
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RPMforge.net release file. This package contains apt, yum and smart
configuration for the RPMforge RPM Repository, as well as the public
GPG keys used to sign them.

%prep
%{?el4:name='Red Hat Enterprise'; version='4'; url="redhat/el$version/en"; builder='dag'}
%{?el3:name='Red Hat Enterprise'; version='3'; url="redhat/el$version/en"; builder='dag'}
%{?el2:name='Red Hat Enterprise'; version='2'; url="redhat/el$version/en"; builder='dag'}
%{?fc4:name='Fedora Core'; version='4'; url="dries/fedora/$version"; builder='dries'}
%{?fc3:name='Fedora Core'; version='3'; url="fedora/$version/en"; builder='dag'}
%{?fc2:name='Fedora Core'; version='2'; url="fedora/$version/en"; builder='dag'}
%{?fc1:name='Fedora Core'; version='1'; url="fedora/$version/en"; builder='dag'}
%{?rh9:name='Red Hat'; version='9'; url="redhat/$version/en"; builder='dag'}
%{?rh8:name='Red Hat'; version='8.0'; url="redhat/$version/en"; builder='dag'}
%{?rh7:name='Red Hat'; version='7.3'; url="redhat/$version/en"; builder='dag'}
%{?rh6:name='Red Hat'; version='6.2'; url="redhat/$version/en"; builder='dag'}

%{__cat} <<EOF >rpmforge.apt
# Name: RPMforge RPM Repository for $name $version - %{_arch}
# URL: http://rpmforge.net/
rpm http://apt.sw.be $url/%{_arch} $builder
EOF

%{__cat} <<EOF >rpmforge.smart
# Name: RPMforge RPM Repository for $name $version - %{_arch}
# URL: http://rpmforge.net/
[rpmforge]
name = Extra packages from RPMforge.net for $name $version - %{_arch}
baseurl = http://apt.sw.be/$url/%{_arch}/$builder
type = rpm-md
EOF

%{__cat} <<EOF >rpmforge.yum
# Name: RPMforge RPM Repository for $name $version - %{_arch}
# URL: http://rpmforge.net/
[rpmforge]
name = $name $version - %{_arch} - RPMforge.net
#baseurl = http://apt.sw.be/$url/$basearch/$builder/
mirrorlist = http://apt.sw.be/$url/mirrors-rpmforge
#mirrorlist = file:///etc/yum.repos.d/mirrors-rpmforge
enabled = 1
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-$builder
gpgcheck = 1
EOF

%{__cat} <<EOF >rpmforge.up2date
# Name: RPMforge RPM Repository for $name $version - %{_arch}
# URL: http://rpmforge.net/
#
# Add the following line to /etc/sysconfig/rhn/sources
#
#	yum dag http://apt.sw.be/$url/$ARCH/$builder
EOF

for mirror in $(%{__cat} %{SOURCE0}); do
	echo "$mirror/$url/\$ARCH/$builder"
done >mirrors-rpmforge.yum

%build

%install
%{__rm} -rf %{buildroot}
%{__cp} -a %{SOURCE1} %{SOURCE2} %{SOURCE3} .
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dries
%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias
%{__install} -Dp -m0644 rpmforge.apt %{buildroot}%{_sysconfdir}/apt/sources.list.d/rpmforge.list
%{__install} -Dp -m0644 rpmforge.smart %{buildroot}%{_sysconfdir}/smart/channels/rpmforge.channel
%{__install} -Dp -m0644 rpmforge.up2date %{buildroot}%{_sysconfdir}/sysconfig/rhn/sources.rpmforge.txt
%{__install} -Dp -m0644 rpmforge.yum %{buildroot}%{_sysconfdir}/yum.repos.d/rpmforge.repo
%{__install} -Dp -m0644 mirrors-rpmforge.yum %{buildroot}%{_sysconfdir}/yum.repos.d/mirrors-rpmforge

%clean
%{__rm} -rf %{buildroot}

%post
rpm -q gpg-pubkey-6b8d79e6-3f49313d >/dev/null 2>&1 || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag
rpm -q gpg-pubkey-1aa78495-3eb24301 >/dev/null 2>&1 || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dries
rpm -q gpg-pubkey-e42d547b-3960bdf1 >/dev/null 2>&1 || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias
exit 0

%files
%defattr(-, root, root, 0755)
%doc RPM-GPG-KEY-rpmforge-* rpmforge.* mirrors-rpmforge.yum
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/rpmforge.list
%config(noreplace) %{_sysconfdir}/smart/channels/rpmforge.channel
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmforge.repo
%config %{_sysconfdir}/sysconfig/rhn/sources.rpmforge.txt
%config %{_sysconfdir}/yum.repos.d/mirrors-rpmforge
%pubkey RPM-GPG-KEY-rpmforge-dag
%pubkey RPM-GPG-KEY-rpmforge-dries
%pubkey RPM-GPG-KEY-rpmforge-matthias
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dries
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias

%changelog
* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.1-3
- Improver smart channel.

* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.1-2
- Added mirrors-rpmforge locally.

* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
