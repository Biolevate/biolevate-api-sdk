.PHONY: generate-python install-python lint-python test-python clean help

# OpenAPI Generator version (official OpenAPITools/openapi-generator)
OPENAPI_GENERATOR_VERSION := 7.20.0
OPENAPI_GENERATOR_IMAGE := openapitools/openapi-generator-cli:v$(OPENAPI_GENERATOR_VERSION)

help:
	@echo "Available targets:"
	@echo "  generate-python   - Generate Python client from OpenAPI spec"
	@echo "  install-python    - Install Python workspace (all packages)"
	@echo "  lint-python       - Lint and format Python code"
	@echo "  test-python       - Run Python tests"
	@echo "  clean             - Clean generated artifacts"

# Generate Python client from OpenAPI spec (via Docker)
# Then apply patch so EliseOntologyMeta.meta_value is Any (backend sends arbitrary JSON)
generate-python:
	rm -rf python/client
	docker run --rm \
		-v $(PWD):/workspace \
		$(OPENAPI_GENERATOR_IMAGE) \
		generate \
		-c /workspace/tools/openapi-generator-config.yaml
	python3 tools/patch-elise-ontology-meta.py

# Install Python workspace (all packages with dev dependencies)
install-python:
	cd python && uv sync --all-extras

# Lint and format Python code
lint-python:
	cd python && uv run ruff check --fix
	cd python && uv run ruff format

# Run Python tests
test-python:
	cd python && uv run pytest

# Clean generated artifacts
clean:
	rm -rf python/client
