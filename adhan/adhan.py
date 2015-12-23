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

SUNRISE_ANGLE = 0.833
SUNSET_ANGLE = 0.833


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
    pass
