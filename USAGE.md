# Guia de Uso do Template Python

Este repositório é um **template** para iniciar novos projetos Python.

---

## 🚀 Como usar

1. Crie um novo repositório a partir deste template (GitHub → "Use this template").
2. Clone o repositório criado:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-projeto.git
   cd nome-do-projeto
   ```
3. Renomeie o pacote `my_project` para o nome real:
   ```bash
   python scripts/rename_package.py nome_do_projeto
   ```
4. Configure o ambiente:
   ```bash
   ./scripts/bootstrap.sh
   ```
5. Ative o ambiente:
   ```bash
   source .venv/bin/activate
   ```
6. Rode a aplicação:
   ```bash
   make run
   ```
7. Rode testes e lint:
   ```bash
   make lint
   make test
   ```

---

## 🐳 Docker

Para buildar e rodar a aplicação em container:

```bash
docker build -t nome-do-projeto -f docker/Dockerfile .
docker run --rm -it nome-do-projeto
```

Se for expor portas (exemplo: APIs em 8000):

```bash
docker run --rm -it -p 8000:8000 nome-do-projeto
```

---

## 📌 Checklist inicial

- [ ] Editar `pyproject.toml` → `[project] name` e `[project.scripts]`  
- [ ] Ajustar `Makefile` (`make run`) para o novo nome  
- [ ] Criar `.env` a partir de `.env.example`  
- [ ] Atualizar `README.md` com descrição do novo projeto  
- [ ] Subir o repositório e verificar se o CI passou

---

## 💡 Dicas

- Use `make init name=novo_nome` (se configurado) para automatizar a inicialização.  
- Sempre rode `make lint && make test` antes de commitar.  
- Para contribuir, siga as orientações em [CONTRIBUTING.md](CONTRIBUTING.md).  