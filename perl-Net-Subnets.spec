#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Subnets
Summary:	Computing subnets in large scale networks
Summary(pl.UTF-8):	Obliczanie podsieci w sieciach dużych rozmiarów
Name:		perl-Net-Subnets
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	34f945ee4f89be35065c6ec6f2e01255
URL:		http://search.cpan.org/dist/Net-Subnets/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very fast matches large lists of IP addresses against many CIDR
subnets, calculates IP address ranges and provides a simple object
oriented interface.

%description -l pl.UTF-8
Ten moduł bardzo szybko dopasowuje duże listy adresów IP do wielu
podsieci CIDR, oblicza zakresy adresów IP i udostępnia prosty
obiektowo zorientowany interfejs.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Subnets.pm
%{_mandir}/man3/*
