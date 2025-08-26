content = r"""SHELL := /bin/bash

.PHONY: help venv install ensure-venv init lint format test cov run clean

## Mostra os alvos disponíveis
help:
	@echo "make install              - cria venv e instala dependências (prod + dev)"
	@echo "make init name=meu_app    - renomeia pacote (my_project->meu_app) e roda bootstrap"
	@echo "make run                  - executa a aplicação (python -m <pacote>)"
	@echo "make lint                 - checa qualidade (ruff/black/mypy)"
	@echo "make format               - formata código (ruff format + black)"
	@echo "make test                 - executa testes com pytest"
	@echo "make cov                  - executa testes com cobertura (xml + htmlcov/)"
	@echo "make clean                - remove caches e artefatos"

# Cria ambiente virtual
venv:
	python3 -m venv .venv

# Instala dependências (produção + dev)
install: venv
	. .venv/bin/activate && pip install -U pip && pip install -e .[dev]

# Garante que a venv existe/está pronta antes de rodar outros alvos
ensure-venv:
	@test -d .venv || $(MAKE) install

# Inicializa um novo projeto (rename + bootstrap)
init:
	@if [ -z "$(name)" ]; then \
		echo "Uso: make init name=novo_nome"; \
		exit 1; \
	fi
	python scripts/rename_package.py $(name)
	./scripts/bootstrap.sh

# Verifica qualidade do código
lint: ensure-venv
	. .venv/bin/activate && ruff check . && ruff format --check . && black --check . && mypy src/

# Formata código automaticamente
format: ensure-venv
	. .venv/bin/activate && ruff format . && ruff check . --fix && black .

# Roda testes unitários e integração
test: ensure-venv
	. .venv/bin/activate && pytest

# Testes com cobertura (gera xml e html)
cov: ensure-venv
	. .venv/bin/activate && pytest --cov=src --cov-report=term-missing --cov-report=xml --cov-report=html

# Executa a aplicação
run: ensure-venv
	. .venv/bin/activate && python -m my_project

# Limpa caches e artefatos
clean:
	rm -rf .venv .mypy_cache .ruff_cache .pytest_cache dist build coverage.xml htmlcov
with open("/mnt/data/Makefile", "w") as f:
	f.write(content)
