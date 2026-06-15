#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Serving at {url}  (Ctrl+C to stop)")
    webbrowser.open(url)
    httpd.serve_forever()
