FROM registry.access.redhat.com/ubi8/ubi:8.8-1067

RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm \
    && /usr/bin/crb enable \
    && dnf install -y https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-8.noarch.rpm \
      'dnf-command(config-manager)' \
    && dnf update -y \
    && rm -r -f /var/cache/*
