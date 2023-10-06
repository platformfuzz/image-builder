Name:           wine
Version:        8.17
Release:        1%{?dist}
Summary:        Wine is a compatibility layer for running Windows applications on Linux.

License:        LGPLv2+
URL:            https://www.winehq.org/
Source0:        https://dl.winehq.org/wine/source/8.x/wine-%{version}.tar.xz

# Build dependencies
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libgcc
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtiff-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libxslt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Wine is a compatibility layer that allows you to run Windows applications on Unix-like operating systems, including Linux and macOS. It provides a way to run Windows software on non-Windows operating systems, making it possible to use many Windows applications on your preferred platform.

%prep
%autosetup -n wine-%{version}

%build
# Configure Wine with optional features
# For example, to enable 32-bit support, use:
# ./configure --enable-win64 --with-wine64
# ./configure --without-freetype
# For more configuration options, see Wine documentation
./configure -enable-win64
make %{?_smp_mflags}

%install
# Install Wine to the buildroot
make install DESTDIR=%{buildroot}

# Create Wine directories and symlinks
mkdir -p %{buildroot}/%{_bindir}
ln -s ../usr/bin/wine %{buildroot}/%{_bindir}/wine
ln -s ../usr/bin/winecfg %{buildroot}/%{_bindir}/winecfg
# ...

# Create Wine menu entries (optional)
# This depends on your desktop environment
# Install .desktop files, icons, etc. as needed
# For example, for a GNOME-based system:
# mkdir -p %{buildroot}/%{_datadir}/applications
# cp wine.desktop %{buildroot}/%{_datadir}/applications/
# ...

%files
# List all installed files and directories
%{_bindir}/wine
%{_bindir}/winecfg
# Add other Wine binaries and tools
%{_bindir}/notepad
%{_bindir}/regedit
%{_datadir}/wine
%{_libdir}/wine
%{_mandir}/man1/*

# Add menu entries (optional)
# %{_datadir}/applications/wine.desktop
# Add other desktop-related files (icons, themes, etc.) if needed
# ...

%changelog
* Fri Oct 6 2023 Your Name jdcajera@gmail.com - 8.17-1
- Initial package build for Wine 8.17
