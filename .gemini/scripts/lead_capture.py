import http.server
import socketserver
import urllib.parse
import csv
import os

PORT = 5000
HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../gutguard_landing.html'))
LEADS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../leads.csv'))

class LeadHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(HTML_PATH, 'rb') as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/signup':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            email = params.get('email', [None])[0]

            if email:
                file_exists = os.path.isfile(LEADS_FILE)
                with open(LEADS_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    if not file_exists:
                        writer.writerow(['Email'])
                    writer.writerow([email])
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"message": "Success! We\'ll be in touch."}')
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"message": "Invalid email."}')

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), LeadHandler) as httpd:
        print(f"GutGuard Validation Server running at http://localhost:{PORT}")
        print(f"Serving: {HTML_PATH}")
        print(f"Saving leads to: {LEADS_FILE}")
        httpd.serve_forever()
