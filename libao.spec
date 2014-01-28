# TODO:
# - roaraudio plugin (needs roaraudio: http://roaraudio.keep-cool.org/downloads.html)
# - ckport support? (%{_libdir}/ckport/db/libao.ckport)
#
# Conditional build:
%bcond_without	alsa		# don't build ALSA plugin
%bcond_with	arts		# build aRts plugin
%bcond_with	esd		# build ESD plugin
%bcond_without	nas 		# don't build NAS plugin
%bcond_without	pulseaudio	# don't build Pulseaudio plugin
%bcond_without	static_libs	# don't build static library
#
Summary:	Cross Platform Audio Output Library
Summary(es.UTF-8):	Biblioteca libao
Summary(pl.UTF-8):	Międzyplatformowa biblioteka do odtwarzania dźwięku
Summary(pt_BR.UTF-8):	Biblioteca libao
Name:		libao
Version:	1.2.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
# Source0-md5:	9f5dd20d7e95fd0dd72df5353829f097
URL:		http://www.xiph.org/ao/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.0}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
BuildRequires:	libtool
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
BuildRequires:	rpmbuild(macros) >= 1.527
%{?with_nas:BuildRequires:	xorg-lib-libXau-devel}
Obsoletes:	libao2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libao is a cross-platform audio library that allows programs to output
audio using a simple API on a wide variety of platforms. It currently
supports: Null output, WAV files, OSS (Open Sound System), ALSA
(Advanced Linux Sound Architecture), Solaris (untested), IRIX
(untested)

%description -l es.UTF-8
Libaso es un biblioteca de audio que soporta programas com salida de
audio usando una API simplificada en una gran variedad de
arquiteturas. Hoy soporta Null output, WAV files, OSS (Open Sound
System), ALSA (Advanced Linux Sound Architecture), Solaris (untested),
IRIX (untested).

%description -l pl.UTF-8
Libao jest biblioteką do odtwarzania dźwięku, która ma proste API i
jest dostępna na wielu różnych platformach. Aktualnie wspiera
odtwarzanie na urządzenie puste (null output), do plików w formacie
WAV oraz urządzenia ALSA (Advanced Linux Sound Architecture), OSS
(Open Sound System), Solaris i IRIX.

%description -l pt_BR.UTF-8
Libao é uma biblioteca de audio multi-plataforma que permite programas
para saida de audio usando uma API simples em uma variedade grande de
plataformas. Atualmente suporta Null output, WAV files, OSS (Open
Sound System), ALSA (Advanced Linux Sound Architecture), Solaris
(untested), IRIX (untested).

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

%package pulse
Summary:	Pulseaudio plugin for libao
Summary(pl.UTF-8):	Wtyczka Pulseaudio dla libao
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libao-polyp

%description pulse
Pulseaudio plugin for libao.

%description pulse -l pl.UTF-8
Wtyczka Pulseaudio dla libao.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{__enable_disable alsa} \
	%{__enable_disable arts} \
	%{__enable_disable esd} \
	%{__enable_disable nas} \
	%{__enable_disable pulseaudio pulse} \
	%{__enable_disable static_libs static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by *.so
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ao/plugins-4/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ao/plugins-4/*.a
%endif

# devel docs (HTML, C example)
%{__mv} $RPM_BUILD_ROOT%{_docdir}/{libao-%{version},libao-devel-%{version}}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README TODO
%attr(755,root,root) %{_libdir}/libao.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libao.so.4
%dir %{_libdir}/ao
%dir %{_libdir}/ao/plugins-4
%attr(755,root,root) %{_libdir}/ao/plugins-4/liboss.so
%{_mandir}/man5/libao.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libao.so
%{_libdir}/libao.la
%{_includedir}/ao
%{_aclocaldir}/ao.m4
%{_pkgconfigdir}/ao.pc
%{_docdir}/libao-devel-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libao.a
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-4/libalsa.so
%endif

%if %{with arts}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-4/libarts.so
%endif

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-4/libesd.so
%endif

%if %{with nas}
%files nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-4/libnas.so
%endif

%if %{with pulseaudio}
%files pulse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-4/libpulse.so
%endif
