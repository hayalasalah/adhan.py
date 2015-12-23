========
adhan.py
========
.. image:: https://travis-ci.org/hayalasalah/adhan.py.svg?branch=master
    :target: https://travis-ci.org/hayalasalah/adhan.py
.. image:: https://img.shields.io/github/license/hayalasalah/adhan.py.svg
    :target: https://github.com/hayalasalah/adhan.py/blob/master/LICENSE

adhan.py is a Python library for computing adhan times.

It is a refactoring of the PrayTimes.org Python adhan calculator that will ensure:

* PEP8 compliant code
* A PyPI package
* A simplified API that favors convention over configuration
* A test suite
* Presence on GitHub to encourage contribution


================================
THE FOLLOWING DOES NOT WORK YET
================================

Installation
============

.. code:: bash

    pip install adhan


Usage
=====

.. code:: python

    from datetime import date

    from adhan import adhan
    from adhan.methods import ISNA, ASR_STANDARD

    params = {}
    params.upate(ISNA)
    params.update(ASR_STANDARD)

    adhan_times = adhan(
        date = date.today(),
        location=(30.25,-97.75),
        parameters=params,
        timezone_offset=-6,
    )

    """
    adhan_times will be a dict containing datetime objects for the keys 'fajr',
    'shuruq', 'zuhr', 'asr', 'maghrib', and 'isha'

    """



Available Methods
=================

The following methods are available in the adhan.methods module and should cover
the vast majority of cases

* ISNA: Islamic Society of North America
* MUSLIM_WORLD_LEAGUE: Muslim World League
* EGYPT: Egyptian General Authority of Survey
* MAKKAH: Umm al-Qura University, Makkah
* KARACHI: University of Islamic Sciences, Karachi
* TEHRAN: Institude of Geophysics, University of Tehran
* SHIA: Shia Ithna Ashari, Leva Research Institute, Qum

* ASR_STANDARD: Shafi'i, Maliki, Ja'fari, and Hanbali
* ASR_HANAFI: Hanafi

Custom Parameter Dictionary
===========================

In case you want to define your own parameters, the parameters argument accepts
dicts with the following keys

* fajr_angle: The angle below sunrise to compute Fajr for
* isha_angle: The angle below sunset to compute Isha for
* asr_multiplier: The multiplier to use for Asr, such that the length of
  an object's shadow is the multiplier * the object's length + the length of the
  object's shadow at midday
* isha_delay: The floating point number of hours after Maghrib that Isha is

