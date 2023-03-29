from sample_package import sample
from unittest import mock
import pytest


def test_sample():
    result = sample.hello()
    assert result == 4


@pytest.mark.parametrize("input1, input2, expected", [(3, 2, 5), (1, 4, 5), (5, 3, 8)])
def test_add(input1, input2, expected):
    result = sample.add(input1, input2)
    assert result == expected


def test_divide():
    result = sample.divide(8, 2)
    assert result == 4
    with pytest.raises(ZeroDivisionError):
        result = sample.divide(10, 0)


@mock.patch("sample_package.sample.randint", return_value=7)
def test_random(mocked_randint):
    result = sample.play_random()
    assert result == "größer"


def test_productionclass():
    instanz = sample.ProductionClass()
    instanz.something = mock.MagicMock()
    instanz.method()
    instanz.something.assert_called_once_with(1, 2, 3)
