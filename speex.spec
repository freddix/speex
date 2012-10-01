%define		_rc	rc1

Summary:	An open-source, patent-free speech codec
Name:		speex
Version:	1.2
Release:	%{_rc}.12
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/speex/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	c4438b22c08e5811ff10e2b06ee9b9ae
URL:		http://www.speex.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speex is a patent-free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
Summary:	Speex library - development files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Speex library - development files.

%package progs
Summary:	speexdec and speexenc utilities
Group:		Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
Utilities for the Speex codec: speexdec (decodes a Speex file and
produces a WAV or raw file) and speexenc (encodes file from WAV or
raw format using Speex).

%prep
%setup -qn %{name}-%{version}%{_rc}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--with-ogg-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/manual.pdf
%attr(755,root,root) %ghost %{_libdir}/libspeex.so.1
%attr(755,root,root) %ghost %{_libdir}/libspeexdsp.so.1
%attr(755,root,root) %{_libdir}/libspeex.so.*.*.*
%attr(755,root,root) %{_libdir}/libspeexdsp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspeex.so
%attr(755,root,root) %{_libdir}/libspeexdsp.so
%{_libdir}/libspeex.la
%{_libdir}/libspeexdsp.la
%{_includedir}/speex
%{_aclocaldir}/speex.m4
%{_pkgconfigdir}/speex.pc
%{_pkgconfigdir}/speexdsp.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

