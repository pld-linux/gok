Summary:	GNOME Onscreen Keyboard
Summary(pl):	Klawiatura na ekranie dla GNOME
Name:		gok
Version:	0.9.8
Release:	1
License:	GPL
Group:		Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	9b4ad918e331f295547deb4190737f09
Patch0:		%{name}-xmldocs_make.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-locale-names.patch
URL:		http://www.gok.ca/
BuildRequires:	at-spi-devel >= 1.3.7
BuildRequires:	atk-devel >= 1.5.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gail-devel >= 1.5.3
BuildRequires:	gnome-common
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	intltool >= 0.28
BuildRequires:	libgnomeui-devel >= 2.5.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.5.0
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	scrollkeeper >= 0.3.12
Requires(post):	GConf2
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
SPI, a przez to pe³ny dostêp do funkcjonalno¶ci dostarczancyh przez te
aplikacje.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--disable-schemas-install

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
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%{_pkgconfigdir}/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_gtkdocdir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
