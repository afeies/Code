from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random
import urllib.parse

class RandomNumberHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/random':
            # Generate a random number between 1 and 100
            random_number = random.randint(1, 100)
            
            # Create response data
            response_data = {
                "random_number": random_number,
                "message": "Here's your random number!"
            }
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            # self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
            self.end_headers()
            
            # Write JSON response
            self.wfile.write(json.dumps(response_data).encode())
        
        elif self.path == '/random2':
            # Generate a random number between 1 and 100
            random_number = random.randint(1, 100)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # Write text response
            self.wfile.write(f'{random_number}'.encode())
        
        elif self.path == '/other':
            # Send HTML response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Write HTML response
            self.wfile.write(b'<h1>Hello World</h1>')
        
        elif self.path == '/doc':
            try:
                with open('doc.html', 'r') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'File not found')
        
        elif self.path.startswith('/file'):
            return
            parsed = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(parsed.query)
            if 'filename' in query:
                filename = query['filename'][0]
                try:
                    with open(filename, 'r') as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(content.encode())
                except FileNotFoundError:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'File not found')
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Missing filename parameter')
        
        else:
            # 404 for other paths
            self.send_response(404)
            # self.send_header('Content-type', 'application/json')
            # self.end_headers()
            
            # error_response = {"error": "Endpoint not found"}
            # self.wfile.write(json.dumps(error_response).encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RandomNumberHandler)
    print(f"Server running on http://localhost:{port}")
    print("Available endpoint:")
    print("  GET /random - Returns a random number")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()