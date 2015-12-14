========
adhan.py
========

adhan.py is a Python library for computing adhan times.

It is a refactoring of the PrayTimes.org Python adhan calculator, simplifying where necessary


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

=====       ===============
Key         Supported Values
---         ----------------
'method'    'mwl', 'isna', 'egypt', 'makkah', 'karachi', 'tehran', or 'jafari'
'asr'       'standard' or 'hanafi'

