simple_websocket_example
========================

Simple websocket example with javascript client and python Tornado server files

Websockets provide convenient server to client messaging. To work with websockets you will need a websocket enabled client/server pair. Check page below for client websocket support:

http://caniuse.com/websockets

There are two files in this example. Sections below explain both of them.


client.js
-------------
Contains javascript client code, which opens a websocket to the server and attempts to re-open it on websocket close event.

client.js should run on client side, which may be embeded to your html file. On page load the code tries to establish websocket connection with address: "ws://localhost:8080/websocket". If for some reason connection is closed, javascript code will try to re-open the connection.

+ Insert your custom processing into the ws.onmessage function. 
+ Use the ws_send function to send a message to the server. 

tornado_server.py
--------------------
Python code in tornado_server.py uses [Tornado](http://www.tornadoweb.org/) web server to open a websocket connection as well as an http connection. Once Tornado is installed (<pre>pip install tornado</pre>) you can use the command below to initialize the web server:

python tornado_server.py

To test if http server is running you can visit http://localhost:8080/hello-tornado page. Please note that websockets are not accessible through http. So do not try to access /websocket via your browser.

If it all goes according to the plan you should see the following on your browser's console:

<pre>
ws open
ws_send sent
</pre>

Python code will also provide some output:

<pre>
WebSocket opened
msg recevied ...
</pre>

Server code stores connected clients in its MyWebSocket.clients data structure. Once a message is received from a client all other recorded clients are forwarded the sent message. If a client disconnects for some reason the MyWebSocket.clients list is updated.

Contact
--------------------
Please let me know if you spot any errors or for any other reason: eposta@cankavaklioglu.name.tr