import os


def check_dir(name: str) -> None:
    """{name}ディレクトリが存在するか確認し、存在しない場合は作成する"""
    if not os.path.exists(f"{name}"):
        os.mkdir(f"{name}")
