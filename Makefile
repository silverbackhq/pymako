PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
COVERAGE ?= coverage


help: Makefile
	@echo
	@echo " Choose a command run in Silverback:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo


## config: Install dependencies.
config:
	$(PIP) install pycodestyle
	$(PIP) install coverage
	$(PIP) install flake8
	$(PIP) install twine


## lint-pycodestyle: PyCode Style Lint
lint-pycodestyle:
	@echo "\n==> Pycodestyle Linting:"
	@find pymako -type f -name \*.py | while read file; do echo "$$file" && pycodestyle --config=./pycodestyle --first "$$file" || exit 1; done


## lint-flake8: Flake8 Lint.
lint-flake8:
	@echo "\n==> Flake8 Linting:"
	@find pymako -type f -name \*.py | while read file; do echo "$$file" && flake8 --config=flake8.ini "$$file" || exit 1; done


## lint: Lint The Code.
lint: lint-pycodestyle lint-flake8
	@echo "\n==> All linting cases passed!"


## test: Run Test Cases.
test:
	@echo "\n==> Run Test Cases:"
	$(PYTHON) setup.py test


## coverage: Get test coverage.
coverage:
	$(COVERAGE) run --source='.' setup.py test
	$(COVERAGE) report -m


## ci: Run all CI tests.
ci: test coverage lint
	@echo "\n==> All quality checks passed"


## build: Build package.
build:
	rm -rf build dist
	$(PYTHON) setup.py sdist bdist_wheel


## upload: Upload package to test pypi.
upload:
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*


## release: Upload package to production pypi.
release:
	$(PYTHON) -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


## test_install: Install package from test pypi.
test_install:
	$(PYTHON) -m pip install --index-url https://test.pypi.org/simple/ pymako


## install: Install package from production pypi.
install:
	$(PYTHON) -m pip install pymako


## develop: Develop install.
develop:
	$(PYTHON) setup.py develop


.PHONY: ci
