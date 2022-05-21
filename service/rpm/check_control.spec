%define relabel_files() \
restorecon -R -v /usr/bin; \
restorecon -R -v /usr/lib/systemd/system; \

%define selinux_policyver 3.13.1-266

Name:          check_control
Version:       1.0
Release:       1%{?dist}
Summary:       A service that controls to specific files
Group:         Testing
License:       MIT
URL:           https://github.com/VladGud/OSS
Source0:       %{name}-%{version}.tar.gz
Source1:       %{name}.if
Source2:       %{name}.te
Source3:       %{name}.fc
Requires:      /bin/bash, /bin/rm, /bin/mkdir, /bin/cp, policycoreutils, policycoreutils-devel, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils, policycoreutils-devel, /usr/sbin/semodule
Requires(postun): policycoreutils, policycoreutils-devel, /usr/sbin/semodule
BuildArch:     noarch

%description
A package for check_control service. 
Authors: V. Sapegin
MEPhI, Operation Systems Security class, Moscow 2022

%prep
%setup -q
mkdir selinux
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} selinux/

%build

cd selinux/
make -f /usr/share/selinux/devel/Makefile %{name}.pp
cd ..

%install

cd selinux/
install -d %{buildroot}%{_datadir}/selinux/
install -p -m 644 %{name}.pp %{buildroot}%{_datadir}/selinux/%{name}.pp
cd ..

mkdir -p %{buildroot}/opt/check_control/
mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}%{_mandir}/man7/

install -m 755 check_control %{buildroot}/opt/check_control/
install -m 644 check_control.conf %{buildroot}/etc
install -m 644 check_control.service %{buildroot}/etc/systemd/system/
install -m 644 check_control.7.gz %{buildroot}%{_mandir}/man7/

%post
%{_sbindir}/semodule -i %{_datadir}/selinux/%{name}.pp
/sbin/fixfiles -R %{name} restore

%postun
if [ $1 -eq 0 ]; then 
	%{_sbindir}/semodule -n -r %{name}
fi

%files
/opt/check_control/*
/etc/check_control.conf
/etc/systemd/system/check_control.service
%{_mandir}/man7/check_control.7.gz
%attr(0600,root,root) %{_datadir}/selinux/%{name}.pp

%changelog
* Sat May 21 2022 Sapegin
- Added check-control-service
