# https://github.com/DRMacIver/hypothesis/blob/master/docs/examples.rst
# pip install hypothesis
# pip install pytz


from hypothesis import given, Settings
from hypothesis.extra.datetime import datetimes
from hypothesis.strategies import sampled_from
import pytz
from datetime import timedelta

ALL_TIMEZONES = list(map(pytz.timezone, pytz.all_timezones))

# There are a lot of fiddly edge cases in dates, so we run a larger number of
# examples just to be sure
with Settings(max_examples=1000):
    @given(
        datetimes(),  # datetimes generated are non-naive by default
        sampled_from(ALL_TIMEZONES), sampled_from(ALL_TIMEZONES),
    )
    def test_convert_via_intermediary(dt, tz1, tz2):
        """
        Test that converting between timezones is not affected by a detour via
        another timezone.
        """
        print(dt, tz1, tz2)
        assert dt.astimezone(tz1).astimezone(tz2) == dt.astimezone(tz2)

    @given(
        datetimes(timezones=[]),  # Now generate naive datetimes
        sampled_from(ALL_TIMEZONES), sampled_from(ALL_TIMEZONES),
    )
    def test_convert_to_and_fro(dt, tz1, tz2):
        """
        If we convert to a new timezone and back to the old one this should
        leave the result unchanged.
        """
        dt = tz1.localize(dt)
        assert dt == dt.astimezone(tz2).astimezone(tz1)

    @given(
        datetimes(),
        sampled_from(ALL_TIMEZONES),
    )
    def test_adding_an_hour_commutes(dt, tz):
        """
        When converting between timezones it shouldn't matter if we add an hour
        here or add an hour there.
        """
        an_hour = timedelta(hours=1)
        assert (dt + an_hour).astimezone(tz) == dt.astimezone(tz) + an_hour

    @given(
        datetimes(),
        sampled_from(ALL_TIMEZONES),
    )
    def test_adding_a_day_commutes(dt, tz):
        """
        When converting between timezones it shouldn't matter if we add a day
        here or add a day there.
        """
        a_day = timedelta(days=1)
        assert (dt + a_day).astimezone(tz) == dt.astimezone(tz) + a_day