import seasons
import datetime


def test_seasons():
    assert seasons.get_minutes_between_dates(datetime.datetime(1990, 1, 1), datetime.datetime(1990, 1, 1)) == 0
    assert seasons.get_minutes_between_dates(datetime.datetime(1990, 1, 1), datetime.datetime(1990, 1, 2)) == 1440
    assert seasons.get_minutes_between_dates(datetime.datetime(1992, 3, 15), datetime.datetime(2024, 8, 4)) == 17035200
    assert not seasons.get_minutes_between_dates(datetime.datetime(1992, 3, 15), datetime.datetime(2024, 8, 4)) == 0
