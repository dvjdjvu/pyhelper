auto:
	python3 setup.py sdist

install:
	tar -xzf dist/*.tar.gz
	
	sudo python3 helper-*/setup.py install

	sudo rm -rf helper-*

clean:
	rm -rf build
	rm -rf helper.egg*
	rm -rf dist
	rm -rf helper-*

build:
	sudo pip3 install wheel
	python3 setup.py bdist_wheel
	
