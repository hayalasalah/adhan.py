"""
test_calculations.py - tests necessary calculations for computing adhan times.

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

from mock import patch

from adhan import calculations


def _is_close(first, second, abs_tolerance):
    diff = abs(first - second)
    return diff <= abs_tolerance


def test_julian_date_conversion():
    """Test that a Gregorian date can be converted to a Julian date."""
    conversion_date = date(2015, 12, 14)

    result = calculations.gregorian_to_julian(conversion_date)
    expected = 2457371

    assert result == expected, \
        "Gregorian date %s should be %d, got %d" % (
            conversion_date,
            expected,
            result,
        )


def test_julian_date_conversion_before_march():  # pylint: disable=invalid-name
    """Test that a date before March can be converted to a Julian date."""
    conversion_date = date(2016, 1, 18)

    result = calculations.gregorian_to_julian(conversion_date)
    expected = 2457406

    assert result == expected, \
        "Gregorian date %s should be %d, got %d" % (
            conversion_date,
            expected,
            result,
        )


def test_declination_of_sun():
    """Test that the correct declination of sun is computed from a date."""
    test_date = date(2014, 12, 14)

    result = calculations.sun_declination(test_date)

    # From http://www.wsanford.com/~wsanford/exo/sundials/DEC_Sun.html
    expected = -23.14

    assert _is_close(result, expected, 0.02), \
        "Sun declination on %s should be %.02f, got %.02f" % (
            test_date,
            expected,
            result,
        )


def test_equation_of_time():
    """Test that the correct equation of time is computed from a date."""
    test_date = date(2015, 5, 12)

    result = calculations.equation_of_time(test_date)
    expected = 0.0602

    assert _is_close(result, expected, 0.005), \
        "Equation of Time on %s should be %.02f, got %.02f" % (
            test_date,
            expected,
            result,
        )


@patch("adhan.calculations.equation_of_time")
def test_zuhr_utc_west(mock_equation_of_time):
    """Test that the correct Zuhr time is computed from a date in the west."""
    test_date = date(2015, 5, 12)
    mock_equation_of_time.return_value = 0.06377

    result = calculations.compute_zuhr_utc(test_date, longitude=-97.5)
    expected = 18.43  # ~6:30pm UTC == ~1:30pm CT
    assert _is_close(result, expected, 0.02), \
        "%.02f is not %.02f" % (result, expected)


@patch("adhan.calculations.equation_of_time")
def test_zuhr_utc_east(mock_equation_of_time):
    """Test that the correct Zuhr time is computed from a date in the east."""
    test_date = date(2015, 5, 12)
    mock_equation_of_time.return_value = 0.06377

    result = calculations.compute_zuhr_utc(test_date, longitude=97.5)
    expected = 18.43  # ~6:30pm UTC == ~1:30pm CT
    assert _is_close(result, expected, 0.02), \
        "%.02f is not %.02f" % (result, expected)
