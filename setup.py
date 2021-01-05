import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='acdh-django-browsing',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django-App providing some useful things to create browsing views',
    long_description=README,
    url='https://github.com/acdh-oeaw/acdh-django-browsing',
    author='Peter Andorfer',
    author_email='peter.andorfer@oeaw.ac.at',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'Django>=3.1',
        'django-autocomplete-light>=3.3.5,'
        'django-crispy-forms>=1.7.2',
        'django-filter>=2.1.0',
        'django-super-deduper>=0.1.2',
        'django-tables2>=2.0.6',
        'pandas>=1.1.0',
    ],
)
