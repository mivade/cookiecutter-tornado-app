from tornado.options import options

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

options.define("port", default=8008, help="HTTP port to listen on")
