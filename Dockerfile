FROM python:3.7.0-alpine3.8
LABEL maintainer="luk.zim91@gmail.com"

COPY . /opt
WORKDIR /opt
RUN addgroup -S app && \
    adduser -SDHG app app && \
    pip install --no-cache-dir -r requirements.txt && \
    chown -R app:app /opt && \
    rm -rf /opt/requirements.txt /tmp/* /var/tmp/*
USER app
ENTRYPOINT [ "python", "/opt/app/app.py" ]
