#!/usr/bin/env python
# Needs Google API Client Library for Python (added to requirements_dev.txt)
# Needs gdata-python-client. Need to install manually
# git clone git@github.com:google/gdata-python-client.git
# cd gdata-python-client
# python setup.py install

import json

import atom.data
import gdata.contacts.client
import gdata.contacts.data
import gdata.data
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


class TokenFromOAuth2Creds:
    def __init__(self, creds):
        self.creds = creds

    def modify_request(self, req):
        if self.creds.access_token_expired or not self.creds.access_token:
            self.creds.refresh(httplib2.Http())
        self.creds.apply(req.headers)


class ContactFromJson:
    def __init__(self, jsonData):
        self.jsonData = json.loads(jsonData)

    def create_contact(self, gd_client):
        new_contact = gdata.contacts.data.ContactEntry()
        new_contact.name = gdata.data.Name(
            given_name=gdata.data.GivenName(text=self.jsonData['givenName']),
            family_name=gdata.data.FamilyName(text=self.jsonData['familyName']),
            full_name=gdata.data.FullName(text=self.jsonData['fullName'])
        )
        new_contact.content = atom.data.Content(text=self.jsonData['notes'])
        # TODO Handle multiple email addresses
        new_contact.email.append(gdata.data.Email(
            address=self.jsonData['email'],
            primary='true',
            rel=gdata.data.WORK_REL,
            display_name=self.jsonData['fullName']
        ))
        # TODO Handle multiple phone numbers
        new_contact.phone_number.append(gdata.data.PhoneNumber(
            text=self.jsonData['phone'],
            rel=gdata.data.WORK_REL,
            primary='true'
        ))
        # TODO Handle multiple mailing addresses
        new_contact.structured_postal_address.append(gdata.data.StructuredPostalAddress(
            rel=gdata.data.WORK_REL, primary='true',
            street=gdata.data.Street(text=self.jsonData['street']),
            city=gdata.data.City(text=self.jsonData['city']),
            region=gdata.data.Region(text=self.jsonData['region']),
            postcode=gdata.data.Postcode(text=self.jsonData['postcode']),
            country=gdata.data.Country(text=self.jsonData['country'])
        ))
        # TODO pass in the domain as a parameter
        contact_entry = gd_client.CreateContact(
            insert_uri='https://www.google.com/m8/feeds/contacts/tangerinepastry.com/full',
            new_contact=new_contact)
        print "Contact's ID: %s" % contact_entry.id.text
        return contact_entry


scopes = ['http://www.google.com/m8/feeds/contacts/']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scopes=scopes)

delegated_credentials = credentials.create_delegated('rjoyal@tangerinepastry.com')

# http_auth = credentials.authorize(Http())

gd_client = gdata.contacts.client.ContactsClient('tangerinepastry.com')
gd_client.auth_token = TokenFromOAuth2Creds(delegated_credentials)
contacts = gd_client.get_contacts(uri='https://www.google.com/m8/feeds/contacts/tangerinepastry.com/full')
for i, entry in enumerate(contacts.entry):
    print '\n%s %s' % (i + 1, entry.name.full_name.text)

contactService = ContactFromJson('''{
    "givenName": "Robert",
    "familyName": "Joyal",
    "fullName": "Robert Joyal",
    "notes": "",
    "email": "rjoyal1@comcast.net",
    "phone": "(978)238-6144",
    "street": "5 Horseshoe Lane",
    "city": "South Hamilton",
    "region": "MA",
    "postcode": "01982",
    "country": "United States"
}''')
contactService.create_contact(gd_client=gd_client)
