import pytest

from game.comparator import is_same


def test_perfect_equality():
    first = "Ain't no moutain high enough"
    assert is_same(first, first)


def test_case():
    assert is_same('ABC', 'abc')
    assert is_same('abc', 'ABC')
    assert is_same('aBc', 'AbC')
    assert is_same('AbC', 'aBc')


def test_ignore_punctuation():
    first = "Ain't no moutain, high? enough!"
    second = "Ain't no moutain high enough"
    assert is_same(first, second)
    assert is_same(second, first)


def test_ignore_symbols():
    first = """Ain't no moutain "high" enough"""
    second = "Aint no moutain high enough"
    assert is_same(first, second)
    assert is_same(second, first)


def test_ignore_double_space():
    first = "Happy  Together"
    second = "Happy Together"
    assert is_same(first, second)
    assert is_same(second, first)


def test_ignore_trailing_space():
    first = "   Happy Together "
    second = "Happy Together"
    assert is_same(first, second)
    assert is_same(second, first)

def test_ignore_accents():
    first =  "àáâãäåçèéêëìíîïñòóôõöùúûüýÿ"
    second = "aaaaaaceeeeiiiinooooouuuuyy"
    assert is_same(first, second)
    assert is_same(second, first)
