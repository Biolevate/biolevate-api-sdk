# Official OpenAPI Generator CLI
# https://github.com/OpenAPITools/openapi-generator
FROM openapitools/openapi-generator-cli:v7.20.0

WORKDIR /workspace

ENTRYPOINT ["docker-entrypoint.sh"]
