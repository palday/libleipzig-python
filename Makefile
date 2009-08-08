PYTHON = python
.PHONY: install build dist test clean distclean

install:
	$(PYTHON) setup.py install

build:
	$(PYTHON) setup.py build

dist:
	$(PYTHON) setup.py sdist

test:
	@nosetests --with-doctest --doctest-extension=rst --detailed-errors

docs: README.rst
	@mkdir -p docs
	rst2html README.rst docs/index.html

clean:
	find . -name '*.py[co]' -exec rm -f {} ';'
	rm -rf docs/ build/ dist/
	rm -f MANIFEST

distclean: clean
	rm -rf /tmp/suds/
