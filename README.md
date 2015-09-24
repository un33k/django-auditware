Django Auditware
====================

**A Django application that tracks user's activity**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]
[![download-image]][download-link]


Overview
====================

Tracks user activity.

How to install
====================

    1. easy_install django-auditware
    2. pip install django-auditware
    3. git clone http://github.com/un33k/django-auditware
        a. cd django-auditware
        b. run python setup.py
    4. wget https://github.com/un33k/django-auditware/zipball/master
        a. unzip the downloaded file
        b. cd into django-auditware-* directory
        c. run python setup.py


How to use
====================

Add `auditware` to your INSTALLED_APP. Then monitor via Django admin.


Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([BSD](LICENSE.md)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-auditware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-auditware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-auditware.svg
[version-link]: https://pypi.python.org/pypi/django-auditware

[coverage-image]: https://coveralls.io/repos/un33k/django-auditware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-auditware

[download-image]: https://img.shields.io/pypi/dm/django-auditware.svg
[download-link]: https://pypi.python.org/pypi/django-auditware
