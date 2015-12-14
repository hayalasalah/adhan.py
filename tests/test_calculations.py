"""
test_calculations.py - tests necessary calculations for computing adhan times

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
from datetime import date

from nose.tools import assert_almost_equals

from adhan import calculations


def test_julian_date_conversion():
    conversion_date = date(2015, 12, 14)

    result = calculations.gregorian_to_julian(conversion_date)
    expected = 2457371

    assert result == expected, \
        "Gregorian date %s should be %d, got %d" % (
            conversion_date,
            expected,
            result,
        )
