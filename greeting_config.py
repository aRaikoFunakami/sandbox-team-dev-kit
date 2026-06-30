"""greeting_config.py — greeting.txt から挨拶の接頭辞を読む loader。

接頭辞は同ディレクトリの greeting.txt に置く。ファイルが無い・空のときは
空文字を返し、呼び出し側で従来どおりの挨拶にフォールバックできるようにする。
"""

from pathlib import Path

CONFIG_FILE = "greeting.txt"


def load_prefix() -> str:
    """greeting.txt の接頭辞を返す。不在・空なら空文字。"""
    path = Path(__file__).resolve().parent / CONFIG_FILE
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8").strip()
