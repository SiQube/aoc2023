from __future__ import annotations

import os.path
import re

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    str_to_int = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    pattern = re.compile(fr"(\d|{'|'.join(str_to_int)})")
    rev_pattern = re.compile(fr"(\d|{'|'.join(s[::-1] for s in str_to_int)})")
    calibration_value = 0
    for line in inp.splitlines():
        _first = pattern.search(line)
        assert _first is not None
        first = _first[0]
        _last = rev_pattern.search(line[::-1])
        assert _last is not None
        last = _last[0][::-1]
        digits = [str_to_int.get(first, first), str_to_int.get(last, last)]
        calibration_value += int(digits[0]) * 10 + int(digits[-1])

    return calibration_value


_TESTS = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
_EXPECTED = 281


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
