#
# Conditional build:
%bcond_without	alsa		# don't build ALSA plugin
%bcond_without	arts		# don't build aRts plugin
%bcond_without	nas 		# don't build NAS plugin
%bcond_with	polypaudio	# build Polypaudio plugin (obsoleted by libao-pulse)
%bcond_without	static_libs	# don't build static library
#
Summary:	Cross Platform Audio Output Library
Summary(es.UTF-8):	Biblioteca libao
Summary(pl.UTF-8):	Międzyplatformowa biblioteka do odtwarzania dźwięku
Summary(pt_BR.UTF-8):	Biblioteca libao
Name:		libao
Version:	0.8.6
Release:	4
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
# Source0-md5:	12e136a4c0995068ff134997c84421ed
Patch0:		%{name}-polypaudio-0_8.patch
URL:		http://www.xiph.org/ao/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.0}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.8
BuildRequires:	libtool
%{?with_nas:BuildRequires:	nas-devel}
%{?with_polypaudio:BuildRequires:	polypaudio-devel >= 0.8}
Obsoletes:	libao2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libao is a cross-platform audio library that allows programs to output
audio using a simple API on a wide variety of platforms. It currently
supports: Null output, WAV files, OSS (Open Sound System), ESD (ESounD
or Enlighten Sound Daemon), ALSA (Advanced Linux Sound Architecture),
Solaris (untested), IRIX (untested)

%description -l es.UTF-8
Libaso es un biblioteca de audio que soporta programas com salida de
audio usando una API simplificada en una gran variedad de
arquiteturas. Hoy soporta Null output, WAV files, OSS (Open Sound
System), ESD (ESounD or Enlighten Sound Daemon), ALSA (Advanced Linux
Sound Architecture), Solaris (untested), IRIX (untested).

%description -l pl.UTF-8
Libao jest biblioteką do odtwarzania dźwięku, która ma proste API i jest
dostępna na wielu różnych platformach.  Aktualnie wspiera odtwarzanie na
urządzenie puste (null output), do plików w formacie WAV, do demona ESD
(ESounD tudzież Enlighten Sound Daemon) oraz urządzenia ALSA (Advanced
Linux Sound Architecture), OSS (Open Sound System), Solaris i IRIX.

%description -l pt_BR.UTF-8
Libao é uma biblioteca de audio multi-plataforma que permite programas
para saida de audio usando uma API simples em uma variedade grande de
plataformas. Atualmente suporta Null output, WAV files, OSS (Open
Sound System), ESD (ESounD or Enlighten Sound Daemon), ALSA (Advanced
Linux Sound Architecture), Solaris (untested), IRIX (untested).

%package devel
Summary:	Cross Platform Audio Output Library Development
Summary(pl.UTF-8):	Część dla programistów biblioteki libao
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libao2-devel

%description devel
The libao-devel package contains the header files and documentation
needed to develop applications with libao.

%description devel -l es.UTF-8
Biblioteca y archivos de inclusión.

%description devel -l pl.UTF-8
Pakiet libao-devel zawiera pliki nagłówkowe i dokumentację, potrzebne
do kompilowania aplikacji korzystających z libao.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão.

%package static
Summary:	Cross Platform Autio Output Static Library
Summary(es.UTF-8):	Bibliotecas estáticas
Summary(pl.UTF-8):	Statyczna biblioteka libao
Summary(pt_BR.UTF-8):	Bibliotecas estáticas
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
The libao-static package contains the static libraries of libao.

%description static -l es.UTF-8
Biblioteca de audio Libao.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libao.

%description static -l pt_BR.UTF-8
Biblioteca de audio Libao.

%package alsa
Summary:	Advanced Linux Sound Architecture (ALSA) plugin for libao
Summary(pl.UTF-8):	Wtyczka libao dla Advanced Linux Sound Architecture (ALSA)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description alsa
Advanced Linux Sound Architecture (ALSA) plugin for libao.

%description alsa -l pl.UTF-8
Wtyczka libao dla Advanced Linux Sound Architecture (ALSA).

%package arts
Summary:	Arts plugin for libao
Summary(pl.UTF-8):	Wtyczka arts dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description arts
Arts plugin for libao.

%description arts -l pl.UTF-8
Wtyczka arts dla libao.

%package esd
Summary:	ESD plugin for libao
Summary(pl.UTF-8):	Wtyczka ESD dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description esd
ESD plugin for libao.

%description esd -l pl.UTF-8
Wtyczka esd dla libao.

%package nas
Summary:	Network Audio System (NAS) plugin for libao
Summary(pl.UTF-8):	Wtyczka libao dla Network Audio System (NAS)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description nas
Network Audio System (NAS) plugin for libao.

%description nas -l pl.UTF-8
Wtyczka libao dla Network Audio System (NAS).

%package polyp
Summary:	Polypaudio plugin for libao
Summary(pl.UTF-8):	Wtyczka Polypaudio dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description polyp
Polypaudio plugin for libao.

%description polyp -l pl.UTF-8
Wtyczka Polypaudio dla libao.

%prep
%setup -q
%patch0 -p1

%build
# just AM_PATH_ESD copy
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if !%{with alsa}
	--disable-alsa \
%else
	--enable-alsa \
%endif
%if !%{with arts}
	--disable-arts \
%endif
%if !%{with nas}
	--disable-nas \
%endif
%if !%{with polypaudio}
	--disable-polyp \
%endif
	--%{!?with_static_libs:dis}%{?with_static_libs:en}able-static

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

%if %{with static_libs}
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
