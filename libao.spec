#
# Conditional build:
# _without_alsa - without ALSA support
# _without_arts - without aRts support
#
Summary:	Cross Platform Audio Output Library
Summary(es):	Biblioteca libao
Summary(pl):	Miêdzyplatformowa biblioteka do odtwarzania d¼wiêku
Summary(pt_BR):	Biblioteca libao
Name:		libao
Version:	0.8.3
Release:	4
Epoch:		1
License:	GPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Source0:	http://www.xiph.org/ogg/vorbis/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am_fixes.patch
URL:		http://www.xiph.org/
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{!?_without_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.8
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libao2

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
Requires:	%{name} = %{version}
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
Requires:	%{name}-devel = %{version}

%description static
The libao-static package contains the static libraries of libao.

%description static -l es
Biblioteca de audio Libao.

%description static -l pl
Statyczna wersja biblioteki libao.

%description static -l pt_BR
Biblioteca de audio Libao.

%package arts
Summary:	Arts plugin for libao
Summary(pl):	Wtyczka arts dla libao
Group:		Libraries
Requires:	%{name} = %{version}

%description arts
Arts plugin for libao.

%description arts -l pl
Wtyczka arts dla libao.

%package esd
Summary:	ESD plugin for libao
Summary(pl):	Wtyczka ESD dla libao
Group:		Libraries
Requires:	%{name} = %{version}

%description esd
Arts plugin for ESD.

%description esd -l pl
Wtyczka esd dla libao.

%package alsa
Summary:	ALSA plugin for libao
Summary(pl):	Wtyczka ALSA dla libao
Group:		Libraries
Requires:	libao = %{version}

%description alsa
ALSA plugin for libao.

%description alsa -l pl
Wtyczka ALSA dla libao.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%ifnarch sparc sparc64
	%{?_without_alsa:--disable-alsa} \
	%{?!_without_alsa:--enable-alsa} \
	%{?_without_arts:--disable-arts} \
%endif
	--enable-shared \
	--enable-static

%{__make} \
	plugindir=%{_libdir}/ao

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_libdir}/ao \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README TODO
%attr(755,root,root) %{_libdir}/libao.so.*.*
%dir %{_libdir}/ao
%attr(755,root,root) %{_libdir}/ao/liboss.so
%{_libdir}/ao/liboss.la
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc doc/*{html,css}
%attr(755,root,root) %{_libdir}/libao.so
%{_libdir}/libao.la
%{_includedir}/ao
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{?_without_arts:0}%{!?_without_arts:1}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/libarts.so
%{_libdir}/ao/libarts.la
%endif

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/libesd.so
%{_libdir}/ao/libesd.la

%if %{?_without_alsa:0}%{!?_without_alsa:1}
%ifnarch sparc sparc64
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/libalsa*.so
%{_libdir}/ao/libalsa*.la
%endif
%endif
