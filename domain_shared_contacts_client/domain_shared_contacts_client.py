# -*- coding: utf-8 -*-
from oauth2client.service_account import ServiceAccountCredentials
import gdata.contacts.client
import httplib2
import json
import contacts_helper


class TokenFromOAuth2Creds:
    def __init__(self, creds):
        self.creds = creds

    def modify_request(self, req):
        if self.creds.access_token_expired or not self.creds.access_token:
            self.creds.refresh(httplib2.Http())
        self.creds.apply(req.headers)


class Client:
    def __init__(self, domain, admin, credentials):
        self.domain = domain
        self.admin = admin
        self.credentials = credentials
        if self.domain is None:
            raise ValueError('Client requires a domain')

        if self.admin is None:
            raise ValueError('Client requires an admin email address')

        if self.credentials is None:
            raise ValueError('Client requires a file path to JSON service account credentials')

        self.gd_client = self.create_gd_client()

    def create_gd_client(self):
        """ Build a Google Data API client """
        scopes = ['http://www.google.com/m8/feeds/contacts/']
        sa_credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials, scopes=scopes)
        delegated_credentials = sa_credentials.create_delegated(self.admin)
        gd_client = gdata.contacts.client.ContactsClient(self.domain)
        gd_client.auth_token = TokenFromOAuth2Creds(delegated_credentials)
        return gd_client

    def get_contacts(self):
        """ Fetch the list of shared contacts for the domain """
        contacts = self.gd_client.get_contacts(uri='https://www.google.com/m8/feeds/contacts/%s/full' % self.domain)
        return contacts

    def create_contact(self, json_data):
        """ Create a new contact from json data """
        if json_data is None:
            raise ValueError('No path provided to a JSON file in the json_data parameter')
        contact_object = json.load(open(json_data))
        new_contact = contacts_helper.create_contact_entry(contact_object)
        contact_entry = self.gd_client.CreateContact(
            insert_uri='https://www.google.com/m8/feeds/contacts/%s/full' % self.domain,
            new_contact=new_contact)
        saved_contact = {'id': contact_entry.id.text}
        return saved_contact

    def read_contact(self, id):
        """ Fetch a contact from the API """
        contact = self.gd_client.GetContact(uri=id)
        return contact

    def update_contact(self):
        """ Update a contact """
        pass

    def delete_contact(self):
        """ Delete a contact """
        pass
