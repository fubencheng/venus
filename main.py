import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os

from router import URL_MAPPING

from tornado.options import define, options

define("port", default=8090, help="run on the given port", type=int)

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application(handlers=URL_MAPPING, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print "application started http://0.0.0.0:{0}/".format(options.port)
    tornado.ioloop.IOLoop.instance().start()