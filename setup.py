#!/usr/bin/env python
import sys

import pylibdmtx


SCRIPTS = ['read_datamatrix', 'create_datamatrix']

# Optional dependency
PILLOW = 'Pillow>=3.2.0'

URL = 'https://github.com/NaturalHistoryMuseum/pylibdmtx/'


def readme():
    try:
        # README.rst is generated from README.md (see DEVELOPING.md)
        with open('README.rst') as f:
            return f.read()
    except:
        return 'Visit {0} for more details.'.format(URL)


setup_data = {
    'name': 'pylibdmtx',
    'version': pylibdmtx.__version__,
    'author': 'Lawrence Hudson',
    'author_email': 'l.hudson@nhm.ac.uk',
    'url': URL,
    'license': 'MIT',
    'description': pylibdmtx.__doc__,
    'long_description': readme(),
    'packages': ['pylibdmtx', 'pylibdmtx.scripts', 'pylibdmtx.tests'],
    'test_suite': 'pylibdmtx.tests',
    'scripts': ['pylibdmtx/scripts/{0}.py'.format(script) for script in SCRIPTS],
    'entry_points': {
        'console_scripts':
            ['{0}=pylibdmtx.scripts.{0}:main'.format(script) for script in SCRIPTS],
    },
    'extras_require': {
        ':python_version=="2.7"': ['enum34>=1.1.6', 'pathlib>=1.0.1'],
        'scripts': [
            PILLOW,
        ],
    },
    'tests_require': [
        # TODO How to specify OpenCV? 'cv2>=2.4.8',
        PILLOW,
        'numpy>=1.8.2',
    ],
    'include_package_data': True,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
}


def setuptools_setup():
    from setuptools import setup
    setup(**setup_data)


if (2, 7) == sys.version_info[:2] or (3, 4) <= sys.version_info:
    setuptools_setup()
else:
    sys.exit('Python versions 2.7 and >= 3.4 are supported')
