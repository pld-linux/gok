Summary:	GNOME Onscreen Keyboard
Summary(pl):	Klawiatura na ekranie dla GNOME
Name:		gok
Version:	1.0.10
Release:	2
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gok/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	de6cceaca780e7ad0702c4b3c0fd8d1f
Patch0:		%{name}-desktop.patch
URL:		http://www.gok.ca/
BuildRequires:	ORBit2-devel
BuildRequires:	at-spi-devel >= 1.6.6
BuildRequires:	atk-devel >= 1:1.10.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gail-devel >= 1.8.5
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-speech-devel
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
BuildRequires:	libxml2-devel >= 1:2.6.21
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.14
Requires(post,preun):	GConf2
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

%description -l pl
Celem projektu gok jest umo¿liwienie u¿ytkownikom sterowania ich
komputerem bez konieczno¶ci u¿ywania standardowej klawiatury ani
myszy. Wiele osób musi sterowaæ komputerem przy u¿yciu alternatywnych
metod wej¶ciowych. Przy u¿yciu innowacyjnych strategii dynamicznej
klawiatury oraz wbudowanego szkieletu mechanizmów dostêpno¶ci w GNOME
2, gok bêdzie umo¿liwia³ bardziej wydajne sterowanie i pozwoli na
u¿ywanie pulpitu GNOME 2. Przy odpowiednim wsparciu ze strony sprzêtu,
u¿ytkownicy gok uzyskaj± pe³ny dostêp do aplikacji obs³uguj±cych AT
SPI, a przez to pe³ny dostêp do funkcjonalno¶ci dostarczanych przez te
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
%{_desktopdir}/*
