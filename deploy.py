# -*- coding: utf-8 -*-

from pathlib import Path

dotfiles_dir = Path.cwd() / Path("home")
home_dir = Path.home()

for p in dotfiles_dir.iterdir():
    print(f"Working on {p}")
    symlink_path = home_dir / Path(f".{p.name}")
    if symlink_path.is_symlink():
        print(f"Deleting old symlink {symlink_path}")
        symlink_path.unlink()
    elif symlink_path.is_file() or symlink_path.is_dir():
        raise Exception(f"{symlink_path} already exists and is NOT a symlink!")
    print(f"Will make symlink at path {symlink_path} -> {p} where directory={p.is_dir()}")
    symlink_path.symlink_to(p, target_is_directory=p.is_dir())
    if not symlink_path.exists():
        raise Exception("New symlink doesn't exist!")
