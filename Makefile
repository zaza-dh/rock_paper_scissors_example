venv:
	pip3.6 install virtualenv
	python3.6 -m virtualenv venv36
	. venv36/bin/activate
	pip3.6 install -r requirements.txt

test: venv
	pytest --cov-report html --cov-config .coveragerc --cov rock_paper_scissors
	@echo 'Find the coverage report under: htmlcov/index.html'

install:
	pip install -e .

lint:
	flake8 rock_paper_scissors || isort --recursive .