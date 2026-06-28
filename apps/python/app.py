# CLO835 Assignment 2 — Python 3.14 starter
# VERSION 0.3 — includes student ID in message
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = "0.3"
MESSAGE = "Hello world from the CLO835 class and 029438025!"
PORT = 8080


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/healthz", "/readyz"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write((MESSAGE + "\n").encode())

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    print(f"CLO835 app v{VERSION} listening on :{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
