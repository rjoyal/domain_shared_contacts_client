# -*- coding: utf-8 -*-
import gdata.contacts.data
import gdata.data


def fetch_attribute_text(attr):
    if attr is None:
        return ''
    else:
        return attr.text


def fetch_attribute_boolean(attr):
    if attr is None:
        return False
    else:
        return attr


def convert_address(entry):
    """
    Handle list of structured postal addresses
    :param entry:
    :return:
    """
    address_list = []
    for address in entry.structured_postal_address:
        address_list.append({
            'primary': fetch_attribute_boolean(address.primary),
            'street': fetch_attribute_text(address.street),
            'city': fetch_attribute_text(address.city),
            'region': fetch_attribute_text(address.region),
            'postcode': fetch_attribute_text(address.postcode),
            'country': fetch_attribute_text(address.country)
        })

    return address_list


def convert_email(entry):
    """
    Handle list of email addresses
    :param entry:
    :return:
    """
    email_list = []
    for email in entry.email:
        email_list.append({
            'address': email.address,
            'primary': fetch_attribute_boolean(email.primary)
        })

    return email_list


def convert_phone_number(entry):
    """
    Handle list of phone numbers
    :param entry:
    :return:
    """
    phone_list = []
    for phone in entry.phone_number:
        phone_list.append({
            'text': fetch_attribute_text(phone),
            'primary': fetch_attribute_boolean(phone.primary)
        })

    return phone_list


def convert_contacts(o):
    """
    Convert the list of ContactEntry objects into a JSON serializable object
    :param o:
    :return:
    """
    new_contacts = []
    for i, entry in enumerate(o.entry):
        new_entry = {
            'id': fetch_attribute_text(entry.id),
            'title': fetch_attribute_text(entry.title),
            'name': {
                'given_name': fetch_attribute_text(entry.name.given_name),
                'family_name': fetch_attribute_text(entry.name.family_name),
                'full_name': fetch_attribute_text(entry.name.full_name)
            },
            'email': convert_email(entry),
            'phone_number': convert_phone_number(entry),
            'structured_postal_address': convert_address(entry)
        }
        new_contacts.append(new_entry)

    return new_contacts


def convert_contact(entry):
    """
    Convert a single ContactEntry object into a JSON serializable object
    :param entry:
    :return:
    """
    new_entry = {
        'id': fetch_attribute_text(entry.id),
        'title': fetch_attribute_text(entry.title),
        'name': {
            'given_name': fetch_attribute_text(entry.name.given_name),
            'family_name': fetch_attribute_text(entry.name.family_name),
            'full_name': fetch_attribute_text(entry.name.full_name)
        },
        'email': convert_email(entry),
        'phone_number': convert_phone_number(entry),
        'structured_postal_address': convert_address(entry)
    }
    return new_entry


def create_contact_entry(contact_object):
    """
    Create a ContactEntry object given the dictionary in contact_object
    :param contact_object:
    :return:
    """
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
            rel=gdata.data.WORK_REL
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


def update_contact_entry(contact, contact_updates):
    """
    Update a contact entry with attributes passed in the contact_updates dictionary. Attributes like 'email' and
    'phone_number' that are lists are replaced with the contents of the list provided in the json data. If you want to
    add additional email addresses, for instance, pass the original email addresses along with any new ones together
    in the 'email' attribute of contact_updates.
    :param contact:
    :param contact_updates:
    :return:
    """

    if 'name' in contact_updates:
        if 'given_name' in contact_updates['name']:
            contact.name.given_name.text = contact_updates['name']['given_name']
        if 'family_name' in contact_updates['name']:
            contact.name.family_name.text = contact_updates['name']['family_name']
        if 'full_name' in contact_updates['name']:
            contact.name.full_name.text = contact_updates['name']['full_name']

    if 'email' in contact_updates:
        contact.email = []
        for email in contact_updates['email']:
            contact.email.append(gdata.data.Email(
                address=email['address'],
                primary=email['primary'],
                # TODO support different address types
                rel=gdata.data.WORK_REL
            ))

    if 'phone_number' in contact_updates:
        contact.phone_number = []
        for phone_number in contact_updates['phone_number']:
            contact.phone_number.append(gdata.data.PhoneNumber(
                text=phone_number['text'],
                rel=gdata.data.WORK_REL,
                primary=phone_number['primary']
            ))

    if 'structured_postal_address' in contact_updates:
        contact.structured_postal_address = []
        for structured_postal_address in contact_updates['structured_postal_address']:
            contact.structured_postal_address.append(gdata.data.StructuredPostalAddress(
                rel=gdata.data.WORK_REL,
                primary=structured_postal_address['primary'],
                street=gdata.data.Street(text=structured_postal_address['street']),
                city=gdata.data.City(text=structured_postal_address['city']),
                region=gdata.data.Region(text=structured_postal_address['region']),
                postcode=gdata.data.Postcode(text=structured_postal_address['postcode']),
                country=gdata.data.Country(text=structured_postal_address['country'])
            ))

    return contact
