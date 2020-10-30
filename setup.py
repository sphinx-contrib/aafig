# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
|Sponsor|\ |GHS|\ |LP|\ |PP|\ |BMC|\ |P|\ |F|

This package contains the aafigure_ Sphinx_ extension.

.. _aafigure: https://launchpad.net/aafigure
.. _Sphinx: http://sphinx.pocoo.org/

aafigure_ is a program and a reStructuredText_ directive to allow embeded ASCII
art figures to be rendered as nice images in various image formats. The
aafigure_ directive needs a *hardcoded* image format, so it doesn't goes well
with Sphinx_ multi-format support.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

This extension adds the ``aafig`` directive that automatically selects the
image format to use acording to the Sphinx_ writer used to generate the
documentation.

Usage example::

    .. aafig::
        :aspect: 60
        :scale: 150
        :proportional:
        :textual:

        +-------+         +-----------+
        | Hello +-------->+ aafigure! |
        +-------+         +-----------+

.. Sponsoring badge:
.. |Sponsor| image:: https://img.shields.io/badge/-Sponsor-555555?style=flat-square
   :target: https://github.com/llucax/llucax/blob/main/sponsoring-platforms.md
.. |GHS| image:: https://img.shields.io/badge/--ea4aaa?logo=github&style=flat-square
   :target: https://github.com/sponsors/llucax
.. |LP| image:: https://img.shields.io/badge/--f6c915?logo=liberapay&logoColor=black&style=flat-square
   :target: https://liberapay.com/llucax/donate
.. |PP| image:: https://img.shields.io/badge/--0070ba?logo=paypal&style=flat-square
   :target: https://www.paypal.com/donate?hosted_button_id=UZRR3REUC4SY2
.. |BMC| image:: https://img.shields.io/badge/--ff813f?logo=buy-me-a-coffee&logoColor=white&style=flat-square
   :target: https://www.buymeacoffee.com/llucax
.. |P| image:: https://img.shields.io/badge/--f96854?logo=patreon&logoColor=white&style=flat-square
   :target: https://www.patreon.com/llucax
.. |F| image:: https://img.shields.io/badge/--6bc76b?logo=flattr&logoColor=white&style=flat-square
   :target: https://flattr.com/@llucax
'''

requires = ['Sphinx>=0.6', 'aafigure>=0.3']

setup(
    name='sphinxcontrib-aafig',
    version='1.0.3',
    url='http://packages.python.org/sphinxcontrib-aafig/',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-aafig',
    license='BOLA',
    author='Leandro Lucarella',
    author_email='luca@llucax.com',
    description='aafig Sphinx extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
