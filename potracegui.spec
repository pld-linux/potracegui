Summary:	GUI interface for potrace
Summary(pl.UTF-8):	Graficzny interfejs dla potrace
Name:		potracegui
Version:	1.3.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/potracegui/%{name}-%{version}.tar.bz2
# Source0-md5:	fabd9f98cfb62048556d97d1b5d6402e
Source1:	%{name}.desktop
URL:		http://potracegui.sourceforge.net/
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.0
BuildRequires:	qt-devel >= 1:3.0.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	potrace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An GUI interface for potrace. It collects informations in an easy way
and then it launches potrace with all the relevant options.

%description -l pl.UTF-8
Graficzny interfejs użytkownika dla potrace pobierający w prosty
sposób informacje, a następnie uruchamiający potrace z odpowiednimi
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
