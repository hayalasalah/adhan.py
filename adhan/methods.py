"""
methods - Contains definitions for common calculation methods.

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

# pylint: disable=pointless-string-statement


"""

Calculation Methods

"""
ISNA = {
    'fajr_angle': 15,
    'isha_angle': 15,
}

MUSLIM_WORLD_LEAGUE = {
    'fajr_angle': 18,
    'isha_angle': 17,
}

EGYPT = {
    'fajr_angle': 19.5,
    'isha_angle': 17.5,
}

MAKKAH = {
    'fajr_angle': 18.5,
    'isha_delay': 1.5,
}

KARACHI = {
    'fajr_angle': 18,
    'isha_angle': 18,
}

TEHRAN = {
    'fajr_angle': 17.7,
    'isha_angle': 14,
}

SHIA = {
    'fajr_angle': 16,
    'isha_angle': 14,
}


"""

Asr Calculation Method

"""
ASR_STANDARD = {
    'asr_multiplier': 1,
}

ASR_HANAFI = {
    'asr_multiplier': 2,
}
