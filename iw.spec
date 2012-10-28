Name:		iw
Summary:	Configuration utility for wireless devices
Version:	3.7
Release:	1
License:	BSD
Group:		System/Base
URL:		http://linuxwireless.org/en/users/Documentation/iw/
Source0:	http://wireless.kernel.org/download/iw/iw-%{version}.tar.bz2
BuildRequires:	libnl-devel

%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written.

%prep
%setup -q

%build
%make

%install
%makeinstall \
	PREFIX=%{buildroot} \
	BINDIR=%{buildroot}/sbin \
	MANDIR=%{buildroot}/%{_mandir}

%files
%doc COPYING README
/sbin/iw
%{_mandir}/man8/iw.8.*
