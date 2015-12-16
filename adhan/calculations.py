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

from math import (
    pi,
    sin, cos, tan, atan2,
    degrees, radians
)


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


def equation_of_time(day):
    """Compute the equation of time for the given date.

    Uses formula described at
    https://en.wikipedia.org/wiki/Equation_of_time#Alternative_calculation

    :param day: The datetime.date to compute the equation of time for
    :returns: The angle, in radians, of the Equation of Time
    """
    EARTH_AXIS_TILT = radians(23.44)

    W = 360 / 365.24  # Earth's orbital velocity

    day_of_year = day.toordinal() - date(day.year, 1, 1).toordinal()

    #
    # Distance Earth moves from solstice to January 1 (so about 10 days)
    #
    A = W * (day_of_year + 10)

    #
    # Distance Earth moves from solstice to day_of_year
    # 2 is the number of days from Jan 1 to periheleon
    # This is the result of a lot of constants collapsing
    #
    B = A + 1.914 * sin(radians(W * (day_of_year - 2)))

    #
    # Compute "the difference between the angles moved at mean speed, and at
    # the corrected speed projected onto the equatorial plane, and [divide] by
    # 180 to get the difference in 'half turns'"
    #
    movement_on_equatorial_plane = degrees(
        atan2(
            tan(radians(B)),
            cos(EARTH_AXIS_TILT)
        )
    )
    eot_half_turns = (A - movement_on_equatorial_plane) / 180

    equation_of_time = 720 * (eot_half_turns - int(eot_half_turns + 0.5))

    return radians(equation_of_time)


def compute_zuhr_utc(day, longitude):
    """Compute the UTC floating point time for Zuhr given date and longitude.

    This function is necessary since all other prayer times are based on the
    time for Zuhr

    :param day: The day to compute Zuhr adhan for
    :param longitude: Longitude of the place of interest
    :returns: The UTC time for Zuhr, as a floating point number in [0, 24)
    """
    eot = equation_of_time(date)

    #
    # Formula as described by PrayTime.org doesn't work in Eastern hemisphere
    # because it expects to be subtracting a negative longitude. +abs() should
    # do the trick
    #

    zuhr_time_utc = 12 + (abs(longitude) / 15) - eot
    return abs(zuhr_time_utc) % 24
