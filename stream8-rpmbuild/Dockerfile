FROM ghcr.io/platformfuzz/image-builder/stream8:latest

RUN dnf install -y epel-release \
    epel-next-release \
    'dnf-command(config-manager)' \
    dnf-utils \
    rpm-build \
    rpmdevtools \
  && dnf config-manager --set-enabled powertools \
  && dnf update -y \
  && dnf clean all \
  && rm -r -f /var/cache/*
