from twttr import shorten


def test_shorten():
    assert shorten("Test") == "Tst"
    assert shorten("tweet") == "twt"
    assert shorten("TWEET") == "TWT"
    assert shorten("MyDayWasGoodHowbutYours?") == "MyDyWsGdHwbtYrs?"
    assert shorten("Test1") == "Tst1"
    assert shorten("Test1.") == "Tst1."
