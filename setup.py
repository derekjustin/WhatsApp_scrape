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
            'group_tools = scrape.group_tools_main:main', 'whats_scrape_GUI = scrape.whats_scrape_GUI_main:main'
        ],
    },
)
