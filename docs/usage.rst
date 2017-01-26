=====
Usage
=====

To use Google Domain Shared Contacts Client in a project::

    import domain_shared_contacts_client
    import json
    client = domain_shared_contacts_client.Client(domain='example.com', admin='admin@example.com')
    contacts = client.get_contacts()
    print json.dumps(contacts)


