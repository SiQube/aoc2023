from __future__ import annotations

import math
import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    game_dict = {game_id: 1 for game_id in range(1, len(inp.splitlines())+1)}
    for line_id, line in enumerate(inp.splitlines()):
        matches = []
        _card_id, draws = line.split(': ')
        card_id = int(_card_id.split()[1])
        _win_numbs, _draw = draws.split('|')
        win_numbs = [int(numb) for numb in _win_numbs.split()]
        draw = [int(numb) for numb in _draw.split()]
        for numb in draw:
            if numb in win_numbs:
                matches.append(numb)
        if matches:
            for _ in range(game_dict[card_id]):
                for match_idx in range(len(matches)):
                    try:
                        game_dict[card_id + match_idx + 1] += 1
                    except KeyError:
                        break

    return int(math.fsum(game_dict.values()))


_TESTS = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
_EXPECTED = 30


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
