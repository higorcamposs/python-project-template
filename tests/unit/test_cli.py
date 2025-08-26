from typer.testing import CliRunner
from my_project.cli import app

runner = CliRunner()

def test_hello_default():
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello, world!" in result.stdout
