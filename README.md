simple_websocket_example
========================

Simple websocket example with javascript client and python Tornado server files

Websockets provide convenient server to client messaging. To work with websockets you will need a websocket enabled client/server pair. Check page below for client websocket support:

http://caniuse.com/websockets

On server side I use [Tornado](http://www.tornadoweb.org/) web server supports websockets. It works nicely.

This repository contains two files:

1. client.js: contains javascript client code, which opens a websocket to the server and attempts to re-open it on websocket close event.

2. tornado_server.py: contains python server code, which opens a websocket along with standart http socket and waits for connections.

Please let me know if you spot any errors or would like to send thanks : )

Contact: eposta@cankavaklioglu.name.tr