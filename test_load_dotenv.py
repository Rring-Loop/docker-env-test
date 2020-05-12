import os
from http.server import HTTPServer, SimpleHTTPRequestHandler, HTTPStatus
from dotenv import load_dotenv


def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print("load env: %s" % dotenv_path)


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
    load_env()
    server_address = ('', 80)
    httpd = HTTPServer(server_address, TestHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
