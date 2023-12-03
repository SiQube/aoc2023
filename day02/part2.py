from __future__ import annotations

import os.path
import re

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    ret = 0
    for line in inp.splitlines():
        max_dict = {
            'red': 1,
            'green': 1,
            'blue': 1,
        }
        for _game in line.split('; '):
            game = re.sub(r'Game \d+: ', '', _game)
            for details in game.split(', '):
                _number, color = details.split()
                number = int(_number)
                if number > max_dict[color]:
                    max_dict[color] = number

        mult = 1
        for fact in max_dict.values():
            mult *= fact

        ret += mult

    return ret


_TESTS = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
_EXPECTED = 2286


@pytest.mark.parametrize(
    ('input_str', 'expected'),
    (
        (_TESTS, _EXPECTED),
    ),
)
def test(input_str: str, expected: int) -> None:
    assert _solve(input_str) == expected


def main() -> int:
    with open(_INPUT) as fp:
        print(_solve(fp.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
