#
# Conditional build:	
# _without_alsa - without ALSA support
# _without_arts - without aRts support
#
Summary:	Cross Platform Audio Output Library
Summary(pl):	Miêdzyplatformowa biblioteka do odtwarzania d¼wiêku
Name:		libao
Version:	0.7.0
Release:	1
Epoch:		1
License:	GPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.vorbis.com/files/rc1/unix/%{name}-%{version}.tar.gz
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
libao is a cross platform audio output library. It currently supports
ESD, OSS, Solaris, and IRIX.

%description -l pl
libao jest miêdzyplatformow± bibliotek± do odtwarzania d¼wiêku.
Aktualnie wspiera ESD, OSS, Solaris i IRIX.

%package devel
Summary:	Cross Platform Audio Output Library Development
Summary(pl):	Czê¶æ dla programistów biblioteki libao
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libao-devel package contains the header files and documentation
needed to develop applications with libao.

%description devel -l pl
Pakiet libao-devel zawiera pliki nag³ówkowe i dokumentacjê, potrzebne
do kompilowania aplikacji korzystaj±cych z libao.

%package static
Summary:	Cross Platform Autio Output Static Library
Summary(pl):	Statyczna biblioteka libao
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The libao-static package contains the static libraries of libao.

%description static -l pl
Statyczna wersja biblioteki libao.

%package arts
Summary:	Arts plugin for libao
Summary(pl):	Wtyczka arts dla libao
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	libao = %{version}

%description arts
Arts plugin for libao.

%description -l pl arts
Wtyczka arts dla libao.

%package esd
Summary:	ESD plugin for libao
Summary(pl):	Wtyczka ESD dla libao
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	libao = %{version}

%description esd
Arts plugin for esd.

%description -l pl esd
Wtyczka esd dla libao.

%prep
%setup -q

%build
rm missing
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS CHANGES README TODO doc/API doc/DRIVERS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/DRIVERS*
%attr(755,root,root) %{_libdir}/libao.so.*.*
%dir %{_libdir}/ao
%attr(755,root,root) %{_libdir}/ao/liboss.so
%attr(755,root,root) %{_libdir}/ao/liboss.la

%files devel
%defattr(644,root,root,755)
%doc doc/API*
%attr(755,root,root) %{_libdir}/libao.so
%attr(755,root,root) %{_libdir}/libao.la
%{_includedir}/ao
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%if %{?_without_arts:0}%{!?_without_arts:1}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/libarts.so
%attr(755,root,root) %{_libdir}/ao/libarts.la
%endif

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ao/libesd.so
%attr(755,root,root) %{_libdir}/ao/libesd.la
