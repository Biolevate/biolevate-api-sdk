.PHONY: generate-python install-python lint-python test-python clean build-generators help

# Generator versions (pinned)
PYTHON_GENERATOR_VERSION := 0.28.2
PYTHON_GENERATOR_IMAGE := biolevate/python-generator:$(PYTHON_GENERATOR_VERSION)

help:
	@echo "Available targets:"
	@echo "  build-generators  - Build all generator Docker images"
	@echo "  generate-python   - Generate Python client from OpenAPI spec"
	@echo "  install-python    - Install Python workspace (all packages)"
	@echo "  lint-python       - Lint and format Python code"
	@echo "  test-python       - Run Python tests"
	@echo "  clean             - Clean generated artifacts"

# Build the Python generator Docker image
build-generators:
	docker build \
		-f tools/docker/python-generator.Dockerfile \
		--build-arg OPENAPI_PYTHON_CLIENT_VERSION=$(PYTHON_GENERATOR_VERSION) \
		-t $(PYTHON_GENERATOR_IMAGE) \
		tools/docker

# Generate Python client from OpenAPI spec (via Docker)
generate-python: build-generators
	docker run --rm \
		-v $(PWD):/workspace \
		$(PYTHON_GENERATOR_IMAGE) \
		generate \
		--path /workspace/openapi/biolevate-api.json \
		--config /workspace/tools/openapi-python-client.yml \
		--output-path /workspace/python/client \
		--overwrite

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
	rm -rf python/client/biolevate_client
