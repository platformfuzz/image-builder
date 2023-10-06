%global pkgname     jq
%global pkgver      1.7
%global pkgrel      1

%define debug_package %{nil}

Name:               %{pkgname}
Version:            %{pkgver}
Release:            %{pkgrel}%{?dist}
Summary:            Command-line JSON processor
License:            MIT
URL:                https://jqlang.github.io/jq/
Source0:            https://github.com/jqlang/jq/archive/jq-%{pkgver}.tar.gz

# Build dependencies
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  oniguruma-devel
BuildRequires:  readline-devel

%description
%{pkgname} is a lightweight and flexible command-line JSON processor.

%clean
rm -rf %{buildroot}
touch %{buildroot}/test

%prep
# %autosetup -n jq-1.7
# mv %{buildroot}/%{pkgname}-%{pkgname}-%{pkgver}
# %setup -q -n jq-1.7
# %setup -n jq-1.7
# %setup -B jq-1.7
# %setup
# tar -xvf %{SOURCE0} -C %{SOURCEDIR}
# /usr/bin/gzip -dc /root/rpmbuild/SOURCES/jq-1.7.tar.gz
# /usr/bin/tar -xof -
# %setup -q -c -n jq-1.7
%setup -q -c -T -D -n jq-1.7


%build
# mv %{buildroot}/%{pkgname}-%{pkgname}-%{pkgver}
# cd %{source}
# ./configure
# make
autoreconf -fi
%configure --prefix=%{_prefix}
make %{?_smp_mflags}


%install
# mkdir -m 755 -p ${RPM_BUILD_ROOT}/%{install_path}
# tar -C ${RPM_BUILD_ROOT}%{install_base} -xf %{SOURCE0}
# mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

%files
# %defattr(-,root,root,-)
%license LICENSE
%{_bindir}/%{name}

%changelog
* Fri Oct 6 2023 John Ajera <jdcajera@gmail.com> - 1.7-1.el8.x86_64
- Initial RPM release
