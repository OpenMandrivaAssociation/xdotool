%define name	xdotool
%define version	2.20101012.3049
%define release	%mkrel 1
%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	fake keyboard/mouse input, window management, and more
Group:		Toys
License:	GPL
URL:		http://www.semicomplete.com/projects/xdotool
Source:     http://semicomplete.googlecode.com/files/xdotool-%{version}.tar.gz
BuildRequires:  libx11-devel
BuildRequires:  libxtst-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
Provides:   %{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std \
    PREFIX=%{_prefix} \
    INSTALLMAN=%{_datadir}/man \
    INSTALLLIB=%{_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xdotool
%{_mandir}/man1/xdotool.1*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxdo.so.%{major}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libxdo.so
%{_includedir}/xdo.h
