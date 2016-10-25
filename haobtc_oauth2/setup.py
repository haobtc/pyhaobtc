#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='haobtc_oauth2',
    keywords=('Python', 'pyoauth2', 'haobtc'),
    license='MIT License',
    url='https://github.com/liluo/py-oauth2',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
)
