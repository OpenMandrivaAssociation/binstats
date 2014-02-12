Summary:	An administration utility
Name:		binstats
Version:	1.08
Release:	11
License:	GPL
Group:		File tools
Url:		http://www.ccc.nottingham.ac.uk/~etzpc/binstats.html
Source0:	%{name}-%{version}.tar.bz2

%description
An administration utility for tracking down the various types of binary
formats for Linux (i386) executables and their dynamic library dependencies
and also executable scripts.

%files
%doc README
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
# make install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 binstats %{buildroot}%{_bindir}/binstats
install -m 755 derefsymlink %{buildroot}%{_bindir}/derefsymlink


