.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
	sort | \
	awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

build: ## Build
	docker build -t n3-guide .

test: ## Test
	docker run -tv $(shell pwd):/source -w /local --env-file .env n3-guide:latest pytest -v tests/

cli: ## CLI
	docker run -it -v $(shell pwd):/source -w /local --env-file .env n3-guide:latest bash