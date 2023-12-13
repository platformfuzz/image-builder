FROM ghcr.io/platformfuzz/image-builder/fedora39:latest

RUN dnf install -y \
    https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
    https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm \
    dnf-utils \
    rpm-build \
    rpmdevtools \
  && dnf update -y \
  && dnf clean all \
  && rm -r -f /var/cache/*
