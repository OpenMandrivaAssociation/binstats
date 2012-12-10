%define name binstats
%define version 1.08
%define release %mkrel 10

Summary: An administration utility
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: File tools
URL: http://www.ccc.nottingham.ac.uk/~etzpc/binstats.html
Source: %{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot

%description
An administration utility for tracking down the 
various types of binary formats for Linux (i386) executables and their 
dynamic library dependencies and also executable scripts.

%prep

%setup -q

%build
make
strip derefsymlink

%install
rm -rf $RPM_BUILD_ROOT

# make install
install -m 755 -d $RPM_BUILD_ROOT%_bindir
install -m 755 binstats $RPM_BUILD_ROOT%_bindir
install -m 755 derefsymlink $RPM_BUILD_ROOT%_bindir

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%_bindir/*
%doc README



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.08-10mdv2011.0
+ Revision: 616765
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.08-9mdv2010.0
+ Revision: 424622
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.08-8mdv2009.0
+ Revision: 243313
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.08-6mdv2008.1
+ Revision: 135829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import binstats


* Tue Aug 01 2006 Lenny Cartier <lenny@mandrakesoft.com> 1.08-6mdv2007.0
- rebuild

* Tue Apr 26 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.08-5mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.08-4mdk
- rebuild

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.08-3mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.08-2mdk
- rebuild

* Thu Jun 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.08-1mdk
- updated to 1.08

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.07-1mdk
- updated to 1.07

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-4mdk
- remove packager tag

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-3mdk
- BM

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.00-2mdk
- bzip2 patch
- fix group

* Mon Feb 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.00-1mdk
- mandrake build
