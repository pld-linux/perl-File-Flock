%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Flock
Summary:	File::Flock perl module
Summary(pl):	Modu³ perla File::Flock
Name:		perl-File-Flock
Version:	101.060501
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Flock is a wrapper around the flock() call.

%description -l pl
File::Flock umo¿liwia korzystanie z wywo³ania flock().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%{perl_sitelib}/File/Flock.pm
%{_mandir}/man3/*
