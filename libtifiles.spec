%define oname libtifiles2
%define major 6
%define libname %mklibname tifiles %{major}
%define develname %mklibname tifiles -d

Summary:	Library for Ti File Format management
Name:		libtifiles
Version:	1.1.3
Release:	%mkrel 1
License:	LGPLv2+
Group:		Communications
URL:		http://tilp.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2
BuildRequires:	glib2-devel
BuildRequires:	ticonv-devel = 1.1.1
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
%setup -q -n %{oname}-%{version}


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


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.1-3mdv2010.0
+ Revision: 439482
- rebuild

* Sat Feb 21 2009 Zombie Ryushu <ryushu@mandriva.org> 1.1.1-2mdv2009.1
+ Revision: 343651
- Fix unneeded file
- Fix circular requirement
- Fix circular requirement

* Fri Feb 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.1-1mdv2009.1
+ Revision: 343372
- correct libification
- add missing buildrequires on bison and zlib-devel
- fix libification
- spec file clean

  + Zombie Ryushu <ryushu@mandriva.org>
    - Work in progress

* Wed Feb 11 2009 Funda Wang <fundawang@mandriva.org> 0.6.6-6mdv2009.1
+ Revision: 339583
- move mo into main package rather than libpackage

  + Zombie Ryushu <ryushu@mandriva.org>
    - Re-libify
    - Re-libify

* Thu Feb 05 2009 Zombie Ryushu <ryushu@mandriva.org> 0.6.6-5mdv2009.1
+ Revision: 337984
- Fix Redundancies
- Fix BuildRoot Tags
- Fix BuildRoot Tags

* Sun Jul 27 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.6-5mdv2009.0
+ Revision: 250611
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 25 2008 Emmanuel Andry <eandry@mandriva.org> 0.6.6-3mdv2008.1
+ Revision: 189889
- Fix lib group

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Funda Wang <fundawang@mandriva.org> 0.6.6-2mdv2008.1
+ Revision: 116814
- New license policy

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill changelog left by repsys


* Fri Jul 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-07 23:24:25 (38510)
- 0.6.6

* Fri Jul 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-07 23:18:39 (38508)
- import libtifiles

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

