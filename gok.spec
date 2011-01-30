#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	usb		# support for libusb input
#
Summary:	GNOME Onscreen Keyboard
Summary(pl.UTF-8):	Klawiatura na ekranie dla GNOME
Name:		gok
Version:	2.30.1
Release:	2
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gok/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	09ae1130220e9321fce9a4a6d0890cea
URL:		http://www.gok.ca/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	at-spi-devel >= 1.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-speech-devel >= 0.4.16
BuildRequires:	gtk+2-devel >= 2:2.18.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonobo-devel >= 2.24.0
BuildRequires:	libcanberra-gtk-devel >= 0.3
BuildRequires:	libtool
%{?with_usb:BuildRequires:	libusb-compat-devel}
BuildRequires:	libwnck-devel >= 2.24.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.14
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXi-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%package apidocs
Summary:	gok API documentation
Summary(pl.UTF-8):	Dokumentacja API gok
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gok API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gok.

%prep
%setup -q

sed -i -e 's/en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--disable-schemas-install \
	--disable-silent-rules \
	%{?with_usb:--enable-libusb-input} \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

if [ -f C/main.kbd ]; then
	mv C/*.kbd .
fi
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gok.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gok.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/create-branching-keyboard
%attr(755,root,root) %{_bindir}/gok
%{_libdir}/bonobo/servers/GNOME_Gok.server
%{_datadir}/%{name}
%{_pkgconfigdir}/gok-1.0.pc
%{_sysconfdir}/gconf/schemas/gok.schemas
%{_iconsdir}/hicolor/*/apps/gok.png
%{_pixmapsdir}/*
%{_desktopdir}/gok.desktop
%{_datadir}/sounds/freedesktop/stereo/*.wav

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gok
%endif
