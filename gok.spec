Summary:	GNOME Onscreen Keyboard
Summary(pl.UTF-8):   Klawiatura na ekranie dla GNOME
Name:		gok
Version:	1.2.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gok/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	a5b022cf0b83800a38bb1f6d402ffa57
Patch0:		%{name}-desktop.patch
URL:		http://www.gok.ca/
BuildRequires:	ORBit2-devel >= 2.14.2
BuildRequires:	at-spi-devel >= 1.7.11
BuildRequires:	atk-devel >= 1:1.12.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.36
BuildRequires:	gail-devel >= 1.9.2
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-speech-devel >= 0.4.4
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool >= 0.35
BuildRequires:	libbonobo-devel >= 2.15.3
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.15.92
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.14
BuildRequires:	xorg-lib-libXi-devel
Requires(post,preun):	GConf2
Requires:	libgnomeui >= 2.15.91
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gok project aims to enable users to control their computer without
having to rely on a standard keyboard or mouse. Many individuals must
control the computer using alternative input methods. Using innovative
dynamic keyboard strategies, and leveraging GNOME 2's built-in
accessibility framework, the gok will make control more efficient and
enable use of the GNOME 2 desktop. With the right hardware support and
the gok individuals will have full access to applications that support
the AT SPI, and therefore, full access to the functionality these
applications provide.

%description -l pl.UTF-8
Celem projektu gok jest umożliwienie użytkownikom sterowania ich
komputerem bez konieczności używania standardowej klawiatury ani
myszy. Wiele osób musi sterować komputerem przy użyciu alternatywnych
metod wejściowych. Przy użyciu innowacyjnych strategii dynamicznej
klawiatury oraz wbudowanego szkieletu mechanizmów dostępności w GNOME
2, gok będzie umożliwiał bardziej wydajne sterowanie i pozwoli na
używanie pulpitu GNOME 2. Przy odpowiednim wsparciu ze strony sprzętu,
użytkownicy gok uzyskają pełny dostęp do aplikacji obsługujących AT
SPI, a przez to pełny dostęp do funkcjonalności dostarczanych przez te
aplikacje.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/gnome-common/data/omf.make .
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--disable-schemas-install \
	--enable-gtk-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gok.schemas

%preun
%gconf_schema_uninstall gok.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%{_pkgconfigdir}/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_gtkdocdir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
