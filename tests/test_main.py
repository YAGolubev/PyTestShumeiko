import pytest

from src.main import Calculator


@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (5, -1, -5),
    ],
)
def test_devide(x, y, res):
    assert Calculator().devide(x, y) == res


@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 3),
        (5, -1, 4),
    ],
)
def test_add(x, y, res):
    assert Calculator().add(x, y) == res
