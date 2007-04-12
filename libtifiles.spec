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



* Tue Jun 28 2005 Olivier Thauvin <nanardon@mandriva.org> 0.6.5-1mdk
- 0.6.5

* Thu Feb 03 2005 Abel Cheung <deaddog@mandrake.org> 0.6.1-1mdk
- New version
- Split package very finely, solely for ease in upgrade

* Sun May 30 2004 Abel Cheung <deaddog@deaddog.org> 0.5.9-1mdk
- New version

* Sat Oct 11 2003 Abel Cheung <deaddog@deaddog.org> 0.5.7-2mdk
- Add missing locale files

* Sat Oct 11 2003 Abel Cheung <deaddog@deaddog.org> 0.5.7-1mdk
- 0.5.7
- More verbose description
- Merge docs back to devel subpackage since there's not a large amount
  of documentation, and they are API docs (really for development)
- License is LGPL
- Define libtoolize instead of calling bare configure without macros
- Remove unnecessary buildrequires
- Compile static library as well

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.5.1-2mdk
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- quiet setup

* Sat Apr 26 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.5.1-1mdk
- 0.5.1

* Sun Feb 09 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.2-2mdk
- i18n files with lib

* Sat Feb 08 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.2-1mdk
- 0.4.2
- use %%mklibname
- split doc in %%name-doc package

* Fri Dec 27 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.9-2mdk
- rebuild for rpm and glibc

* Sun Nov 24 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.9-1mdk
- 0.3.9

* Tue Sep 03 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.2-2mdk
- fix missing locales

* Tue Sep 03 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.2-1mdk
- 1st mdk package
