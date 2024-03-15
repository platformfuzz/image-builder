FROM ghcr.io/platformfuzz/image-builder/ubuntu:latest

RUN apt-get update -y \
  && apt-get install -y curl --no-install-recommends \
  && apt-get install -y --reinstall ca-certificates \
  && update-ca-certificates \
  && curl -k -L -o /usr/bin/hadolint \
    https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64 \
  && chmod +x /usr/bin/hadolint \
  && apt-get update -y \
  && apt-get upgrade -y \
  && rm -rf /var/lib/apt/lists/*
