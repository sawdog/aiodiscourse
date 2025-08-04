
.PHONY: help docs test docker-run

help:
	@echo "make docs        - Build HTML docs"
	@echo "make test        - Run tests"
	@echo "make docker-run  - Start local Discourse dev container"

docs:
	sphinx-build docs docs/_build/html

test:
	pytest

docker-run:
	docker compose -f docker/docker-compose.yml up --build
