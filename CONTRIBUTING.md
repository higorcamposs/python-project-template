# Contribuindo

Obrigado pelo interesse em contribuir!

## Pré-requisitos
- Python 3.11+
- Git e Make instalados
- Docker (opcional)

## Como começar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/python-project-template.git
   cd python-project-template
   ```
2. Crie o ambiente:
   ```bash
   ./scripts/bootstrap.sh
   ```
3. Rode a aplicação:
   ```bash
   make run
   ```

## Testes e Qualidade
Antes de enviar qualquer mudança:
```bash
make format   # formata código (Ruff + Black)
make lint     # checa qualidade e tipagem
make test     # roda testes unitários
```

## Commits
Use o padrão **Conventional Commits**:
- feat: nova funcionalidade
- fix: correção de bug
- docs: apenas documentação
- chore: ajustes menores

Exemplo:
```bash
git commit -m "feat(cli): adiciona comando hello world"
```

## Pull Requests
- Abra PRs sempre contra a branch `main`
- Descreva claramente as mudanças
- Garanta que o CI passou
- Um revisor precisa aprovar antes do merge

---

Se tiver dúvidas, abra uma [Issue](../../issues) e a gente conversa 😃
