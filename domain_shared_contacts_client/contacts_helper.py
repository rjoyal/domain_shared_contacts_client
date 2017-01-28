# -*- coding: utf-8 -*-
import gdata.contacts.data
import gdata.data


def convert_address(entry):
    """ Handle list of structured postal addresses """
    address_list = []
    for address in entry.structured_postal_address:
        address_list.append({
            'primary': address.primary,
            'street': address.street.text,
            'city': address.city.text,
            'region': address.region.text,
            'postcode': address.postcode.text,
            'country': address.country.text
        })

    return address_list


def convert_email(entry):
    """ Handle list of email addresses """
    email_list = []
    for email in entry.email:
        email_list.append({
            'address': email.address,
            'primary': email.primary
        })

    return email_list


def convert_phone_number(entry):
    """ Handle list of phone numbers """
    phone_list = []
    for phone in entry.phone_number:
        phone_list.append({
            'text': phone.text,
            'primary': phone.primary
        })

    return phone_list


def convert_contacts(o):
    """ Convert the list of ContactEntry objects into a JSON serializable object """
    new_contacts = []
    for i, entry in enumerate(o.entry):
        new_entry = {
            'id': entry.id.text,
            'title': entry.title.text,
            'name': {
                'given_name': entry.name.given_name.text,
                'family_name': entry.name.family_name.text,
                'full_name': entry.name.full_name.text
            },
            'email': convert_email(entry),
            'phone_number': convert_phone_number(entry),
            'structured_postal_address': convert_address(entry)
        }
        new_contacts.append(new_entry)

    return new_contacts


def convert_contact(entry):
    """ Convert a single ContactEntry object into a JSON serializable object """
    new_entry = {
        'id': entry.id.text,
        'title': entry.title.text,
        'name': {
            'given_name': entry.name.given_name.text,
            'family_name': entry.name.family_name.text,
            'full_name': entry.name.full_name.text
        },
        'email': convert_email(entry),
        'phone_number': convert_phone_number(entry),
        'structured_postal_address': convert_address(entry)
    }
    return new_entry


def create_contact_entry(contact_object):
    new_contact = gdata.contacts.data.ContactEntry()
    new_contact.name = gdata.data.Name(
        given_name=gdata.data.GivenName(text=contact_object['name']['given_name']),
        family_name=gdata.data.FamilyName(text=contact_object['name']['family_name']),
        full_name=gdata.data.FullName(text=contact_object['name']['full_name'])
    )
    for email in contact_object['email']:
        new_contact.email.append(gdata.data.Email(
            address=email['address'],
            primary=email['primary'],
            # TODO support different address types
            rel=gdata.data.WORK_REL,
            display_name=contact_object['name']['full_name']
        ))
    for phone_number in contact_object['phone_number']:
        new_contact.phone_number.append(gdata.data.PhoneNumber(
            text=phone_number['text'],
            rel=gdata.data.WORK_REL,
            primary=phone_number['primary']
        ))
    for structured_postal_address in contact_object['structured_postal_address']:
        new_contact.structured_postal_address.append(gdata.data.StructuredPostalAddress(
            rel=gdata.data.WORK_REL,
            primary=structured_postal_address['primary'],
            street=gdata.data.Street(text=structured_postal_address['street']),
            city=gdata.data.City(text=structured_postal_address['city']),
            region=gdata.data.Region(text=structured_postal_address['region']),
            postcode=gdata.data.Postcode(text=structured_postal_address['postcode']),
            country=gdata.data.Country(text=structured_postal_address['country'])
        ))

    return new_contact
