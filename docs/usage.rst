=====
Usage
=====

An example of how to use Google Domain Shared Contacts Client in a project to retrieve a list of contacts::

    import domain_shared_contacts_client
    import json
    client = domain_shared_contacts_client.Client(
        domain='example.com', 
        admin='admin@example.com', 
        credentials='/path/to/credentials.json')
    contacts = client.get_contacts()
    print json.dumps(contacts)

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
