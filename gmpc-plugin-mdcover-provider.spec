%define		source_name gmpc-mdcover
Summary:	Cover art from local directory provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Dostawca okładek z lokalnego katalogu dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-mdcover-provider
Version:	0.18.100
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	2344508cf5552e183c1996d93aa6644f
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_MDCOVER
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.18.100
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.18.100
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gmpc >= 0.18.100
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

%find_lang %{name} --all-name

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
