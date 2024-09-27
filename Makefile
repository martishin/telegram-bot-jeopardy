# Variables
PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip
PYTHON_VENV := $(VENV)/bin/python
PYTEST := $(VENV)/bin/pytest
BOT_FILE := bot.py
TRAIN_FILE := ml/train.py
TEST_DIR := tests

# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make create-venv     Create virtual environment."
	@echo "  make install-deps    Install dependencies."
	@echo "  make run-bot         Run the Telegram bot."
	@echo "  make train-model     Train the model."
	@echo "  make test            Run the tests."

.PHONY: create-venv
create-venv:
	@echo "Creating virtual environment in $(VENV)..."
	$(PYTHON) -m venv $(VENV) && \
	source $(VENV)/bin/activate && \
	$(PIP) install -r requirements.txt && \
  	echo "Environment created and dependencies installed."

.PHONY: train-model
train-model:
	@echo "Training the model..."
	$(PYTHON_VENV) $(TRAIN_FILE)

.PHONY: run-bot
run-bot:
	@echo "Running the Telegram bot..."
	$(PYTHON_VENV) $(BOT_FILE)

.PHONY: test
test:
	@echo "Running tests..."
	$(PYTEST) $(TEST_DIR)

.PHONY: build
build:
	@echo "Building Docker container..."
	docker build -t telegram-bot-jeopardy .

.PHONY: run
run:
	@echo "Running Docker container..."
	docker run --env-file .env telegram-bot-jeopardy
