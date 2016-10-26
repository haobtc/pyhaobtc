#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='haobtc-oauth2',
    version='0.0.1',
    description='haobtc oauth2',
    author='freeza91',
    author_email='useyes91@gmail.com',
    keywords=('Python', 'pyoauth2', 'haobtc'),
    license='MIT License',
    url='https://github.com/haobtc/pyhaobtc/tree/master/haobtc_oauth2',
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
    zip_safe=False,
)