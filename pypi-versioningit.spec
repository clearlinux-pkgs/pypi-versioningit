#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v27
# autospec commit: 65cf152
#
Name     : pypi-versioningit
Version  : 3.3.0
Release  : 7
URL      : https://files.pythonhosted.org/packages/89/f4/bc578cc80989c572231a36cc03cc097091176fa3fb8b4e2af1deb4370eb7/versioningit-3.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/f4/bc578cc80989c572231a36cc03cc097091176fa3fb8b4e2af1deb4370eb7/versioningit-3.3.0.tar.gz
Summary  : Versioning It with your Version In Git
Group    : Development/Tools
License  : MIT
Requires: pypi-versioningit-bin = %{version}-%{release}
Requires: pypi-versioningit-license = %{version}-%{release}
Requires: pypi-versioningit-python = %{version}-%{release}
Requires: pypi-versioningit-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
|repostatus| |ci-status| |coverage| |pyversions| |conda| |license|
.. |repostatus| image:: https://www.repostatus.org/badges/latest/active.svg
:target: https://www.repostatus.org/#active
:alt: Project Status: Active — The project has reached a stable, usable
state and is being actively developed.

%package bin
Summary: bin components for the pypi-versioningit package.
Group: Binaries
Requires: pypi-versioningit-license = %{version}-%{release}

%description bin
bin components for the pypi-versioningit package.


%package license
Summary: license components for the pypi-versioningit package.
Group: Default

%description license
license components for the pypi-versioningit package.


%package python
Summary: python components for the pypi-versioningit package.
Group: Default
Requires: pypi-versioningit-python3 = %{version}-%{release}

%description python
python components for the pypi-versioningit package.


%package python3
Summary: python3 components for the pypi-versioningit package.
Group: Default
Requires: python3-core
Provides: pypi(versioningit)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-versioningit package.


%prep
%setup -q -n versioningit-3.3.0
cd %{_builddir}/versioningit-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1751307114
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-versioningit
cp %{_builddir}/versioningit-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-versioningit/7237c9d6583d5c6212b737d87c2d5432a8609f3c || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/versioningit

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-versioningit/7237c9d6583d5c6212b737d87c2d5432a8609f3c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
