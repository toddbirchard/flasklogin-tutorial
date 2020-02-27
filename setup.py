"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flask_login_tutorial',
    version='0.1.0',
    description='Example Flask project for implementing Flask-Login.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/flasklogin-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Tutorials',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Flask Flask-Login Users Login Authentication Tutorial',
    packages=find_packages(),
    install_requires=['flask',
                      'flask_login',
                      'flask_sqlalchemy',
                      'flask_assets',
                      'PyMySQL',
                      'WTForms'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run = wsgi:app',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/flasklogin-tutorial/issues',
        'Source': 'https://github.com/toddbirchard/flasklogin-tutorial/',
    },
)
