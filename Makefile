package:
	python3 setup.py sdist bdist_wheel

install:
	pip3 install -e .

publish:
	twine upload dist/*

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache