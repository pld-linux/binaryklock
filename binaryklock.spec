Summary:	Binary clock applet
Summary(pl.UTF-8):	Aplet binarnego zegara
Name:		binaryklock
Version:	0.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ubercode.de/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	b4d7a0a46b316908864b656678d89740
Patch0:		kde-ac260-lt.patch
URL:		http://ubercode.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BinaryKlock is a binary clock kicker applet.

%description -l pl.UTF-8
BinaryKlock to biarny zegar będący apletem kickera.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
# update config.sub for amd64
cp -f /usr/share/automake/config.sub admin
# or rebuild auto*
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/applets/*.desktop
%{_libdir}/kde3/binaryklock_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/binaryklock_panelapplet.so
