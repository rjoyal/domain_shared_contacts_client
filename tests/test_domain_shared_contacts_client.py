#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_domain_shared_contacts_client
----------------------------------

Tests for `domain_shared_contacts_client` module.
"""
import unittest
from click.testing import CliRunner
from domain_shared_contacts_client import cli
from domain_shared_contacts_client import contacts_helper
import gdata.contacts.data
import json


class TestContactEntry:
    def __init__(self):
        self.entry = gdata.contacts.data.ContactEntry()


class TestDomainSharedContactsClient(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 2
        assert 'credentials are required' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'domain_shared_contacts_client' in help_result.output
        result = runner.invoke(cli.main, ['--action=foo'])
        assert result.exit_code == 2
