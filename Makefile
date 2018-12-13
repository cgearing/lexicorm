.PHONY: test-unit
test-unit:
	pipenv run pytest tests/unit data_pipeline --doctest-modules

test-behave:
	pipenv run behave test/e2e --format=progress

.PHONY:  test-unit test-behave
test-local: test-unit test-behave

.PHONY: lint pep8 pyflakes mypy
lint: pep8 pyflakes mypy

pep8:
	pipenv run pycodestyle lexicorm

pyflakes:
	pipenv run pyflakes lexicorm

mypy:
	pipenv run mypy --package lexicorm --strict --ignore-missing-imports