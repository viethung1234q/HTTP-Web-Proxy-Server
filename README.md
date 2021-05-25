# HTTTP-WEB-PROXY-SERVER

# Đoàn Việt Hưng - hungdoan2712@gmail.com

Your task is to develop a small web proxy server which is able to cache web pages. It is a very simple
proxy server which only understands simple GET-requests, but is able to handle all kinds of objects -
not just HTML pages, but also images.

Generally, when the client makes a request, the request is sent to the web server. The web server then
processes the request and sends back a response message to the requesting client. In order to improve
the performance we create a proxy server between the client and the web server. Now, both the
request message sent by the client and the response message delivered by the web server pass through
the proxy server. In other words, the client requests the objects via the proxy server. The proxy server
will forward the client’s request to the web server. The web server will then generate a response
message and deliver it to the proxy server, which in turn sends it to the client.

# RUNNING THE PROXY SERVER

Run the proxy server program using your command prompt and then request a web page from your
browser. Direct the requests to the proxy server using your IP address and port number. For e.g:

              http://localhost:8888/www.google.com

To use the proxy server with browser and proxy on separate computers, you will need the IP address
on which your proxy server is running. In this case, while running the proxy, you will have to replace
the “localhost” with the IP address of the computer where the proxy server is running. Also note the
port number used. You will replace the port number used here “8888” with the port number you have
used in your server code at which your proxy server is listening.

# CONFIGURING YOUR BROWSER

You can also directly configure your web browser to use your proxy. This depends on your browser.
In Internet Explorer, you can set the proxy in Tools > Internet Options > Connections tab > LAN
Settings. In Netscape (and derived browsers such as Mozilla), you can set the proxy in Tools >
Options > Advanced tab > Network tab > Connection Settings. In both cases you need to give the
address of the proxy and the port number that you gave when you ran the proxy server. You should be
able to run the proxy and the browser on the same computer without any problem. With this approach,
to get a web page using the proxy server, you simply provide the URL of the page you want. For e.g:
            
              http://www.google.com
