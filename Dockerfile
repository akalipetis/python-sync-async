FROM python:3.8
WORKDIR /usr/src/app
RUN wget https://github.com/tsenart/vegeta/releases/download/v12.8.4/vegeta_12.8.4_linux_amd64.tar.gz -O /tmp/vegeta.tar.gz && \
    cd /tmp && \
    tar zxf /tmp/vegeta.tar.gz && \
    mv vegeta /usr/local/bin
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY ./ ./