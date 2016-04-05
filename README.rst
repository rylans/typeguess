typeguess
=========

|Build Status|

Automatically guess data types

Examples
~~~~~~~~

.. code:: python

    >>> from typeguess import guess
    >>> guess(['hanson@mail.org'])
    'string.email'

.. code:: python

    >>> from typeguess import guess
    >>> guess(['m', 'f'])
    'string.vcard.gender'

Planned Features
~~~~~~~~~~~~~~~~

-  vCard types
-  XML Schema types

License
-------

Apache 2.0

.. |Build Status| image:: https://travis-ci.org/rylans/typeguess.svg?branch=master
   :target: https://travis-ci.org/rylans/typeguess
