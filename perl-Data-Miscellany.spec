%define upstream_name    Data-Miscellany
%define upstream_version 1.100850

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Collection of miscellaneous subroutines
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


