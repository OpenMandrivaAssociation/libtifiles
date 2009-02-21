%define oname libtifiles2
%define major 5
%define libname %mklibname tifiles %{major}
%define develname %mklibname tifiles -d

Summary:	Library for Ti File Format management
Name:		libtifiles
Version:	1.1.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		Communications
URL:		http://tilp.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2
BuildRequires:	glib2-devel
BuildRequires:	ticonv-devel
BuildRequires:	zlib-devel
BuildRequires:	bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n %{libname}
Summary:	Library for Ti File Format management
Group:		System/Libraries
# Requires:	%{name} = %{version}-%{release}

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

%package -n %{develname}
Summary:	Development related files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	tifiles-devel = %{version}-%{release}
Obsoletes:	%{name}-doc < %{version}
Provides:	%{name}-doc

%description -n	%{develname}
This package contains headers and other necessary files to develop 
or compile applications that use %{name}.

%prep
<<<<<<< .mine
%setup -q 
=======
%setup -q -n %{oname}-%{version}
>>>>>>> .r343287

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std gnulocaledir=%{buildroot}%{_datadir}/locale
rm -rf %{buildroot}/%{_docdir}/%{name}-%{version}

%find_lang %{oname}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname} -f %{oname}.lang
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/locale/fr/LC_MESSAGES/libticables2.mo