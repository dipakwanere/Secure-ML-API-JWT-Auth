install:
	python -m pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv tests/test_*.py
	#tests/ --cov=src/ --cov-report=term-missing --verbose

format:
	black .

# train:
# 	python src/train.py

# build:
# 	docker build -t mlops-project:latest .

# run:
# 	docker run --rm mlops-project:latest

# clean:
# 	rm -rf __pycache__ .pytest_cache models/*


all: install lint test format