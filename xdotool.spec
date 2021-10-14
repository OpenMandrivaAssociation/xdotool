%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define _empty_manifest_terminate_build 0

Name:		xdotool
Version:	3.20210903.1
Release:	1
Summary:	fake keyboard/mouse input, window management, and more
Group:		Toys
License:	GPL
URL:		http://www.semicomplete.com/projects/xdotool
Source:		https://github.com/jordansissel/xdotool/archive/master/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xkbcommon)

%description
This tool lets you simulate keyboard input and mouse activity, move and resize
windows, etc. It does this using X11's XTEST extension and other Xlib
functions.

Additionally, you can search for windows and move, resize, hide, and modify
window properties like the title. If your window manager supports it, you can
use xdotool to switch desktops, move windows between desktops, and change the
number of desktops. 

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains libraries for %{name}.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{optflags}"

%install
%make_install \
    PREFIX=%{_prefix} \
    INSTALLMAN=%{_datadir}/man \
    INSTALLLIB=%{_libdir}

%files
%{_bindir}/xdotool
%{_mandir}/man1/xdotool.1*

%files -n %{libname}
%{_libdir}/libxdo.so.%{major}

%files -n %{develname}
%{_libdir}/libxdo.so
%{_includedir}/xdo.h
