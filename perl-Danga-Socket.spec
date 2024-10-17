%define upstream_name    Danga-Socket
%define upstream_version 1.61

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Event loop and event-driven async socket base class
License:	GPL+ and Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Danga/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Sys::Syscall)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES
%{perl_vendorlib}/Danga
%{_mandir}/man3/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.610.0-2mdv2011.0
+ Revision: 681369
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.610.0-1mdv2011.0
+ Revision: 405959
- rebuild using %%perl_convert_version

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.61-1mdv2009.1
+ Revision: 309296
- update to new version 1.61

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.59-2mdv2009.0
+ Revision: 268407
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.59-1mdv2009.0
+ Revision: 194843
- update to new version 1.59
- update to new version 1.59

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.58-1mdv2008.1
+ Revision: 156175
- update to new version 1.58

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.57-1mdv2008.0
+ Revision: 19826
- 1.57


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.53-1mdv2007.0
- new version
- fix sources URL

* Wed Aug 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.52-1mdv2007.0
- New version 1.52
- fix directory ownership

* Sun Apr 30 2006 Michael Scherer <misc@mandriva.org> 1.51-1mdk
- New release 1.51

* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 1.50-1mdk
- First Mandriva package

