%define		source_name gmpc-mdcover
Summary:	Cover art from local directory provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Dostawca okładek z lokalnego katalogu dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-mdcover-provider
Version:	0.16.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/0.16.0/gmpc-mdcover-%{version}.tar.gz
# Source0-md5:	838e78d6df59adb51cbfbabb5cd1bcf8
URL:		http://gmpc.sarine.nl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.16.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gmpc >= 0.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cover art from local directory provider plugin for Gnome Music Player
Client.

%description -l pl.UTF-8
Dostawca okładek z lokalnego katalogu dla odtwarzacza Gnome Music
Player Client.

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
