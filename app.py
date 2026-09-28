"""Controlled source-code fixture. Never expose parse_payload to a public service."""


import json


def parse_payload(text):
    value = json.loads(text)
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object')
    return value


if __name__ == '__main__':
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class DemoHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('X-Frame-Options', 'DENY')
            self.send_header('Strict-Transport-Security', 'max-age=31536000')
            self.end_headers()
            self.wfile.write(b'Controlled BultShield header fixture. No user input is executed.')

    HTTPServer(('127.0.0.1', 8080), DemoHandler).serve_forever()
