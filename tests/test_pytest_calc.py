import calc
import pytest
import sys


@pytest.mark.skipif(sys.version_info[0] < 3, reason='Because I can')
def test_add():
    assert calc.add(10, 5) == 15
    assert calc.add(-5, 5) == 0
    assert calc.add(-10, -5) == -15


@pytest.mark.string
def test_add_string():
    assert calc.add_string('aaa', 'bbb') == 'aaabbb'
    assert type(calc.add_string('aaa', 'bbb')) is str


@pytest.mark.number
def test_subtract():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-5, 5) == -10
    assert calc.subtract(-10, -5) == -5


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (2, 4, 6),
                             (2.5, 3.5, 6),
                             ('Lubie', ' placki', 'Lubie placki')
                         ]
                         )
def test_add_2(num1, num2, result):
    # print(f'add({num1}, {num2}) = {result}')
    assert calc.add(num1, num2) == result
