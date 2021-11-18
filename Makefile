.PHONY: build
build:
	docker run -t -v $${PWD}:/src -w /src python:3.10 python setup.py bdist_wheel