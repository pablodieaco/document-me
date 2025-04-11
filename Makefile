# Ruta al entorno virtual
VENV=.venv
PYTHON=$(VENV)/bin/python
PREFECT=$(VENV)/bin/prefect
PIP=$(VENV)/bin/pip

MODEL_NAME ?= llama3
INPUT_FOLDER ?= ./scripts
OUTPUT_FOLDER ?= ./documented_scripts

cloud-login:
	@echo "🔑 Prefect login..."
	@$(PREFECT) cloud login

install:
	@echo "📦 Installing dependencies..."
	$(PIP) install -r document_me/requirements.txt

watcher:

	$(PYTHON) -m document_me.watcher --model_name $(MODEL_NAME) --input_folder $(INPUT_FOLDER) --output_folder $(OUTPUT_FOLDER)

venv:
	@test -d $(VENV) || python3 -m venv $(VENV)
	@echo "Virtual environment ready."

setup: venv install

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

.PHONY: huggingface-login cloud-login install watcher venv setup clean
