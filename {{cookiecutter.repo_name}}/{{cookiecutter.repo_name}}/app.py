from tornado.web import Application


def make_app(urls, debug=False):
    app = Application(urls, debug=debug)
