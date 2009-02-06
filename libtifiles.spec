%define version 0.6.6
%define release %mkrel 5
%define major 0
%define libname %mklibname tifiles %{major}
%define develname %mklibname -d tifiles

Summary:	Library for Ti File Format management
Name:		libtifiles
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
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

It supports all the currently availablecables calculators and their associated
file formats:
- TI8x calculators: TI73, 82, 83, TI83+, 85 and 86 (with 2 sub-classes:
  TI 73/83+ and 85/86).
- TI9x calculators: TI89, 92, 92+ and V200PLT.

%package        -n %{libname}
Group:          System/Libraries
Summary:        Library for Ti File Format management
Requires:       %{name} = %{version}

%description -n %{libname}
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

%package -n	%{develname}
Summary:	Development related files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-doc
Provides:	%{name}-doc


%description -n	%{develname}
This package contains headers and other necessary files to develop 
or compile applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --enable-static=yes
%make

%install
rm -rf %{buildroot}
%makeinstall_std gnulocaledir=%{buildroot}%{_datadir}/locale
rm -rf %{buildroot}/%{_docdir}/%{name}-%{version}

%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}


%files
%files -f %{name}.lang
%defattr(-,root,root)

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
%{_datadir}/locale/fr/LC_MESSAGES/libtifiles.mo
%doc COPYING


%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
