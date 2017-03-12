import logging
import os.path as osp

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import options

from .handlers import IndexHandler

logger = logging.getLogger(__name__)


def subdir(*paths):
    here = osp.abspath(osp.dirname(__file__))
    return osp.join(here, *paths)


def make_app(debug=False):
    app = Application(
        [
            (r"/", IndexHandler),
        ],
        static_path=subdir("static"),
        template_path=subdir("templates"),
        debug=debug)


if __name__ == "__main__":
    options.parse_command_line()
    app = make_app(debug=True)
    app.listen(options.port)
    logger.info("Listening on port %d", options.port)
    IOLoop.current().start()
