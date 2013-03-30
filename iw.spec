Name:		iw
Summary:	Configuration utility for wireless devices
Version:	3.8
Release:	2
License:	BSD
Group:		System/Base
Source0:	http://wireless.kernel.org/download/iw/iw-%{version}.tar.bz2
URL:		http://linuxwireless.org/en/users/Documentation/iw/
BuildRequires:	pkgconfig(libnl-3.0)

%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written.

%prep
%setup -q

%build
%make

%install
%{makeinstall} \
	PREFIX=%{buildroot} \
	BINDIR=%{buildroot}/sbin \
	MANDIR=%{buildroot}/%{_mandir}

%files
%doc COPYING README
/sbin/iw
%{_mandir}/man8/iw.8.*
