from um import count


def test_single_um():
    assert count("hello, um, world") == 1


def test_multiple_um():
    assert count("um, thanks, um...") == 2


def test_case_insensitive():
    assert count("Um, thanks for the tip.") == 1


def test_substring():
    assert count("yummy") == 0


def test_multiple_words():
    assert count("Um... um, okay, um, nevermind.") == 3


def test_surrounded_by_letters():
    assert count("umumum") == 0


def test_surrounded_by_punctuation():
    assert count("Hello... um, world!") == 1
