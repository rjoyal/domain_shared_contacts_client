from unittest import TestCase

from domain_shared_contacts_client.contacts_helper import (
    convert_organization, create_organization,
)


class OrganizationTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Federation of International Touch',
            'title': 'Event Director',
            'department': 'Events Commission',
            'job_description': 'Delivery of major FIT tournaments',
            'symbol': 'FIT',
        }
        self.organization = create_organization(self.data)

    def test_create_organization(self):
        expected = (
            '<ns0:organization '
                'xmlns:ns0="http://schemas.google.com/g/2005" '
                'label="http://schemas.google.com/g/2005#work">',
            '<ns0:orgDepartment>Events Commission</ns0:orgDepartment>',
            '<ns0:orgJobDescription>'
                'Delivery of major FIT tournaments</ns0:orgJobDescription>',
            '<ns0:orgName>Federation of International Touch</ns0:orgName>',
            '<ns0:orgSymbol>FIT</ns0:orgSymbol>',
            '<ns0:orgTitle>Event Director</ns0:orgTitle>',
            '</ns0:organization>',
        )
        xml = str(self.organization)
        for st in expected:
            self.assertIn(st, xml)

    def test_convert_organization(self):
        self.assertEqual(convert_organization(self.organization), self.data)
