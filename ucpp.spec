#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : ucpp
Version  : 1.3.2
Release  : 6
URL      : https://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
Source0  : https://dev-www.libreoffice.org/src/0168229624cfac409e766913506961a8-ucpp-1.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ucpp-bin = %{version}-%{release}
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
Requires: ucpp-bin = %{version}-%{release}
Provides: ucpp-devel = %{version}-%{release}
Requires: ucpp = %{version}-%{release}

%description dev
dev components for the ucpp package.


%package staticdev
Summary: staticdev components for the ucpp package.
Group: Default
Requires: ucpp-dev = %{version}-%{release}

%description staticdev
staticdev components for the ucpp package.


%prep
%setup -q -n ucpp
cd %{_builddir}/ucpp
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604600746
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604600746
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ucpp

%files dev
%defattr(-,root,root,-)
/usr/include/arith.h
/usr/include/config.h
/usr/include/cpp.h
/usr/include/hash.h
/usr/include/mem.h
/usr/include/nhash.h
/usr/include/tune.h
/usr/include/ucppi.h

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libucpp.a
