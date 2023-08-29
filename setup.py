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
        "acdh-django-charts==0.5.3",
        "django-autocomplete-light>=3.8.1,<4",
        "django-crispy-forms>=2.0,<3",
        "crispy-bootstrap5>=0.7,<1",
        "django-filter>=23.1,<24",
        "django-super-deduper>=0.1.4",
        "django-tables2>=2.5,<3",
        "tablib>=3.5.0,<4",
    ],
)
