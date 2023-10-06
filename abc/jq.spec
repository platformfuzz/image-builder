%define name        jq
%define version     1.7
%define release     1
%define buildroot   %{_topdir}/%{name}-%{version}-root

Summary:        Command-line JSON processor
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        MIT
Source:         https://github.com/stedolan/jq/archive/jq-%{version}.tar.gz
URL:            https://stedolan.github.io/jq/
Group:          Development/Tools

# Build dependencies
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
# BuildRequires:  oniguruma-devel
BuildRequires:  readline-devel

%description
`jq` is a lightweight and flexible command-line JSON processor.

%prep
%setup -q -n jq-%{version}

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md
/usr/local/bin/jq

%changelog
* Fri Oct 6 2023 John Ajera jdcajera@gmail.com - 8.17-1
- Initial RPM release
