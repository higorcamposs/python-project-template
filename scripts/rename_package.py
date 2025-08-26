#!/usr/bin/env python3
import os
import sys
import pathlib

def rename_package(old: str, new: str):
    root = pathlib.Path(__file__).resolve().parents[1]

    # Renomeia a pasta do pacote
    old_path = root / "src" / old
    new_path = root / "src" / new
    if old_path.exists():
        os.rename(old_path, new_path)

    # Percorre arquivos e substitui referências
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in {".py", ".toml", ".md", ".yml", ".yaml", ""}:
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception:
                continue
            if old in txt:
                txt = txt.replace(old, new)
                p.write_text(txt, encoding="utf-8")

    print(f"✅ Pacote renomeado: {old} -> {new}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/rename_package.py novo_nome")
        sys.exit(1)

    old_name = "my_project"
    new_name = sys.argv[1]
    rename_package(old_name, new_name)