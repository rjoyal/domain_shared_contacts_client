#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0', 'gdata', 'oauth2client',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='domain_shared_contacts_client',
    version='1.0.3',
    description="A Python client to CRUD Google Domain Shared Contacts",
    long_description=readme + '\n\n' + history,
    author="Robert Joyal",
    author_email='rjoyal@gmail.com',
    url='https://github.com/rjoyal/domain_shared_contacts_client',
    packages=[
        'domain_shared_contacts_client',
    ],
    package_dir={'domain_shared_contacts_client':
                 'domain_shared_contacts_client'},
    entry_points={
        'console_scripts': [
            'domain_shared_contacts_client=domain_shared_contacts_client.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='domain_shared_contacts_client',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
