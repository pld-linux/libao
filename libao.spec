#
# Conditional build:	
# _without_alsa - without ALSA support
#
Summary:	Cross Platform Audio Output Library
Summary(pl):	Miêdzyplatformowa biblioteka do odtwarzania d¼wiêku
Name:		libao
Version:	1.0.0_cvs2000.10.29
Release:	1
License:	GPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://www.xiph.org/ogg/vorbis/download/vorbis_nightly_cvs.tgz
Patch0:		%{name}-make.patch
Patch1:		%{name}-opt.patch
URL:		http://www.xiph.org/
BuildRequires:	esound-devel
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
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

%prep
%setup -q -n ao
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
CFLAGS="%{rpmcflags} -ffast-math -D_REENTRANT -fsigned-char"
%configure %{?_without_alsa:--without-alsa}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libao.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/index.html
%attr(755,root,root) %{_libdir}/libao.so
%attr(755,root,root) %{_libdir}/libao.la
%{_includedir}/ao

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
