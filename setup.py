#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='scrape',
    version="0.1.0",
    description="WhatsApp Scaper.",
    author='Derek Holsapple',
    author_email='derekhols31@gmail.com',
    packages=['scrape'],
    install_requires=[],
    tests_require=[],
    entry_points={
        'console_scripts': [
            'foo = scrape.foo:main', 'scrape = scrape.whatsapp_scrape:main',
        ],
    },
)
