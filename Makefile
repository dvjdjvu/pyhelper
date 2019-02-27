auto:
	python3 setup.py sdist

install:
	tar -xzf dist/*.tar.gz
	
	sudo python3 helper-*/setup.py install

	sudo rm -rf helper-*

clean:
	rm -rf build
	rm -rf help.egg*
	rm -rf dist
	rm -rf helper-*
	
