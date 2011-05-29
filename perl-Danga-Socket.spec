%define upstream_name    Danga-Socket
%define upstream_version 1.61

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Event loop and event-driven async socket base class
License:    GPL+ and Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Danga/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Sys::Syscall)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an abstract base class for objects backed by a socket which provides 
the basic framework for event-driven asynchronous IO, designed to be fast. 
Danga::Socket is both a base class for objects, and an event loop.

Callers subclass Danga::Socket. Danga::Socket's constructor registers itself 
with the Danga::Socket event loop, and invokes callbacks on the object for 
readability, writability, errors, and other conditions.
Because Danga::Socket uses the "fields" module, your subclasses must too.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES
%{perl_vendorlib}/Danga
%{_mandir}/man3/*
