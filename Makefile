install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff