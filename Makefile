.PHONY: test

test:
	pipenv run behave test/e2e --format=progress

.PHONY: lint pep8 pyflakes mypy
lint: pep8 pyflakes mypy

pep8:
	pipenv run pycodestyle lexicorm

pyflakes:
	pipenv run pyflakes lexicorm

mypy:
	pipenv run mypy --package lexicorm --strict --ignore-missing-imports

deploy: deploy-clean deploy-build deploy-deploy

deploy-clean:
	rm -rf build/ dist/ genyrator.egg-info/
deploy-build:
	pipenv run python setup.py sdist bdist_wheel

deploy-deploy:
	pipenv run twine upload --repository-url https://test.pypi.org/legacy/ dist/*
