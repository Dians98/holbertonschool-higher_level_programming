#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        match(self.path):
            case '/data':
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                response = {"name": "John", "age": 30, "city": "New York"}
                response_json = json.dumps(response)
                self.wfile.write(response_json.encode("utf-8"))

            case "/status":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(bytes("OK", "utf8"))

            case "/":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes("Hello, this is a simple API!", "utf8"))

            case _:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes("Endpoint not found", "utf8"))


# configure server
port = 8000
server_address = ("127.0.0.1", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

# run server
httpd.serve_forever()
