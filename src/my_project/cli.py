import os

from dotenv import load_dotenv
import typer

app = typer.Typer(help="CLI do projeto base.")
load_dotenv()


@app.callback()
def main():
    """Inicialização da CLI (carrega .env, etc)."""
    pass


@app.command()
def hello(name: str = "world"):
    """Exibe uma saudação simples."""
    typer.echo(f"Hello, {name}!")


@app.command()
def env():
    """Mostra variáveis básicas carregadas do .env."""
    typer.echo(f"APP_ENV={os.getenv('APP_ENV')}")
    typer.echo(f"LOG_LEVEL={os.getenv('LOG_LEVEL')}")


if __name__ == "__main__":
    app()
