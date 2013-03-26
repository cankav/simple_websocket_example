simple websocket example
========================

Simple websocket example with javascript client and python Tornado server files

Websockets provide convenient server to client messaging. To work with websockets you will need a websocket enabled client/server pair. Check page below for client websocket support:

http://caniuse.com/websockets

Sections below explain files in this example.

client.js
-------------
Contains javascript client code, which opens a websocket to the server and attempts to re-open it on websocket close event.

client.js should run on client side, which may be embeded to your html file. On page load the code tries to establish websocket connection with address: "ws://localhost:8080/websocket". If for some reason connection is closed, javascript code will try to re-open the connection after waiting for one second.

+ Insert your custom processing into the ws.onmessage function. 
+ Use the ws_send function to send a message to the server. 

Please note that you will need jquery for this example to work.

client.html
-------------
Bare-bones html file which includes jquery from Google's CDN and client.js.

tornado_server.py
--------------------
Python code in tornado_server.py uses [Tornado](http://www.tornadoweb.org/) web server to open a websocket connection as well as an http connection. Once Tornado is installed (pip install tornado) you can use the command below to initialize the web server:

<pre>
python tornado_server.py
</pre>

To test if http server is running you can visit http://localhost:8080/hello-tornado page. Please note that websockets are not accessible through http. So do not try to access /websocket via your browser.

If it all goes according to the plan you should see the following on your browser's console when you access your html document:

<pre>
ws open
ws_send sent
</pre>

Python code will also provide some output:

<pre>
WebSocket opened
msg recevied {"event":"register"}
</pre>

Server code stores connected clients in its MyWebSocket.clients data structure. Once a message is received from a client all other recorded clients are forwarded the sent message. If a client disconnects for some reason the MyWebSocket.clients list is updated.

Contact
--------------------
Please let me know if you spot any errors or for any other reason: eposta@cankavaklioglu.name.tr
