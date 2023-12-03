from __future__ import annotations

import itertools
import os.path
import re

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _check_for_gear(
        tup: tuple[int, int],
        number_positions: dict[tuple[int, int], int],
) -> set[int]:
    matched_numbers = set()
    for direction in itertools.product([-1, 0, 1], [-1, 0, 1]):
        _tup = (tup[0] + direction[0], tup[1] + direction[1])
        for key, value in number_positions.items():
            if _tup == key:
                matched_numbers.add(value)
    return matched_numbers


def _solve(inp: str) -> int:
    ret = 0
    number_positions = {}
    for line_id, line in enumerate(inp.splitlines()):
        spans = [(int(match[0]), match.span())
                 for match in re.compile(r'\d+').finditer(line)]
        for value, span in spans:
            for pos in range(span[0], span[1]):
                number_positions[(line_id, pos)] = value

    for line_id, line in enumerate(inp.splitlines()):
        for char_id, char in enumerate(line):
            if char == '*':
                adj_numbers = _check_for_gear(
                    (line_id, char_id), number_positions,
                )
                if len(adj_numbers) == 2:
                    mult = 1
                    for num in adj_numbers:
                        mult *= num
                    ret += mult

    return ret


_TESTS = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
_EXPECTED = 467835


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
