# -*- coding: utf-8 -*-

import json
import os.path

import click
import contacts_helper
import domain_shared_contacts_client


@click.group()
@click.argument('domain')
@click.argument('admin')
@click.argument('credentials', type=click.Path(exists=True))
@click.pass_context
def cli(ctx, domain, admin, credentials):
    """
    Command line utility to interact with the Shared Contacts API.
    """
    ctx.obj['domain'] = domain
    ctx.obj['admin'] = admin
    ctx.obj['credentials'] = credentials


@cli.command()
@click.option('--indent', '-i', type=int, default=None)
@click.option('--sort/--no-sort', default=True)
@click.option('--output', '-o', type=click.File('w'), default='-')
@click.pass_context
def list(ctx, indent, sort, output):
    """
    all contacts
    """
    client = domain_shared_contacts_client.Client(**ctx.obj)
    contacts = client.get_contacts()
    json.dump(contacts, output,
              default=contacts_helper.convert_contacts,
              sort_keys=sort, indent=indent)


@cli.command()
@click.argument('contact', type=click.Path(exists=True))
@click.option('--indent', '-i', type=int, default=None)
@click.option('--sort/--no-sort', default=True)
@click.option('--output', '-o', type=click.File('w'), default='-')
@click.pass_context
def create(ctx, contact, indent, sort, output):
    """
    a single contact
    """
    client = domain_shared_contacts_client.Client(**ctx.obj)
    contact = client.create_contact(contact)
    json.dump(contact, output,
              default=contacts_helper.convert_contacts,
              sort_keys=sort, indent=indent)


@cli.command()
@click.argument('id')
@click.option('--indent', '-i', type=int, default=None)
@click.option('--sort/--no-sort', default=True)
@click.option('--output', '-o', type=click.File('w'), default='-')
@click.pass_context
def read(ctx, id, indent, sort, output):
    """
    a single contact
    """
    client = domain_shared_contacts_client.Client(**ctx.obj)
    key = 'http://www.google.com/m8/feeds/contacts/%s/base/%s'
    contact = client.read_contact(key % (ctx.obj['domain'], id))
    json.dump(contact, output,
              default=contacts_helper.convert_contact,
              sort_keys=sort, indent=indent)


@cli.command()
@click.argument('contact', type=click.Path(exists=True))
@click.option('--indent', '-i', type=int, default=None)
@click.option('--sort/--no-sort', default=True)
@click.option('--output', '-o', type=click.File('w'), default='-')
@click.pass_context
def update(ctx, contact, indent, sort, output):
    """
    a single contact
    """
    client = domain_shared_contacts_client.Client(**ctx.obj)
    with open(contact) as fp:
        data = json.load(fp)
    contact = client.update_contact(data['id'], contact)
    json.dump(contact, output,
              default=contacts_helper.convert_contact,
              sort_keys=sort, indent=indent)


@cli.command()
@click.argument('id')
@click.option('--indent', '-i', type=int, default=None)
@click.option('--sort/--no-sort', default=True)
@click.option('--output', '-o', type=click.File('w'), default='-')
@click.pass_context
def delete(ctx, id, indent, sort, output):
    """
    a single contact
    """
    client = domain_shared_contacts_client.Client(**ctx.obj)
    key = 'http://www.google.com/m8/feeds/contacts/%s/base/%s'
    result = client.delete_contact(key % (ctx.obj['domain'], id))
    json.dump(result, output, sort_keys=sort, indent=indent)


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
