Summary:	GUI interface for potrace
Summary(pl):	Interfejs GUI dla potrace
Name:		potracegui
Version:	0.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://potracegui.sourceforge.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	6a770a6c6c706f17df64223d8c943bac
Source1:	%{name}.desktop
URL:		http://potracegui.sourceforge.net
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.7
Buildrequires:	qt-devel
Requires:	potrace 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An GUI interface for potrace. It collects informations in an easy way
and then it launches potrace with all the relevant options.

%description -l pl
Interfejs GUI dla potrace pobieraj±cy w prosty sposób informacje a
nastêpnie uruchamiaj±cy potrace z odpowiednimi opcjami.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*
