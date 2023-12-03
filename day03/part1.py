from __future__ import annotations

import itertools
import os.path
import re

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _check_for_symbol(
        tup: tuple[int, int],
        part_positions: list[tuple[int, int]],
) -> bool:
    for direction in itertools.product([-1, 0, 1], [-1, 0, 1]):
        _tup = (tup[0] + direction[0], tup[1] + direction[1])
        if _tup in part_positions:
            return True
    return False


def _solve(inp: str) -> int:
    ret = 0
    part_positions = []
    for line_id, line in enumerate(inp.splitlines()):
        for char_id, char in enumerate(line):
            if not char.isdigit() and char != '.':
                part_positions.append((line_id, char_id))

    for line_id, line in enumerate(inp.splitlines()):
        spans = [(int(match[0]), match.span())
                 for match in re.compile(r'\d+').finditer(line)]
        for value, span in spans:
            part_check = False
            for char_id in range(span[0], span[1]):
                part_check = _check_for_symbol(
                    (line_id, char_id), part_positions,
                )
                if part_check:
                    break
            if part_check:
                ret += value

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
_EXPECTED = 4361


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
