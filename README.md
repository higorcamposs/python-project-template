![CI](https://github.com/seu-usuario/python-project-template/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


# 🐍 Python Project Template

Um template moderno para iniciar projetos em **Python**, seguindo boas práticas da comunidade.  
Inclui estrutura organizada com **src layout**, testes automatizados, Docker, Makefile, scripts de bootstrap, documentação e CI/CD.

---

## 📂 Estrutura do Projeto

```text
.
├── CHANGELOG.md          # Histórico de alterações (semver + keepachangelog)
├── CONTRIBUTING.md       # Guia de contribuição
├── docker/
│   └── Dockerfile        # Build de imagem Docker
├── docs/
│   └── index.md          # Documentação inicial (ex: mkdocs ou sphinx)
├── LICENSE               # Licença do projeto
├── Makefile              # Atalhos para tarefas comuns (lint, test, run, etc.)
├── README.md             # Este arquivo
├── scripts/
│   ├── bootstrap.sh      # Setup inicial do ambiente
│   └── devserver.sh      # Script de execução em modo dev
├── src/
│   └── my_project/       # Código principal da aplicação
│       ├── cli.py        # CLI usando Typer/Click
│       ├── core/         # Módulos de domínio
│       │   └── __init__.py
│       ├── __init__.py
│       └── __main__.py   # Permite rodar com `python -m my_project`
└── tests/
    ├── integration/      # Testes de integração
    └── unit/             # Testes unitários
```

---

## 🚀 Primeiros Passos

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/python-project-template.git
cd python-project-template
```

### 2. Criar ambiente virtual e instalar dependências
```bash
./scripts/bootstrap.sh
```

### 3. Ativar ambiente virtual
```bash
source .venv/bin/activate
```

### 4. Rodar a aplicação
```bash
python -m my_project
```

---

## 🧪 Rodando Testes

```bash
make test
```

Com relatório de cobertura:
```bash
make cov
```

---

## 🐳 Docker

### Build da imagem
```bash
docker build -t my_project -f docker/Dockerfile .
```

### Executar container
```bash
docker run --rm -it my_project
```

---

## ⚙️ Makefile (atalhos úteis)

- `make install` → Instala dependências  
- `make lint` → Verifica qualidade do código (Ruff, Black, Mypy)  
- `make format` → Formata o código  
- `make test` → Roda os testes  
- `make cov` → Roda testes com cobertura  
- `make run` → Executa a aplicação  

---

## 📖 Documentação

A documentação pode ser expandida no diretório `docs/`.  
Sugestão: usar [MkDocs](https://www.mkdocs.org/) com tema [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

---

## 🤝 Contribuindo

Contribuições são bem-vindas!  
Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para saber como contribuir.

---

## 📌 Roadmap (sugestão)

- [ ] Adicionar `pyproject.toml` com dependências base  
- [ ] Configurar `pre-commit` (Ruff, Black, Mypy)  
- [ ] Adicionar GitHub Actions/GitLab CI  
- [ ] Adicionar exemplos de testes unitários e integração  
- [ ] Publicar documentação com MkDocs  

---

## 📜 Licença

Distribuído sob a licença [MIT](LICENSE).