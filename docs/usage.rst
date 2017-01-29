=====
Usage
=====


Use Google Domain Shared Contacts Client in a project to list, create, read, update and delete contacts::

    import domain_shared_contacts_client
    import json
    
    # Create the client. Authenticates to the Google Data API using the service account credentials provided
    client = domain_shared_contacts_client.Client(
        domain='example.com', 
        admin='admin@example.com', 
        credentials='/path/to/credentials.json')
    
    # Fetch the list of contacts currently available
    contacts = client.get_contacts()
    print json.dumps(contacts, default=contacts_helper.convert_contacts)

Fetch contacts using the CLI::

    $ domain_shared_contacts_client \
        --domain example.com \
        --admin admin@example.com \
        --credentials /path/to/client_secret.json \
        --action list

Example new_contact.json::

    {
        "name": {
            "given_name": "John",
            "family_name": "Doe",
            "full_name": "John Doe"
        },
        "email": [
            {
                "address": "jdoe@somewhere.com",
                "primary": "true"
            }
        ],
        "phone_number": [
            {
                "text": "(888)555-1212",
                "primary": "true"
            }
        ],
        "structured_postal_address": [
            {
                "street": "1 Example St.",
                "city": "Springfield",
                "region": "IL",
                "postcode": "62701",
                "country": "United States",
                "primary": "true"
            }
        ]
    }


Create a new contact::

    saved_contact = client.create_contact('/path/to/new_contact.json')
    print json.dumps(saved_contact)

Create a new contact using the CLI::

    $ domain_shared_contacts_client \
        --domain example.com \
        --admin admin@example.com \
        --credentials /path/to/client_secret.json \
        --action create \
        --contact-details /path/to/new_contact.json
    {"id": "http://www.google.com/m8/feeds/contacts/example.com/base/2ba2136d0e101978"}

Read a contact::

    contact = client.read_contact(saved_contact['id'])
    print json.dumps(contact, default=contacts_helper.convert_contact)

Read a contact using the CLI::

    $ domain_shared_contacts_client \
        --domain example.com \
        --admin admin@example.com \
        --credentials /path/to/client_secret.json \
        --action read \
        --id http://www.google.com/m8/feeds/contacts/example.com/base/2ba2136d0e101978

Example update_contact.json::

    {
        "name": {
            "given_name": "Joe",
            "full_name": "Joe Doe"
        },
        "email": [
            {
                "address": "jdoe@somewhereelse.com",
                "primary": "true"
            },
            {
                "address": "jdoe@somewhere.com",
                "primary": "false"
            }
        ]
    }


Update a contact::

    contact = client.update_contact(saved_contact['id'], '/path/to/updated_contact.json')
    print json.dumps(contact, default=contacts_helper.convert_contact)

Update a contact using the CLI::

    $ domain_shared_contacts_client \
        --domain example.com \
        --admin admin@example.com \
        --credentials /path/to/client_secret.json \
        --action read \
        --id http://www.google.com/m8/feeds/contacts/example.com/base/2ba2136d0e101978 \
        --contact-details /path/to/updated_contact.json

Delete a contact::

    result = client.delete_contact(saved_contact['id'])
    print json.dumps(result)

Delete a contact using the CLI::

    $ domain_shared_contacts_client 
        --domain example.com \
        --admin admin@example.com \
        --credentials /path/to/client_secret.json \
        --action delete \
        --id http://www.google.com/m8/feeds/contacts/example.com/base/2ba2136d0e101978
    {"status": "OK"}

This package assumes the following:

- You have a Google Apps domain account

- You are able to login as the Domain Admin for the domain account

- You have created a `Service Account`_ and enabled G-Suite Domain-wide Delegation for that account

- You have created a key for the service account and downloaded it in JSON format

  - This will be provided in the 'credentials' parameter to instantiate a Client

- You have granted your service account authority to make API calls on your behalf

  - Go to the domain Admin Console

  - Select Security from the list of controls. If you don't see Security listed, select More controls from the gray bar at 
    the bottom of the page, then select Security from the list of controls. If you can't see the controls, make sure you're 
    signed in as an administrator for the domain.
    
  - Select Show more and then Advanced settings from the list of options.

  - Select Manage API client access in the Authentication section.

  - In the Client Name field enter the service account's Client ID. You can find your service account's client ID in the 
    Service accounts page.

  - In the One or More API Scopes field enter the list of scopes that your application should be granted access to. 
    In our case, that is http://www.google.com/m8/feeds/contacts/

  - Click Authorize

  - Your application now has the authority to make API calls as users in your domain (to "impersonate" users).


.. _Service Account: https://console.developers.google.com/permissions/serviceaccounts
