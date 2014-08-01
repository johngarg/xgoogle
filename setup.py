from setuptools import setup, find_packages
import sys

__version__ = '1.4'

import os
def _read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='xgoogle',
    version=__version__,
    description="Python library to Google services (google search, google images, google videos, google translate)",
    long_description=_read('README.md'),
    classifiers=[],
    keywords='google search',
    author='Peteris Krumins',
    author_email='peter@catonmat.net',
    url='http://github.com/pkrumins/xgoogle',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    entry_points={
        # -*- Entry points: -*-
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
       # -*- Extra requirements: -*-
      'nltk==2.0.4'
    ],
)
