# To use openSMILE
FROM ubuntu:18.04 as ubuntu_base

RUN apt-get update -qq &&\
    apt-get install -qq curl &&\
    apt-get install -qq --no-install-recommends \
        libopenblas-dev liblapack-dev \
        libavcodec-dev libavformat-dev libswscale-dev \
        libtbb2 libtbb-dev libjpeg-dev \
        libpng-dev libtiff-dev &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /open_smile

COPY ./opensmile-2.3.0 ./
COPY ./dataset_files ./dataset_files
RUN cp bin/linux_x64_standalone_static/SMILExtract /usr/local/bin/