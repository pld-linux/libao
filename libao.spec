Summary:	Cross Platform Audio Output Library
Name:		libao
Version:	1.0.0_cvs2000.10.29
Release:	1
Group:		Libraries/Multimedia
Group(pl):	Biblioteki/Multimedia
Copyright:	GPL
URL:		http://www.xiph.org/
Vendor:		Xiphophorus <team@xiph.org>
Source:		ftp://www.xiph.org/ogg/vorbis/download/vorbis_nightly_cvs.tgz
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libao is a cross platform audio output library.  It currently supports
ESD, OSS, Solaris, and IRIX.

%package devel
Summary: 	Cross Platform Audio Output Library Development
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libao-devel package contains the header files and documentation
needed to develop applications with libao.

%package static
Summary:	Cross Platform Autio Output Library Development
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The libao-static package contains the static libraries of libao.

%prep
%setup -q -n ao
%patch0 -p1

%build
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%{_prefix}
else
  CFLAGS="$RPM_OPT_FLAGS" %configure --prefix=%{_prefix}
fi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644,root,root,755)
%doc AUTHORS
%doc CHANGES
%doc COPYING
%doc README
%attr(755,root,root) %{_libdir}/libao.so*
%attr(755,root,root) %{_libdir}/libao.la

%files devel
%defattr(644,root,root,755)
%doc doc/index.html
%{_includedir}/ao/ao.h
%{_includedir}/ao/os_types.h

%files static
%attr(644,root,root) %{_libdir}/*.a

%clean 
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
