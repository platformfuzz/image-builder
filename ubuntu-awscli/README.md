# Ubuntu AWSCli

```dockerfile
FROM ghcr.io/platformfuzz/image-builder/ubuntu:latest

RUN apt-get install -y curl --no-install-recommends \
  && curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip \
  && unzip awscliv2.zip \
  && ./aws/install \
  && rm awscliv2.zip \
  && rm -r aws/ \
  && apt-get update -y \
  && apt-get upgrade -y \
  && rm -rf /var/lib/apt/lists/*
``````
