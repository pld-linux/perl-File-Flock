%include	/usr/lib/rpm/macros.perl
Summary:	File-Flock perl module
Summary(pl):	Modu³ perla File-Flock
Name:		perl-File-Flock
Version:	100.092501
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Flock-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Flock is a wrapper around the flock() call.

%description -l pl
File::Flock umo¿liwia korzystanie z wywo³ania flock().

%prep
%setup -q -n File-Flock-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/Flock.pm
%{_mandir}/man3/*
