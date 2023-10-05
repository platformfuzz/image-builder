# UBI 8 RPM Builder

```dockerfile
FROM ghcr.io/platformfuzz/image-builder/ubi8:latest

RUN dnf -y install http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-6.el8.noarch.rpm \
    http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-stream-repos-8-6.el8.noarch.rpm \
  && dnf install -y dnf-utils rpm-build rpmdevtools \
  && dnf clean all \
  && rm -r -f /var/cache/*
``````
