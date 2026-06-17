"""hello.py — 起動時に挨拶を表示するサンプル。

引数で名前を渡すとその名前で挨拶する。空文字・空白のみは拒否する。
"""

import sys


def greet(name: str = "team-dev-kit") -> str:
    if not name.strip():
        raise ValueError("name must not be empty")
    return f"hello, {name}"


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "team-dev-kit"
    try:
        print(greet(name))
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
