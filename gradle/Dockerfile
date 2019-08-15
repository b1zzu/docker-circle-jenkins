ARG FROM_IMAGE
FROM ${FROM_IMAGE}

USER root
WORKDIR /

ENV GRADLE_HOME=/opt/gradle
ENV PATH=${GRADLE_HOME}/bin:${PATH}

ARG GRADLE_VERSION

RUN wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip gradle-${GRADLE_VERSION}-bin.zip \
    && rm gradle-${GRADLE_VERSION}-bin.zip \
    && mv gradle-${GRADLE_VERSION} ${GRADLE_HOME} \
    && gradle --version
