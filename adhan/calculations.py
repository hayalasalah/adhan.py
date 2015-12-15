"""
calculations.py - necessary calculations for computing adhan times.

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

from __future__ import division

from math import pi, sin, cos, degrees
from datetime import date


def gregorian_to_julian(date):
    """Convert a datetime.date object to its corresponding Julian day.

    :param date: The datetime.date to convert to a Julian day
    :returns: A Julian day, as an integer
    """
    MONTHS_PER_YEAR = 12
    MARCH = 3
    JULIAN_START_YEAR = -4800

    before_march = 1 if date.month < MARCH else 0

    #
    # Number of months since March
    #
    month_index = date.month + MONTHS_PER_YEAR * before_march - MARCH

    #
    # Number of years (year starts on March) since 4800 BC
    #
    years_elapsed = date.year - JULIAN_START_YEAR - before_march

    total_days_in_previous_months = (153 * month_index + 2) // 5
    total_days_in_previous_years = 365 * years_elapsed
    total_leap_days = (
        (years_elapsed // 4) -
        (years_elapsed // 100) +
        (years_elapsed // 400)
    )

    return sum([
        date.day,
        total_days_in_previous_months,
        total_days_in_previous_years,
        total_leap_days,
        -32045,      # Offset to get January 1, 4713 equal to 0
    ])


def sun_declination(day):
    """Compute the declination angle of the sun for the given date.

    Uses the Spencer Formula
    (found at http://www.illustratingshadows.com/www-formulae-collection.pdf)

    :param day: The datetime.date to compute the declination angle for
    :returns: The angle, in degrees, of the angle of declination
    """
    day_of_year = day.toordinal() - date(day.year, 1, 1).toordinal()
    day_angle = 2 * pi * day_of_year / 365
    declination_radians = sum([
        0.006918,
        0.001480*sin(3*day_angle),
        0.070257*sin(day_angle),
        0.000907*sin(2*day_angle),
        -0.399912*cos(day_angle),
        -0.006758*cos(2*day_angle),
        -0.002697*cos(3*day_angle),
    ])

    return degrees(declination_radians)

