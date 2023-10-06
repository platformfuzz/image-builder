FROM ghcr.io/platformfuzz/image-builder/stream8:latest

RUN dnf module enable -y python38:3.8 \
  && dnf install -y epel-release epel-next-release \
    'dnf-command(config-manager)' curl wget git jq \
    gnupg hostname net-tools initscripts iputils \
    bind-utils yum-utils sshpass make gcc gcc-c++ \
    openssl-devel bzip2-devel libffi-devel zlib-devel \
    rpm-build rpmdevtools rpm-sign rpmlint systemd \
    diffutils patch rpm-devel python39 \
  && dnf config-manager --set-enabled powertools \
  && dnf update -y \
  && rm -r -f /var/cache/*
