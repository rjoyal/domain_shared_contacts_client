# -*- coding: utf-8 -*-

import json
import os.path

import click

import contacts_helper
import domain_shared_contacts_client

actions = ['list', 'create', 'read', 'update', 'delete']


def validate_file(ctx, param, value):
    """
    Check if the value parameter points to an existing file
    Use validate_required_file to validate that the parameter is present
    """
    if value is None:
        return None
    if not os.path.isfile(value):
        # TODO how to get parameter name in error message
        raise click.BadParameter('%s should point to a existing file: %s not found' % (param.human_readable_name, value))
    return value


def validate_required_file(ctx, param, value):
    if value is None:
        raise click.BadParameter('%s are required' % param.human_readable_name)
    return validate_file(ctx, param, value)


def validate_action(ctx, param, value):
    """ Check if the action is supported """
    if value not in actions:
        raise click.BadParameter('invalid action %s' % value)
    return value


@click.command()
@click.option('--domain', help='Your Google Apps domain (e.g. example.com')
@click.option('--admin', help='Your domain admin account email (e.g. admin@example.com)')
@click.option('--credentials', help='JSON credentials for your service account',
              callback=validate_required_file)
@click.option('--action', help='One of the following actions: list, create, read, update, delete',
              callback=validate_action)
@click.option('--contact_details', help='A JSON file containing a new contact record',
              callback=validate_file)
@click.option('--id', help='The ID of a contact to read, update or delete')
def main(domain, admin, credentials, action, contact_details, id):
    """Console script for domain_shared_contacts_client"""
    client = domain_shared_contacts_client.Client(domain=domain, admin=admin,
                                                  credentials=credentials)
    if action == 'list':
        contacts = client.get_contacts()
        print(json.dumps(contacts, default=contacts_helper.convert_contacts,
                         sort_keys=True, indent=4))
    elif action == 'create':
        if contact_details is None:
            raise click.UsageError('Please provide contact_details')
        saved_contact = client.create_contact(contact_details)
        print(json.dumps(saved_contact))
    elif action == 'read':
        contact = client.read_contact(id)
        print(json.dumps(contact, default=contacts_helper.convert_contact,
                         sort_keys=True, indent=4))
    elif action == 'update':
        if contact_details is None:
            raise click.UsageError('Please provide contact_details')
        contact = client.update_contact(id, contact_details)
        print(json.dumps(contact, default=contacts_helper.convert_contact,
                         sort_keys=True, indent=4))
    elif action == 'delete':
        result = client.delete_contact(id)
        print(json.dumps(result))


if __name__ == "__main__":
    main()
