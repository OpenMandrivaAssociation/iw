Summary:	Configuration utility for wireless devices
Name:		iw
Version:	5.9
Release:	2
License:	BSD
Group:		System/Base
Url:		http://linuxwireless.org/en/users/Documentation/iw/
Source0:	http://kernel.org/pub/software/network/iw/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libnl-3.0)

%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which use a
mac80211 driver as these are the new drivers being written.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build CC=%{__cc}

%install
%make_install
mkdir -p %{buildroot}/sbin
ln -sf %{_sbindir}/iw %{buildroot}/sbin/iw

%files
%doc COPYING README
/sbin/iw
%{_sbindir}/iw
%{_mandir}/man8/iw.8.*
