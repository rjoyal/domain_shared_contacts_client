#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_domain_shared_contacts_client
----------------------------------

Tests for `domain_shared_contacts_client` module.
"""
import unittest

import gdata.contacts.data
from click.testing import CliRunner
from domain_shared_contacts_client import cli


class TestContactEntry:
    def __init__(self):
        self.entry = gdata.contacts.data.ContactEntry()


class TestDomainSharedContactsClient(unittest.TestCase):

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli)
        # I'm assuming that a successful result is what we are looking for below
        self.assertEqual(result.exit_code, 0)
