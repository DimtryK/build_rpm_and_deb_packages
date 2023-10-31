FROM oraclelinux:8.4

RUN dnf install -y rpm-build \
python3 \
python3-setuptools

RUN mkdir -p /root/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

COPY psycopg.spec /root/rpmbuild/SPECS/
COPY psycopg-3.1.12.tar.gz /root/rpmbuild/SOURCES/

RUN rpmbuild -ba /root/rpmbuild/SPECS/psycopg.spec

WORKDIR /root/rpmbuild/RPMS/noarch

CMD ["/bin/bash"]