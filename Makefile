auto:
	python3 setup.py sdist

install:
	tar -xzf dist/*.tar.gz
	
	sudo python3 help-*/setup.py install

	rm -r help-*

clean:
	rm -rf build
	rm -rf help.egg*
	rm -rf dist
	
