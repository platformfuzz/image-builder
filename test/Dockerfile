FROM ghcr.io/platformfuzz/image-builder/ubi8-rpmbuild:latest

COPY . .

RUN rpmdev-setuptree

COPY ./wine.spec /root/rpmbuild/SPECS/

RUN cd /root/rpmbuild/SOURCES/ \
  && spectool --get-files --all ../SPECS/*.spec \
  && cd .. \
  && yum-builddep --assumeyes ./SPECS/*.spec 
  # && rpmbuild --ba ./SPECS/*.spec

# RUN /usr/bin/rpmbuild --ba /root/rpmbuild/SPECS/yq.spec \
#   && dnf install -y /root/rpmbuild/RPMS/x86_64/yq-4.35.2-1.el8.x86_64.rpm

# RUN dnf -y install http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-6.el8.noarch.rpm \
#     http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-stream-repos-8-6.el8.noarch.rpm \
#   && dnf install -y dnf-utils rpm-build rpmdevtools \
#   && dnf clean all \
#   && rm -r -f /var/cache/*
