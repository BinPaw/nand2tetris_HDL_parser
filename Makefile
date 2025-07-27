.PHONY: help
.DEFAULT_GOAL := help

help:
	python -m n2t --help

install: ## Install requirements
	python -m pip install --upgrade pip
	python -m pip install --upgrade poetry
	poetry install --no-root

lock: ## Lock project dependencies
	poetry lock --no-update

update: ## Update project dependencies
	poetry update

format: ## Run code formatters
	poetry run ruff format src tests scripts
	poetry run ruff check  src tests scripts --fix

lint: ## Run code linters
	poetry run ruff format src tests scripts --check
	poetry run ruff check  src tests scripts
	poetry run mypy src tests scripts

test:  ## Run tests with coverage
	poetry run pytest --cov --last-failed --hypothesis-profile easy
