#
# Conditional build:	
# _without_alsa - without ALSA support
# _without_arts - without aRts support
#
Summary:	Cross Platform Audio Output Library
Summary(es):	Biblioteca libao
Summary(pl):	MiÍdzyplatformowa biblioteka do odtwarzania dºwiÍku
Summary(pt_BR):	Biblioteca libao
Name:		libao
Version:	0.8.2
Release:	3
Epoch:		1
License:	GPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.xiph.org/ogg/vorbis/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am_fixes.patch
Patch1:		%{name}-libdep.patch
URL:		http://www.xiph.org/
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	esound-devel >= 0.2.8
%{!?_without_arts:BuildRequires:	arts-devel}
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
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
libao jest miÍdzyplatformow± bibliotek± do odtwarzania dºwiÍku.
Aktualnie wspiera ESD, OSS, Solaris i IRIX.

%description -l pt_BR
Libao È uma biblioteca de audio multi-plataforma que permite programas
para saida de audio usando uma API simples em uma variedade grande de
plataformas. Atualmente suporta Null output, WAV files, OSS (Open
Sound System), ESD (ESounD or Enlighten Sound Daemon), ALSA (Advanced
Linux Sound Architecture), Solaris (untested), IRIX (untested).

%package devel
Summary:	Cross Platform Audio Output Library Development
Summary(pl):	CzÍ∂Ê dla programistÛw biblioteki libao
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
The libao-devel package contains the header files and documentation
needed to develop applications with libao.

%description devel -l es
Biblioteca y archivos de inclusiÛn.

%description devel -l pl
Pakiet libao-devel zawiera pliki nag≥Ûwkowe i dokumentacjÍ, potrzebne
do kompilowania aplikacji korzystaj±cych z libao.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus„o.

%package static
Summary:	Cross Platform Autio Output Static Library
Summary(es):	Bibliotecas est·ticas
Summary(pl):	Statyczna biblioteka libao
Summary(pt_BR):	Bibliotecas est·ticas
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
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
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description arts
Arts plugin for libao.

%description arts -l pl
Wtyczka arts dla libao.

%package esd
Summary:	ESD plugin for libao
Summary(pl):	Wtyczka ESD dla libao
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description esd
Arts plugin for esd.

%description esd -l pl
Wtyczka esd dla libao.

%package alsa
Summary:	ALSA plugin for libao
Summary(pl):	Wtyczka ALSA dla libao
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Requires:	libao = %{version}

%description alsa
ALSA plugin for libao.

%description alsa -l pl
Wtyczka ALSA dla libao.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
%ifnarch sparc sparc64
	%{?_without_alsa:--disable-alsa} \
	%{?!_without_alsa:--enable-alsa} \
	%{?_without_arts:--disable-arts} \
%endif
	--enable-shared \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/libao.so.*.*
%dir %{_libdir}/ao
%dir %{_libdir}/ao/plugins-2
%attr(755,root,root) %{_libdir}/ao/plugins-2/liboss.so
%attr(755,root,root) %{_libdir}/ao/plugins-2/liboss.la
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc doc/*{html,css}
%attr(755,root,root) %{_libdir}/libao.so
%attr(755,root,root) %{_libdir}/libao.la
%{_includedir}/ao
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{?_without_arts:0}%{!?_without_arts:1}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libarts.so
%attr(755,root,root) %{_libdir}/ao/plugins-2/libarts.la
%endif

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libesd.so
%attr(755,root,root) %{_libdir}/ao/plugins-2/libesd.la

%if %{?_without_alsa:0}%{!?_without_alsa:1}
%ifnarch sparc sparc64
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/plugins-2/libalsa.so
%attr(755,root,root) %{_libdir}/ao/plugins-2/libalsa.la
%endif
%endif
