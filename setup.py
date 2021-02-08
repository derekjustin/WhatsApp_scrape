#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='scrape',
    version="0.1.0",
    description="WhatsApp Scaper.",
    author='Derek Holsapple Justin Strelka',
    author_email='derekhols31@gmail.com justin.strelka@outlook.com',
    packages=['scrape'],
    install_requires=[],
    tests_require=[],
    entry_points={
        'console_scripts': [
            'foo = scrape.foo:main', 'open_browser = scrape.open_browser:OpenBrowser'
        ],
    },
)
