#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Racine /
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        # Endpoint /data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode("utf-8"))

        # Endpoint /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        # Gestion des erreurs 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    port = 8000
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()
