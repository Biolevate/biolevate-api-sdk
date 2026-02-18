FROM python:3.12-slim

ARG OPENAPI_PYTHON_CLIENT_VERSION=0.28.2

RUN pip install --no-cache-dir \
    openapi-python-client==${OPENAPI_PYTHON_CLIENT_VERSION} \
    ruff

WORKDIR /workspace

ENTRYPOINT ["openapi-python-client"]
