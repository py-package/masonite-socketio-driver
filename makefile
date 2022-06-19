publish: ## Publish package to pypi
	python setup.py sdist bdist_wheel
	twine upload dist/* --verbose
	rm -fr build dist .egg src/masonite_audit.egg-info