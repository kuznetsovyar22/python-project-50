install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests/test_gendiff.py

test-coverage:
	poetry run pytest --cov --cov-report lcov