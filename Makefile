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