# Most recent Ubuntu LTS
FROM ubuntu:20.04

ENV TZ=Europe/Bratislava
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set an encoding to make things work smoothly.
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Add a timestamp for the build. Also, bust the cache.
#ADD http://worldclockapi.com/api/json/utc/now /opt/docker/etc/timestamp

# Install system packages (fix by https://github.com/phusion/baseimage-docker/issues/319 )
RUN apt-get --yes -qq update \
 && apt-get --yes -qq upgrade \
 && apt-get install -y --no-install-recommends apt-utils \
 && apt-get --yes -qq install \
                      bzip2 \
                      cmake \
                      cpio \
                      curl \
                      g++ \
                      gcc \
                      gfortran \
                      git \
                      gosu \
                      libblas-dev \
                      liblapack-dev \
                      libopenmpi-dev \
                      openmpi-bin \
                      python3-dev \
                      python3-pip \
                      virtualenv \
                      wget \
                      zlib1g-dev \
 && apt-get --yes -qq clean \
 && rm -rf /var/lib/apt/lists/*

# Run common commands
COPY run_commands /opt/docker/bin/run_commands
RUN /opt/docker/bin/run_commands

# Add a file for users to source
COPY entrypoint_source /opt/docker/bin/entrypoint_source

# Add a file that wraps that for use with the `ENTRYPOINT`.
COPY entrypoint /opt/docker/bin/entrypoint

# Ensure that all containers start with tini and the user selected process.
ENTRYPOINT [ "/opt/docker/bin/tini", "--", "/opt/docker/bin/entrypoint" ]

# Provide a default command (`bash`), which will start if the user doesn't specify one.
CMD [ "/bin/bash" ]
