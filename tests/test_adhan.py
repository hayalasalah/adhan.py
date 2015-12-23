"""
test_adhan.py - tests the program's interface.

Copyright (C) 2015  Zuhair Parvez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
from datetime import date, datetime

from adhan import adhan, methods


def test_functional_simple():
    """Test that a simple usage of the module works."""
    #
    # First, actually compute the adhan times
    #

    parameters = {}
    parameters.update(methods.isna)
    parameters.update(methods.asr_hanafi)

    adhan_times = adhan(
        date=date(2015, 12, 22),
        location=(30.25, -97.75),
        parameters=parameters,
        timezone_offset=-6
    )

    #
    # Check that the expected prayer times are actually in the result
    #
    expected = {
        'fajr': datetime(2015, 12, 22, 6, 13),
        'shuruq': datetime(2015, 12, 22, 7, 24),
        'asr': datetime(2015, 12, 22, 15, 17),
        'maghrib': datetime(2015, 12, 22, 17, 35),
        'isha': datetime(2015, 12, 22, 18, 47),
    }

    for name, expected_time in expected.items():
        assert name in adhan_times, \
            '%s not in adhan times' % name

        actual_time = adhan_times[name]

        assert isinstance(actual_time, datetime), \
            '%s\'s value is not a datetime' % name

        seconds_diff = abs(expected_time - actual_time).seconds
        assert seconds_diff <= 120, \
            'time for %s differ: expected %s, actual %s' % (
                name,
                expected_time,
                actual_time
            )
