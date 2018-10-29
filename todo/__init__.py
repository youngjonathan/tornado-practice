from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.ioloop import IOLoop
from views import HelloWorld

define('port', default=8888, help='port to listen on')

def main():
    app = Application([
        ('/', HelloWorld)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on port: {}'.format(options.port))
    IOLoop.current().start()

if __name__ == '__main__':
    main()



