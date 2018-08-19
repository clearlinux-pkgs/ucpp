#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : ucpp
Version  : 1.3.2
Release  : 2
URL      : https://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
Source0  : https://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ucpp-bin
Patch1: install.patch

%description
ucpp-1.3 is a C preprocessor compliant to ISO-C99.
Author: Thomas Pornin <pornin@bolet.org>
Main site: http://pornin.nerim.net/ucpp/

%package bin
Summary: bin components for the ucpp package.
Group: Binaries

%description bin
bin components for the ucpp package.


%package dev
Summary: dev components for the ucpp package.
Group: Development
Requires: ucpp-bin
Provides: ucpp-devel

%description dev
dev components for the ucpp package.


%prep
%setup -q -n ucpp
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534637739
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1534637739
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ucpp

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.a
