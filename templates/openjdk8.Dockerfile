ARG FROM
FROM ${FROM}

USER root
WORKDIR /

ENV JAVA_HOME=/opt/openjdk
ENV PATH=${JAVA_HOME}/bin:${PATH}

RUN wget https://github.com/AdoptOpenJDK/openjdk8-upstream-binaries/releases/download/jdk8u222-b10/OpenJDK8U-jdk_x64_linux_8u222b10.tar.gz \
    && tar -vxf OpenJDK8U-jdk_x64_linux_8u222b10.tar.gz \
    && rm OpenJDK8U-jdk_x64_linux_8u222b10.tar.gz \
    && mv openjdk-8u222-b10 ${JAVA_HOME} \
    && java -version
