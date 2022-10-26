.PHONY: help install_mamba install_macos install_linux update_macos update_linux
.DEFAULT_GOAL = help

PYTHON = python
VERSION = 3.8
NAME = py_name
ROOT = ./
PIP = pip
CONDA = conda
SHELL = bash
PKGROOT = alti_tools
TESTS = ${ROOT}tests
ENVS = ${ROOT}environments

help:	## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)



##@ Installation
install_mamba: ## Install mamba in base environment
	conda install mamba -n base

install_macos: ## Install conda env in MACOS
	mamba env create -f ${ENVS}/macos.yaml

install_linux: ## Install conda env in Linux
	mamba env create -f ${ENVS}/linux.yaml

update_macos: ## Update conda env in MACOS
	mamba env update -f ${ENVS}/macos.yaml

update_linux: ## Update conda env in linux
	mamba env update -f ${ENVS}/linux.yaml

install_precommit: ## Install precommit tools
	mamba install pre-commit -c conda-forge
	pre-commit install --all-files

##@ Formatting
black:  ## Format code in-place using black.
	black ${PKGROOT}/ ${TESTS} -l 79 .

isort:  ## Format imports in-place using isort.
	isort ${PKGROOT}/ ${TESTS}

format: ## Code styling - black, isort
		black ${PKGROOT}/ ${TESTS} -l 79 .
		@printf "\033[1;34mBlack passes!\033[0m\n\n"
		isort ${PKGROOT}/ ${TESTS}
		@printf "\033[1;34misort passes!\033[0m\n\n"

##@ Testing
test:  ## Test code using pytest.
	@printf "\033[1;34mRunning tests with pytest...\033[0m\n\n"
	pytest -v ${PKGROOT}/ ${TESTS}
	@printf "\033[1;34mPyTest passes!\033[0m\n\n"

##@ JupyterBook
jb_build: ## Build Jupyterbook
	rm -rf jb/_build/
	jupyter-book build jb --all

jb_clean: ## Clean JupyterBook
	jupyter-book clean jb

##@ Documentation
build_docs:  ## Build the documentation
	@echo "\n=== pip install doc requirements =============="
	pip install -r docs/docs_requirements.txt
	pip install --upgrade "Jinja2<3"
	@echo "\n=== install pandoc =============="
ifeq ("$(UNAME_S)", "Linux")
	$(eval TEMP_DEB=$(shell mktemp))
	@echo "Checking for pandoc installation..."
	@(which pandoc) || ( echo "\nPandoc not found." \
	  && echo "Trying to install automatically...\n" \
	  && wget -O "$(TEMP_DEB)" $(PANDOC_DEB) \
	  && echo "\nInstalling pandoc using dpkg -i from $(PANDOC_DEB)" \
	  && echo "(If this step does not work, manually install pandoc, see http://pandoc.org/)\n" \
	  && sudo dpkg -i "$(TEMP_DEB)" \
	)
	@rm -f "$(TEMP_DEB)"
endif
ifeq ($(UNAME_S),Darwin)
	brew install pandoc
endif
	@echo "\n=== build docs =============="
	(cd docs ; make html)
	@echo "\n${SUCCESS}=== Docs are available at docs/_build/html/index.html ============== ${SUCCESS}"