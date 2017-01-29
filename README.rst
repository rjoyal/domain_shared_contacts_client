===============================
Google Domain Shared Contacts Client
===============================


.. image:: https://img.shields.io/pypi/v/domain_shared_contacts_client.svg
        :target: https://pypi.python.org/pypi/domain_shared_contacts_client

.. image:: https://img.shields.io/travis/rjoyal/domain_shared_contacts_client.svg
        :target: https://travis-ci.org/rjoyal/domain_shared_contacts_client

.. image:: https://readthedocs.org/projects/domain-shared-contacts-client/badge/?version=latest
        :target: https://domain-shared-contacts-client.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/rjoyal/domain_shared_contacts_client/shield.svg
     :target: https://pyup.io/repos/github/rjoyal/domain_shared_contacts_client/
     :alt: Updates


A Python client to CRUD Google Domain Shared Contacts


- Free software: MIT license
- Documentation: https://domain-shared-contacts-client.readthedocs.io.


Features
--------

- Command-line client and Python library::

    $ pip install domain_shared_contacts_client
    $ domain_shared_contacts_client --help
    Usage: domain_shared_contacts_client [OPTIONS]

      Console script for domain_shared_contacts_client

    Options:
      --domain TEXT           Your Google Apps domain (e.g. example.com
      --admin TEXT            Your domain admin account email (e.g.
                              admin@example.com)
      --credentials TEXT      JSON credentials for your service account
      --action TEXT           One of the following actions: list, create, read,
                              update, delete
      --contact_details TEXT  A JSON file containing a new contact record
      --id TEXT               The ID of a contact to read, update or delete
      --help                  Show this message and exit.

- List, create, read, update and delete basic information for Google Domain Shared Contacts
    - name
        - given_name
        - family_name
        - full_name
    - email (list)
        - address
        - primary
    - phone_number (list)
        - text
        - primary
    - structured_postal_address (list)
        - street
        - city
        - region
        - postcode
        - country
        - primary

Limitations
-----------

* Python 2.7 only
* Updates a limited set of the ContactEntry attributes
* Email address, phone number and postal address types are hard-coded to gdata.data.WORK_REL

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

