"""
adhan.py - The main interface for using the API.

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
import math

from datetime import datetime, timedelta
from functools import partial

# from adhan import calculations, methods

from .calculations import (
    compute_time_at_sun_angle,
    compute_zuhr_utc,
    time_at_shadow_length,
)

from .methods import ASR_STANDARD

SUNRISE_ANGLE = 0.833
SUNSET_ANGLE = 0.833


def floating_point_to_datetime(day, fp_time):
    """Convert a floating point time to a datetime."""
    result = datetime(year=day.year, month=day.month, day=day.day)
    result += timedelta(minutes=math.ceil(60 * fp_time))
    return result


def adhan(day, location, parameters, timezone_offset=0):
    """Calculate adhan times given the parameters.

    This function will compute the adhan times for a certain location on
    certain day. The method for calculating the prayers as well as the time for
    Asr can also be specified. The timezone offset naively adds the specified
    number of hours to each time that is returned.

    :param day: The datetime.date to calculate for
    :param location: 2-tuple of floating point coordiantes for latitude and
                     longitude of location in degrees
    :param parameters: A dictionary-like object of parameters for computing
                       adhan times. Commonly used calculation methods are
                       available in the adhan.methods module
    :param timezone_offset: The number of hours to add to each prayer time
                            to account for timezones. Can be floating point

    """
    latitude, longitude = location

    #
    # To reduce a little repetitiveness, using a partial function that has the
    # day and latitude already set
    #
    time_at_sun_angle = partial(
        compute_time_at_sun_angle,
        day=day,
        latitude=latitude
    )

    zuhr_time = compute_zuhr_utc(day, longitude)

    shuruq_time = zuhr_time - time_at_sun_angle(angle=SUNRISE_ANGLE)
    maghrib_time = zuhr_time + time_at_sun_angle(angle=SUNSET_ANGLE)

    fajr_time = zuhr_time - time_at_sun_angle(angle=parameters['fajr_angle'])

    #
    # Most methods define Isha as a certain angle the sun has to be below
    # the horizon, but some methods define it as a certain number of minutes
    # after Maghrib
    #
    if parameters.get('isha_delay', None):
        isha_time = maghrib_time + parameters['isha_delay']
    else:
        isha_time = (
            zuhr_time +
            time_at_sun_angle(angle=parameters['isha_angle'])
        )

    #
    # Default to standard Asr method if not specified
    #
    asr_multiplier = parameters.get('asr_multiplier', ASR_STANDARD)
    asr_time = zuhr_time + time_at_shadow_length(
        day=day, latitude=latitude, multiplier=asr_multiplier
    )

    offset = timedelta(minutes=60 * timezone_offset)
    return {
        'fajr': floating_point_to_datetime(day, fajr_time) + offset,
        'zuhr': floating_point_to_datetime(day, zuhr_time) + offset,
        'shuruq': floating_point_to_datetime(day, shuruq_time) + offset,
        'asr': floating_point_to_datetime(day, asr_time) + offset,
        'maghrib': floating_point_to_datetime(day, maghrib_time) + offset,
        'isha': floating_point_to_datetime(day, isha_time) + offset,
    }

