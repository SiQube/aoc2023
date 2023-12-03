from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    calibration_value = 0
    for line in inp.splitlines():
        digits = [char for char in line if char.isdigit()]
        calibration_value += int(digits[0] + digits[-1])

    return calibration_value


_TESTS = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
_EXPECTED = 142


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
