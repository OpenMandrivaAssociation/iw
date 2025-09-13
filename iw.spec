%global optflags %{optflags} -Oz
%global build_ldflags %{build_ldflags} -z nostart-stop-gc

Summary:	Configuration utility for wireless devices
Name:		iw
Version:	6.17
Release:	1
License:	BSD
Group:		System/Base
Url:		https://linuxwireless.org/en/users/Documentation/iw/
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
%make_build CC=%{__cc} SBINDIR=%{_sbindir}

%install
%make_install SBINDIR=%{_sbindir}

%files
%doc COPYING README
%{_sbindir}/iw
%doc %{_mandir}/man8/iw.8*
