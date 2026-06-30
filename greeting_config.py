"""greeting_config.py — 挨拶の接頭辞を設定ファイルから読む loader。

greeting.txt の先頭行を接頭辞として返す。ファイルが無い・空のときは
フォールバック接頭辞を返す。hello.py から loader 経由で利用される。
"""

from pathlib import Path

DEFAULT_PREFIX = "[team-dev-kit]"
CONFIG_FILE = "greeting.txt"


def load_prefix(path: str = CONFIG_FILE) -> str:
    """greeting.txt の先頭行を接頭辞として返す。無い・空なら DEFAULT_PREFIX。"""
    config = Path(path)
    if not config.exists():
        return DEFAULT_PREFIX
    lines = config.read_text(encoding="utf-8").splitlines()
    prefix = lines[0].strip() if lines else ""
    return prefix or DEFAULT_PREFIX
