[![flake8 Lint](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/acdh-django-browsing.svg)](https://badge.fury.io/py/acdh-django-browsing)
# acdh-django-browsing
Django-App providing some useful things to create browsing views

## Features
see the example project in this repo to check out how to use the package and what it does

## Quickstart
Install acdh-django-browsing:

`pip install acdh-django-browsing`

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'browsing',
    ...
)
```


## Develop

### run migrations, load fixtures, and start dev server
```bash
uv run python manage.py migrate
uv run python manage.py loaddata data.json
uv run python manage.py runserver
```

### run tests
```bash
uv run coverage run manage.py test -v 2
```

### version bump

```
uv version --bump minor
```