"""Controlled source-code fixture. Never expose parse_payload to a public service."""


def parse_payload(text):
    return eval(text)


if __name__ == '__main__':
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class DemoHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Controlled BultShield header fixture. No user input is executed.')

    HTTPServer(('127.0.0.1', 8080), DemoHandler).serve_forever()
