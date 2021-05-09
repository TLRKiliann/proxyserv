#!/usr/bin/python3
# -*- coding: utf-8 -*-


import http.server
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import requests
import requests_raw
import time

host = "localhost"
port = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        #payload = {'key1': 'value1', 'key2': 'value2'}
        url = 'https://www.myip.com/'
        rg = requests.get('https://www.myip.com/')
        #rg = requests.get('https://www.myip.com/', data=payload)
        print("Status :", rg.status_code)
        print("\n")
        print(rg.url)
        print("\n")
        print(rg.headers)
        print("\n")
        print(rg.encoding)
        print("\n")
        rg.content
        print(type(rg.content))
        print(rg.content[0:400])
        print("\n")
        rg.text
        print(type(rg.text))
        print(rg.text[0:400])
        print("\n")
        data = {'title':'Pyton Requests','body':'Requests are qwesome','userId':1} 
        rp = requests.post('https://www.myip.com/posts', data, stream = True)
        print(type(rp.raw))
        print(rp.raw)
        print(type(rp.raw.read(30)))
        print(rp.raw.read(30))

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write(bytes("<html><head><title>https://my_server2_to_test.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s </p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is web server 2.</p>", "utf-8"))
        self.wfile.write(bytes("<p> --- GET URL : </p>", "utf-8"))
        self.wfile.write(bytes(rg.url, "utf-8"))
        self.wfile.write(bytes("<p> --- GET + Headers-Content-Type : </p>", "utf-8"))
        self.wfile.write(bytes(rg.headers['content-type'], "utf-8"))
        self.wfile.write(bytes("<p> --- Encoding : </p>", "utf-8"))
        self.wfile.write(bytes(rg.encoding, "utf-8"))
        self.wfile.write(bytes("<p> --- Text data : </p>", "utf-8"))
        self.wfile.write(bytes(rg.text, "utf-8"))
        self.wfile.write(bytes("<p> --- Content : </p>", "utf-8"))
        self.wfile.write(bytes(rg.content))
        self.wfile.write(bytes("<p> --- Raw : </p>", "utf-8"))
        self.wfile.write(bytes(rp.raw.read(30)))
        self.wfile.write(bytes("<p> --- GET finished--- </p>", "utf-8"))
        self.wfile.write(bytes("------------- <br>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((host, port), MyServer)
    print("Server started http://%s:%s" % (host, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")