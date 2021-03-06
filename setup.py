#!/usr/bin/env python3
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import os.path
import warnings

requirements = [
    'setuptools >= 2',
    'Flask >= 0.10.1',
    'Flask-OAuthlib >= 0.4.2',
    'SQLAlchemy',
    'requests',
]

extras_require = {
    'doc': [
        'Sphinx',
        'sphinxcontrib-httpdomain',
    ],
}

dependency_links = [
]

classifiers = '''
    Development Status :: 1 - Planning
    Framework :: Flask
    Intended Audience :: Developers
    License :: OSI Approved :: MIT License
    Operating System :: POSIX
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: Implementation :: CPython
    Topic :: Internet :: WWW/HTTP :: WSGI :: Application
'''


def readme():
    try:
        root = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(root, 'README.rst')) as f:
            return f.read()
    except IOError:
        warnings.warn("Couldn't found README.rst", RuntimeWarning)
        return ''


class PyTest(TestCommand):
    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='Githubarium',
    version='0.1.0dev1',
    author='Eunchong Yu',
    author_email='kroisse@gmail.com',
    url='https://github.com/flask-kr/githubarium',
    license='MIT',
    platforms=['POSIX'],
    description='The organization service for starred repositories in GitHub',
    long_description=readme(),
    packages=find_packages(where='.', exclude='tests'),
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    extras_require=extras_require,
    tests_require=[
        'pytest',
    ],
    cmdclass={
        'test': PyTest,
    },
    dependency_links=dependency_links,
    classifiers=[line.strip() for line in classifiers.splitlines() if line],
)
