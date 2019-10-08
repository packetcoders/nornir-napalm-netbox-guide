.DEFAULT_GOAL := help

#export PYROOT=./ansible/scripts
export YAMLROOT=./ansible/

.PHONY: help
help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
	sort | \
	awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

.PHONY: remove-yml-eol-spaces
remove-yml-eol-spaces: ## Remove end of line spaces from yaml files
	@echo "[*] Removing EOL YAML spaces."
	@find ./ \( -name *.yaml -o -name *.yml \) | xargs sed -i  "s/\s *$$//g"

.PHONY: yaml-lint
yaml-lint: ## Perform linting against ansible yaml files
	@echo "[*] Performing YAML Lint."
	@. ./venv/bin/activate
	@find ./ansible/ \( -name *.yaml -o -name *.yml \) -exec ansible-lint -x ANSIBLE0012 {} +

.PHONY: py-lint
py-lint: ## Perform linting against py files
	@echo "[*] Performing PyLint."
	@. ./venv/bin/activate
	@find $$YAMLROOT \( -path ./venv -prune -o -name *.py \) -exec pylint {} +

.PHONY: install-py3.6
install-py3.6: ## Install Python3.6
	@echo "[*] Installing Py3.6."
	sudo add-apt-repository ppa:jonathonf/python-3.6
	sudo apt update
	sudo apt install python3.6 python3-pip
	sudo -H pip3 install --upgrade pip
	curl https://bootstrap.pypa.io/get-pip.py | sudo -H python3.6

.PHONY: add-venv-py3.6
add-venv-py3.6: ## Install virtualenv, create virtualenv, install requirements
	@echo "[*] Installing/creating virtualenv and deps (Python3.6)"
	pip3.6 install virtualenv
	virtualenv -p /usr/bin/python3.6 venv
	. ./venv/bin/activate
	venv/bin/pip3.6 install -q -r ./requirements.txt

.PHONY: add-venv-py2.7
add-venv-py2.7: ## Install virtualenv, create virtualenv, install requirements
	@echo "[*] Installing/creating virtualenv and deps (Python2.7)"
	pip2.7 install virtualenv
	virtualenv -p /usr/bin/python2.7 venv
	. ./venv/bin/activate
	venv/bin/pip2.7 install -q -r ./requirements.txt

.PHONY: lint
lint: ## Remove YAML EOL spaces, perform yaml and py linting.
lint:   remove-yml-eol-spaces yaml-lint py-lint

# :%s/^[ ]\+/\t/g - automatically replace all tabs with spaces
