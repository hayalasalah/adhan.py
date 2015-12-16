========
adhan.py
========
.. image:: https://travis-ci.org/hayalasalah/adhan.py.svg?branch=master
    :target: https://travis-ci.org/hayalasalah/adhan.py

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

    config = {
       'method' : 'isna',
       'asr'    : 'hanafi',
    }
    adhan_times = adhan(latitude=30.25, longitude=-97.75, date=date.today(), **config)

    print adhan_times['fajr']
    print adhan_times['shuruq']
    print adhan_times['zuhr']
    print adhan_times['asr']
    print adhan_times['maghrib']
    print adhan_times['isha']




Supported Options
=================

* 'method'
    * The method to use to calculate the adhan times
    * **Options**: 'mwl', 'isna', 'egypt', 'makkah', 'karachi', 'tehran', or 'jafari'
* 'asr'
    * Whether Asr should be calculated the Hanafi way or not (Standard)
    * **Options**: 'standard' or 'hanafi'

