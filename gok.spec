Summary:	Gnome Onscreen Keyboard
Name:		gok
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.gok.ca/%{name}-%{version}.tar.gz
URL:		http://www.gok.ca/
BuildRequires:	at-spi-devel
BuildRequires:	libwnck-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gok project aims to enable users to control their computer without
having to rely on a standard keyboard or mouse. Many individuals must
control the computer using alternative input methods. Using innovative
dynamic keyboard strategies, and leveraging gnome 2's built-in
accessibility framework, the gok will make control more efficient and
enable use of the gnome 2 desktop. With the right hardware support and
the gok individuals will have full access to applications that support
the AT SPI, and therefore, full access to the functionality these
applications provide.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pkgconfigdir}/*
%{_omf_dest_dir}/%{name}
%{_datadir}/gnome/help/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_gtkdocdir}/%{name}
