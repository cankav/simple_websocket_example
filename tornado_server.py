#!/usr/bin/env python

from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.websocket
import json

define('port', type=int, default=8080)

class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello from tornado')

class MyWebSocket(tornado.websocket.WebSocketHandler):
  clients = []

  def open(self):
    # clients must be accessed through class object!!!
    MyWebSocket.clients.append(self)
    print "\nWebSocket opened"

  def on_message(self, message):
    print "msg recevied", message
    msg = json.loads(message) # todo: safety?

    # send other clients this message
    for c in MyWebSocket.clients:
      if c != self:
        c.write_message(msg)

  def on_close(self):
    print "WebSocket closed"
    # clients must be accessed through class object!!!
    MyWebSocket.clients.remove(self)

def main():
  tornado_app = tornado.web.Application([
      ('/hello-tornado', HelloHandler),
      ('/websocket', MyWebSocket),
      ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
