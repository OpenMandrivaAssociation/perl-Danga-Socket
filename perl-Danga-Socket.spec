%define module  Danga-Socket
%define name    perl-%{module}
%define version 1.61
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Event loop and event-driven async socket base class
License:        GPL and Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Danga/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Sys::Syscall)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is an abstract base class for objects backed by a socket which provides 
the basic framework for event-driven asynchronous IO, designed to be fast. 
Danga::Socket is both a base class for objects, and an event loop.

Callers subclass Danga::Socket. Danga::Socket's constructor registers itself 
with the Danga::Socket event loop, and invokes callbacks on the object for 
readability, writability, errors, and other conditions.
Because Danga::Socket uses the "fields" module, your subclasses must too.

%prep
%setup -q -n %{module}-%{version} 

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

