from __future__ import annotations

import os.path
import re

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    max_dict = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    ret = 0
    for line in inp.splitlines():
        game_id = int(line.split(':')[0].split()[1])
        valid_game = True
        for _game in line.split('; '):
            game = re.sub(r'Game \d+: ', '', _game)
            for details in game.split(', '):
                number, color = details.split()
                if int(number) > max_dict[color]:
                    valid_game = False

                if not valid_game:
                    break
        if valid_game:
            ret += game_id

    return ret


_TESTS = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
_EXPECTED = 8


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
