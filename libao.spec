#
# Conditional build:
%bcond_without	alsa		# don't build ALSA plugin
%bcond_without	arts		# don't build aRts plugin
%bcond_without	nas 		# don't build NAS plugin
%bcond_without	polypaudio	# don't build Polypaudio plugin
%bcond_without	static		# don't build static library
#
Summary:	Cross Platform Audio Output Library
Summary(es):	Biblioteca libao
Summary(pl):	Miêdzyplatformowa biblioteka do odtwarzania d¼wiêku
Summary(pt_BR):	Biblioteca libao
Name:		libao
Version:	0.8.6
Release:	1
Epoch:		1
License:	GPL v2+
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
# Source0-md5:	12e136a4c0995068ff134997c84421ed
URL:		http://www.xiph.org/ao/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.0}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.8
BuildRequires:	libtool
%{?with_nas:BuildRequires:	nas-devel}
%{?with_polypaudio:BuildRequires:	polypaudio-devel >= 0.6}
Obsoletes:	libao2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libao is a cross-platform audio library that allows programs to output
audio using a simple API on a wide variety of platforms. It currently
supports: Null output, WAV files, OSS (Open Sound System), ESD (ESounD
or Enlighten Sound Daemon), ALSA (Advanced Linux Sound Architecture),
Solaris (untested), IRIX (untested)

%description -l es
Libaso es un biblioteca de audio que soporta programas com salida de
audio usando una API simplificada en una gran variedad de
arquiteturas. Hoy soporta Null output, WAV files, OSS (Open Sound
System), ESD (ESounD or Enlighten Sound Daemon), ALSA (Advanced Linux
Sound Architecture), Solaris (untested), IRIX (untested).

%description -l pl
Libao jest bibliotek± do odtwarzania d¼wiêku, która ma proste API i jest
dostêpna na wielu ró¿nych platformach.  Aktualnie wspiera odtwarzanie na
urz±dzenie puste (null output), do plików w formacie WAV, do demona ESD
(ESounD tudzie¿ Enlighten Sound Daemon) oraz urz±dzenia ALSA (Advanced
Linux Sound Architecture), OSS (Open Sound System), Solaris i IRIX.

%description -l pt_BR
Libao é uma biblioteca de audio multi-plataforma que permite programas
para saida de audio usando uma API simples em uma variedade grande de
plataformas. Atualmente suporta Null output, WAV files, OSS (Open
Sound System), ESD (ESounD or Enlighten Sound Daemon), ALSA (Advanced
Linux Sound Architecture), Solaris (untested), IRIX (untested).

%package devel
Summary:	Cross Platform Audio Output Library Development
Summary(pl):	Czê¶æ dla programistów biblioteki libao
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libao2-devel

%description devel
The libao-devel package contains the header files and documentation
needed to develop applications with libao.

%description devel -l es
Biblioteca y archivos de inclusión.

%description devel -l pl
Pakiet libao-devel zawiera pliki nag³ówkowe i dokumentacjê, potrzebne
do kompilowania aplikacji korzystaj±cych z libao.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão.

%package static
Summary:	Cross Platform Autio Output Static Library
Summary(es):	Bibliotecas estáticas
Summary(pl):	Statyczna biblioteka libao
Summary(pt_BR):	Bibliotecas estáticas
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
The libao-static package contains the static libraries of libao.

%description static -l es
Biblioteca de audio Libao.

%description static -l pl
Statyczna wersja biblioteki libao.

%description static -l pt_BR
Biblioteca de audio Libao.

%package alsa
Summary:	Advanced Linux Sound Architecture (ALSA) plugin for libao
Summary(pl):	Wtyczka libao dla Advanced Linux Sound Architecture (ALSA)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description alsa
Advanced Linux Sound Architecture (ALSA) plugin for libao.

%description alsa -l pl
Wtyczka libao dla Advanced Linux Sound Architecture (ALSA).

%package arts
Summary:	Arts plugin for libao
Summary(pl):	Wtyczka arts dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description arts
Arts plugin for libao.

%description arts -l pl
Wtyczka arts dla libao.

%package esd
Summary:	ESD plugin for libao
Summary(pl):	Wtyczka ESD dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description esd
ESD plugin for libao.

%description esd -l pl
Wtyczka esd dla libao.

%package nas
Summary:	Network Audio System (NAS) plugin for libao
Summary(pl):	Wtyczka libao dla Network Audio System (NAS)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description nas
Network Audio System (NAS) plugin for libao.

%description nas -l pl
Wtyczka libao dla Network Audio System (NAS).

%package polyp
Summary:	Polypaudio plugin for libao
Summary(pl):	Wtyczka Polypaudio dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description polyp
Polypaudio plugin for libao.

%description polyp -l pl
Wtyczka Polypaudio dla libao.

%prep
%setup -q

%build
# just AM_PATH_ESD copy
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if %{without alsa}
	--disable-alsa \
%else
	--enable-alsa \
%endif
%if %{without arts}
	--disable-arts \
%endif	
%if %{without nas}
	--disable-nas \
%endif
%if %{without polypaudio}
	--disable-polyp \
%endif
	--%{!?with_static:dis}%{?with_static:en}able-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/ao/plugins-2/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README TODO
%attr(755,root,root) %{_libdir}/libao.so.*.*.*
%dir %{_libdir}/ao
%dir %{_libdir}/ao/plugins-2
%attr(755,root,root) %{_libdir}/ao/plugins-2/liboss.so
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc doc/*{html,css,c}
%attr(755,root,root) %{_libdir}/libao.so
%{_libdir}/libao.la
%{_includedir}/ao
%{_aclocaldir}/ao.m4
%{_pkgconfigdir}/*.pc

%if %{with static}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libalsa*.so
%endif

%if %{with arts} 
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libarts.so
%endif

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libesd.so

%if %{with nas}
%files nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libnas.so
%endif 

%if %{with polypaudio}
%files polyp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libpolyp.so
%endif 
