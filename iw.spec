Summary:	Configuration utility for wireless devices
Name:		iw
Version:	3.15
Release:	1
License:	BSD
Group:		System/Base
Url:		http://linuxwireless.org/en/users/Documentation/iw/
Source0:	http://kernel.org/pub/software/network/iw/iw-%{version}.tar.xz
BuildRequires:	pkgconfig(libnl-3.0)

%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written.

%prep
%setup -q

%build
%setup_compile_flags
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
