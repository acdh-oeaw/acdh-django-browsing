[![flake8 Lint](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-django-browsing/actions/workflows/test.yml)

# acdh-django-browsing

Django-App providing some useful things to create browsing views

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

### install dev-dependencies
```bash
pip install build pytest coverage flake8 black django django-next-prev
```

### install package
```bash
pip install .
```

### run migrations and start dev server
```
python manage.py migrate
python manage.py runserver
```

### build the package

```
python -m build
```