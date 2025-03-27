.PHONY: clean build publish bump-patch bump-minor bump-major release-github release commit-release

# Define the token loading from .env file
PYPI_TOKEN := $(shell grep PYPI_TOKEN .env | cut -d '=' -f2)
VERSION := $(shell grep '^version = ' pyproject.toml | cut -d '"' -f2)

# Default target
all: clean build publish

# Clean up any existing build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf dist
	rm -rf *.egg-info
	rm -rf build

# Bump the patch version (0.1.3 -> 0.1.4)
bump-patch:
	@echo "Bumping patch version..."
	@sed -i.bak -E 's/^version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/version = "\1.\2.'$$(( $$(grep '^version = ' pyproject.toml | sed -E 's/^version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/\3/') + 1 ))'"/' pyproject.toml
	@rm -f pyproject.toml.bak
	@echo "Version bumped to $$(grep '^version = ' pyproject.toml | cut -d '"' -f2)"

# Bump the minor version (0.1.3 -> 0.2.0)
bump-minor:
	@echo "Bumping minor version..."
	@sed -i.bak -E 's/^version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/version = "\1.'$$(( $$(grep '^version = ' pyproject.toml | sed -E 's/^version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/\2/') + 1 ))'.0"/' pyproject.toml
	@rm -f pyproject.toml.bak
	@echo "Version bumped to $$(grep '^version = ' pyproject.toml | cut -d '"' -f2)"

# Bump the major version (0.1.3 -> 1.0.0)
bump-major:
	@echo "Bumping major version..."
	@sed -i.bak -E 's/^version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/version = "'$$(( $$(grep '^version = ' pyproject.toml | sed -E 's/^version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/\1/') + 1 ))'.0.0"/' pyproject.toml
	@rm -f pyproject.toml.bak
	@echo "Version bumped to $$(grep '^version = ' pyproject.toml | cut -d '"' -f2)"

# Build the package using uv
build: clean
	@echo "Building package with uv..."
	uv build

# Commit the version changes
commit-release:
	@echo "Committing version $$(grep '^version = ' pyproject.toml | cut -d '"' -f2)..."
	git add pyproject.toml
	git commit -m "Release v$$(grep '^version = ' pyproject.toml | cut -d '"' -f2)"

# Create a GitHub release using the current version
release-github: commit-release
	@echo "Creating GitHub release for version $$(grep '^version = ' pyproject.toml | cut -d '"' -f2)..."
	@if [ -z "$$(which gh)" ]; then echo "Error: GitHub CLI not installed. Run 'brew install gh' or visit https://cli.github.com/"; exit 1; fi
	@if ! gh auth status >/dev/null 2>&1; then echo "Error: You need to login to GitHub CLI. Run 'gh auth login'"; exit 1; fi
	git tag -a v$$(grep '^version = ' pyproject.toml | cut -d '"' -f2) -m "Release v$$(grep '^version = ' pyproject.toml | cut -d '"' -f2)"
	git push origin main
	git push origin v$$(grep '^version = ' pyproject.toml | cut -d '"' -f2)
	gh release create v$$(grep '^version = ' pyproject.toml | cut -d '"' -f2) --title "v$$(grep '^version = ' pyproject.toml | cut -d '"' -f2)" --generate-notes ./dist/*

# Publish the package to PyPI with the token from .env
publish: build
	@echo "Publishing to PyPI..."
	uv publish --token $(PYPI_TOKEN)

# Complete release process - bump version, build, publish to PyPI and GitHub
release: bump-patch build publish release-github
	@echo "Released version $$(grep '^version = ' pyproject.toml | cut -d '"' -f2)"

# Help target
help:
	@echo "Available targets:"
	@echo "  clean          - Remove build artifacts"
	@echo "  bump-patch     - Bump patch version (0.1.3 -> 0.1.4)"
	@echo "  bump-minor     - Bump minor version (0.1.3 -> 0.2.0)"
	@echo "  bump-major     - Bump major version (0.1.3 -> 1.0.0)"
	@echo "  build          - Build the package using uv"
	@echo "  publish        - Publish to PyPI with token from .env"
	@echo "  commit-release - Commit version changes to git"
	@echo "  release-github - Create a GitHub release for the current version"
	@echo "  release        - Run bump-patch, build, publish and release-github in sequence"
	@echo "  all            - Run clean, build, and publish in sequence" 