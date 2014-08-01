Summary: Simple Repeater
Name: stone
Version: 2.3e
Release: 2.3.3.17%{dist}
URL: http://www.gcd.org/sengoku/stone/
Source0: %{name}-%{version}.tar.gz
Patch0: stone.2.3.3.17.patch
License: GPL
Group: network
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: openssl-devel
Requires: openssl cpp

%description
  Stone is a TCP/IP repeater in the application layer.  It
repeats TCP and UDP from inside to outside of a firewall, or
from outside to inside.

%prep
%setup -q -n stone-2.3d-2.3.2.7
%patch0 -p1

%build
make linux-ssl SSL_FLAGS='-DUSE_SSL' SSL_LIBS='-lssl -lcrypto'

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install stone $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/stone
%doc GPL.txt README.*

%changelog
* Thu Aug 1 2014 dba@ha <hamada.pcserver.jp@gmail.com>
- modify stone.spec.
- update stone.c. (2.3.2.7 -> 2.3.3.17).
- modify Makefile. add -D_GNU_SOURCE option for RHEL6.

* Sun Jan 12 2003 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- Initial build.

