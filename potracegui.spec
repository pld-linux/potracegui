Summary:	GUI interface for potrace
Summary(pl):	Graficzny interfejs dla potrace
Name:		potracegui
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/potracegui/%{name}-%{version}.tar.bz2
# Source0-md5:	45097e02397a64271ec3bb0e1625a3a9
# Source0-size:	517143
Source1:	%{name}.desktop
URL:		http://potracegui.sourceforge.net/
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.0
Buildrequires:	qt-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	potrace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An GUI interface for potrace. It collects informations in an easy way
and then it launches potrace with all the relevant options.

%description -l pl
Graficzny interfejs u¿ytkownika dla potrace pobieraj±cy w prosty
sposób informacje, a nastêpnie uruchamiaj±cy potrace z odpowiednimi
opcjami.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/potracegui
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png
