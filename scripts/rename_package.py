#!/usr/bin/env python3
import os
import pathlib
import sys


def rename_package(old: str, new: str):
    root = pathlib.Path(__file__).resolve().parents[1]

    # Renomeia a pasta do pacote
    old_path = root / "src" / old
    new_path = root / "src" / new
    if old_path.exists():
        os.rename(old_path, new_path)

    # Substitui referências nos arquivos
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in {".py", ".toml", ".md", ".yml", ".yaml", ""}:
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception:
                continue
            changed = txt.replace(old, new)
            if changed != txt:
                p.write_text(changed, encoding="utf-8")

    # Atualiza pyproject.toml (packages e coverage)
    pyproj = root / "pyproject.toml"
    if pyproj.exists():
        txt = pyproj.read_text(encoding="utf-8")
        txt = txt.replace(f'packages = ["src/{old}"]', f'packages = ["src/{new}"]')
        txt = txt.replace(f'source = ["src/{old}"]', f'source = ["src/{new}"]')
        pyproj.write_text(txt, encoding="utf-8")

    print(f"✅ Pacote renomeado: {old} -> {new}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/rename_package.py novo_nome")
        sys.exit(1)

    old_name = "my_project"
    new_name = sys.argv[1]
    rename_package(old_name, new_name)
