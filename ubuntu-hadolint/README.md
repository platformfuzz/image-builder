# Ubuntu HadoLint

```dockerfile
FROM ghcr.io/platformfuzz/image-builder/ubuntu:latest

RUN apt-get install -y curl --no-install-recommends \
  && curl -k -L -o /usr/bin/hadolint \
    https://github.com/hadolint/hadolint/releases/latest/download/hadolint-Linux-x86_64 \
  && chmod +x /usr/bin/hadolint \
  && apt-get update -y \
  && apt-get upgrade -y \
  && rm -rf /var/lib/apt/lists/*
``````
