%define upstream_name    Data-Miscellany
%define upstream_version 1.100850

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Collection of miscellaneous subroutines
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
This is a collection of miscellaneous subroutines useful in wide but
varying scenarios; a catch-all module for things that don't obviously
belong anywhere else. Obviously what's useful differs from person to
person, but this particular collection should be useful in object-oriented
frameworks, such as the Class::Framework manpage and the Data::Conveyor
manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.100.850-2mdv2011.0
+ Revision: 653401
- rebuild for updated spec-helper

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.850-1mdv2011.0
+ Revision: 527732
- update to 1.100850

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 474658
- update to 0.04

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 444077
- import perl-Data-Miscellany


* Thu Sep 17 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
