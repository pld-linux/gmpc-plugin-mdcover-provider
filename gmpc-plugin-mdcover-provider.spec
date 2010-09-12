%define		source_name gmpc-mdcover
Summary:	Cover art from local directory provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Dostawca okładek z lokalnego katalogu dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-mdcover-provider
Version:	0.20.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	9d60da105676a75fa01aacce91e88275
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_MDCOVER
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.10
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool >= 0.21
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	gmpc >= 0.19.0
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
