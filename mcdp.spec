Summary:	Text mode cd player
Summary(pl):	Tekstowy odtwarzacz p³yt cd
Name:		mcdp
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.mcmilk.de/projects/mcdp/dl/latest.tar.bz2
# Source0-md5:	4a6e423cea3724b69f3e3bcdc3bacea1
URL:		http://www.mcmilk.de/projects/mcdp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcdp is a small (maybe the smallest) cd-player for linux.

%description -l pl
mcdp jest ma³ym (prawdopodobnie najmniejszym) odtwarzaczem p³yt cd pod
linuksa.

%prep
%setup -q

%build
rm -f missing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install BINDIR="$RPM_BUILD_ROOT%{_bindir}" MANDIR="$RPM_BUILD_ROOT%{_mandir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/AUTHOR doc/THANKS doc/REQUIREMENTS doc/WISHLIST doc/profile.sh doc/README doc/TODO doc/CHANGES
%attr(755,root,root) %{_bindir}/*
