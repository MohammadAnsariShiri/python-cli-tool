import pytest
from scorekeeper.stats import average, best


def test_average_normal():
    rows = [('Ali', 10.0), ('Sara', 20.0)]
    assert average(rows) == 15.0


def test_average_empty_list():
    assert average([]) == 0.0


def test_average_floats():
    rows = [('Ali', 17.5), ('Sara', 18.9), ('Neda', 16.4)]
    assert average(rows) == pytest.approx(17.6)


def test_best_normal():
    rows = [('Ali', 17.5), ('Sara', 18.9), ('Neda', 16.4)]
    assert best(rows) == ('Sara', 18.9)


def test_best_empty_list():
    assert best([]) is None


def test_best_single_item():
    assert best([('Ali', 15.0)]) == ('Ali', 15.0)