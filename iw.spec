%define ver 0.9.8

Name: iw
Summary: Configuration utility for wireless devices
Version: %ver
Release: %mkrel 1
License: BSD
Group: System/Base
Source0: iw-%{ver}.tar.bz2
URL: http://linuxwireless.org/en/users/Documentation/iw/
#Requires: libnl1
BuildRequires: libnl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%{makeinstall} \
	PREFIX=%{buildroot} \
	BINDIR=%{buildroot}/sbin \
	MANDIR=%{buildroot}/%{_mandir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/sbin/iw
%{_mandir}/man8/iw.8.lzma
%doc COPYING README
