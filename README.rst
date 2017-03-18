cookiecutter-tornado-app
========================

Cookiecutter template for a Tornado_ web app.

Usage::

    cookiecutter https://github.com/mivade/cookiecutter-tornado-app.git

.. _Tornado: http://www.tornadoweb.org/en/stable/


Features
--------

This project template is fairly minimal. It includes:

* Basic HTML5 base template
* Static CSS and JS directory layout (unpopulated)
* An empty ``BaseHandler`` class for optionally adding things like
  authentication
* A working ``IndexHandler`` to render the ``index.html`` template
* Boilerplate ``setup.py`` and common options for pytest_ in ``setup.cfg``

.. _pytest: http://docs.pytest.org/en/latest/
