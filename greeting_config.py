"""greeting_config.py — 挨拶の接頭辞を設定ファイルから読む loader。

greeting.txt の 1 行目を接頭辞として返す。ファイルが無い・空のときは
既定値を返すため、呼び出し側は常に文字列を受け取れる。
"""

from pathlib import Path

DEFAULT_PREFIX = "Hello"
CONFIG_FILE = "greeting.txt"


def load_prefix(config_path: str | Path = CONFIG_FILE) -> str:
    """greeting.txt から接頭辞を読む。無い／空なら DEFAULT_PREFIX を返す。"""
    path = Path(config_path)
    if not path.is_file():
        return DEFAULT_PREFIX
    prefix = path.read_text(encoding="utf-8").strip()
    return prefix or DEFAULT_PREFIX
