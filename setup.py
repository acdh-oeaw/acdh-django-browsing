from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="acdh-django-browsing",
    version="2.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="Django-App providing some useful things to create browsing views",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/acdh-oeaw/acdh-django-browsing",
    author="Peter Andorfer",
    author_email="peter.andorfer@oeaw.ac.at",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[
        "django-autocomplete-light",
        "django-crispy-forms",
        "crispy-bootstrap5",
        "django-filter",
        "django-super-deduper",
        "django-tables",
        "tablib",
    ],
)
