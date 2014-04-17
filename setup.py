from setuptools import setup

setup(
    name = "django-passwords",
    version = __import__("passwords").__version__,
    author = "Donald Stufft",
    author_email = "donald@e.vilgeni.us",
    description = "A Django reusable app that provides validators and a form field that checks the strength of a password",
    long_description = open("README.rst").read(),
    url = "https://github.com/a302379333/django-passwords",
    license = "BSD",
    packages = [
        "passwords",
    ],
    package_data = {'passwords': ['static/passwords/passwords.coffee',
                                    'static/passwords/passwords.js',
                                    'static/passwords/passwords.css',
                                    'locale/en/LC_MESSAGES/django.mo',
                                    'locale/en/LC_MESSAGES/django.po',
                                    'locale/ru/LC_MESSAGES/django.mo',
                                    'locale/ru/LC_MESSAGES/django.po',]},
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Framework :: Django",
    ]
)
