# CentOS Stream 8 Development

```dockerfile
FROM ghcr.io/platformfuzz/image-builder/stream8:latest

RUN dnf install -y dnf-utils rpm-build rpmdevtools \
  && dnf clean all \
  && rm -r -f /var/cache/*
``````
