Name:           zabbix-alertscript-maintenance
Version:        0.1.1
Release:        1%{?dist}
Summary:        Script that allows Zabbix to send a node into maintenance

License:        ASLv2
URL:            https://github.com/gregswift/zabbix-alertscript-maintenance
Source0:        %{name}.tar.gz

BuildArch:      noarch

Requires:       zabbix >= 2.2
Requires:       python-pyzabbix

%description


%prep
%setup -q -n %{name}


%build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc README.md LICENSE
%config(noreplace) %{_sysconfdir}/zabbix/alertscripts/maintmode.conf
%attr(0755,zabbixsrv,zabbixsrv) %{_sharedstatedir}/zabbixsrv/alertscripts/maintenance-mode
%{_datadir}/%{name}/*.xml


%changelog
* Fri May 15 2015 greg5320 <gregswift@gmail.com> - 0.1.1-1
- Add python-pyzabbix dependency

* Mon May 11 2015 greg5320 <gregswift@gmail.com> - 0.1.0-1
- Initial build
