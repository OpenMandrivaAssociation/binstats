%define name binstats
%define version 1.08
%define release %mkrel 9

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

