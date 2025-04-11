# Ruta al entorno virtual
VENV=.venv
PYTHON=$(VENV)/bin/python
PREFECT=$(VENV)/bin/prefect
PIP=$(VENV)/bin/pip

cloud-login:
	@echo "🔑 Prefect login..."
	@$(PREFECT) cloud login

install:
	@echo "📦 Installing dependencies..."
	$(PIP) install -r document_me/requirements.txt

watcher:
	$(PYTHON) -m document_me.watcher ${MODEL_NAME:-llama3}

venv:
	@test -d $(VENV) || python3 -m venv $(VENV)
	@echo "Virtual environment ready."

setup: venv install

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

.PHONY: huggingface-login cloud-login install watcher venv setup clean
