%define		_enable_debug_packages	0

Summary:	The Cangjie engine for IBus input platform
Summary(pl.UTF-8):	Silnik Cangjie dla platformy wprowadzania znaków IBus
Name:		ibus-cangjie
Version:	2.4
Release:	6
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/Cangjians/ibus-cangjie/releases
Source0:	https://github.com/Cangjians/ibus-cangjie/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3c78f16cf6562d52adc3c32158d96b7f
URL:		https://github.com/Cangjians/ibus-cangjie
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	ibus-devel >= 1.4.1
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcangjie-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2.3
BuildRequires:	python3-cangjie
BuildRequires:	python3-ibus >= 1.4.1
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	ibus >= 1.4.1
Requires:	python3-cangjie
Requires:	python3-ibus >= 1.4.1
Requires:	python3-pygobject3 >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an IBus engine for users of the Cangjie and Quick input
methods. It is primarily intended to Hong Kong people who want to
input Traditional Chinese, as they are (by far) the majority of
Cangjie and Quick users. However, it should work for others as well
(e.g to input Simplified Chinese).

%description -l pl.UTF-8
Ten pakiet zawiera silnik IBus dla użytkowników metod wprowadzania
znaków Cangjie oraz Quick. Jest przeznaczony głównie dla mieszkańców
Hong Kongu, chcących wprowadzać znaki chińskiego tradycyjnego, jako że
są oni (obecnie) większością użytkowników metod Cangjie oraz Quick.
Silnik powinien jednak działać także innym (np. wprowadzającym chiński
uproszczony).

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	am_cv_python_pythondir=%{py3_sitescriptdir} \
	--disable-silent-rules

%{__make} \
	libexecdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libexecdir=%{_libdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/ibus-setup-cangjie
%dir %{_libdir}/ibus-cangjie
%attr(755,root,root) %{_libdir}/ibus-cangjie/ibus-engine-cangjie
%{py3_sitescriptdir}/ibus_cangjie
%{_datadir}/appdata/cangjie.appdata.xml
%{_datadir}/appdata/quick.appdata.xml
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.cangjie.gschema.xml
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.quick.gschema.xml
%{_datadir}/ibus-cangjie
%{_datadir}/ibus/component/cangjie.xml
%{_datadir}/ibus/component/quick.xml
%{_desktopdir}/ibus-setup-cangjie.desktop
%{_desktopdir}/ibus-setup-quick.desktop
%{_iconsdir}/hicolor/16x16/intl/cangjie.png
%{_iconsdir}/hicolor/16x16/intl/quick.png
%{_iconsdir}/hicolor/scalable/intl/cangjie.svg
%{_iconsdir}/hicolor/scalable/intl/quick.svg
