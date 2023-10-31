FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

RUN apt-get update && \
apt-get install -y \
python3 \
dh-python \
dpkg-dev \
debhelper \
python3-all \
python3-stdeb \
build-essential

RUN mkdir /build

COPY . /build

WORKDIR /build

RUN dpkg-buildpackage -us -uc

CMD ["/bin/bash"]