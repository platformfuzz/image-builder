# Ubuntu AWSCli

```dockerfile
FROM ghcr.io/platformfuzz/image-builder/ubuntu:latest

RUN apt-get update -y \
  && apt-get install -y curl unzip --no-install-recommends \
  && apt-get install -y --reinstall ca-certificates \
  && update-ca-certificates \
  && curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip \
  && unzip awscliv2.zip \
  && ./aws/install \
  && rm awscliv2.zip \
  && rm -r aws/ \
  && apt-get update -y \
  && apt-get upgrade -y \
  && rm -rf /var/lib/apt/lists/*
``````
