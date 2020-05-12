import os
from http.server import HTTPServer, SimpleHTTPRequestHandler, HTTPStatus


class TestHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        """Serve a GET request."""
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(os.getenv(
            "APP_ENV", "NOT FOUND APP_ENV").encode('utf-8'))

    def do_HEAD(self):
        """Serve a GET request."""
        self.do_GET()


def main():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, TestHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
