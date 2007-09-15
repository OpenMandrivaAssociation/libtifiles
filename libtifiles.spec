%define version 0.6.6
%define release %mkrel 1

%define major 0
%define libname %mklibname tifiles %major

Summary:	Library for Ti File Format management
Name:		libtifiles
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Communications
URL:		http://tilp.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/tilp/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}

%description
The TiFiles library is a part of the TiLP project and constitutes
with the other libraries a complete framework for developping
and/or linking TI files oriented applications.

It is a library capable of reading/modifying/writing TI formatted
files and can group/ungroups files, without worrying about different
TI file formats.

It supports all the currently available calculators and their associated
file formats:
- TI8x calculators: TI73, 82, 83, TI83+, 85 and 86 (with 2 sub-classes:
  TI 73/83+ and 85/86).
- TI9x calculators: TI89, 92, 92+ and V200PLT.

%package -n	%{libname}
Summary:	Library for TI File Format management
Group:		Communications
Requires:	%{name} = %{version}

%description -n	%{libname}
The TiFiles library is a part of the TiLP project and constitutes
with the other libraries a complete framework for developping
and/or linking TI files oriented applications.

It is a library capable of reading/modifying/writing TI formatted
files and can group/ungroups files, without worrying about different
TI file formats.

It supports all the currently available calculators and their associated
file formats:
- TI8x calculators: TI73, 82, 83, TI83+, 85 and 86 (with 2 sub-classes:
  TI 73/83+ and 85/86).
- TI9x calculators: TI89, 92, 92+ and V200PLT.


%package -n	%{libname}-devel
Summary:	Development related files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-doc
Provides:	%{name}-doc

%description -n	%{libname}-devel
This package contains headers and other necessary files to develop 
or compile applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --enable-static=yes
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std gnulocaledir=${RPM_BUILD_ROOT}%{_datadir}/locale
rm -rf ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}

%find_lang %{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


