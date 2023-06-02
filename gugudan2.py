from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')  # charset=utf-8 추가
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>구구단</title></head>', 'utf-8'))
            self.wfile.write(bytes('<body><h1>구구단</h1>', 'utf-8'))
            self.wfile.write(bytes('<form method="POST">', 'utf-8'))
            self.wfile.write(bytes('<input type="number" name="number" placeholder="숫자를 입력하세요">', 'utf-8'))
            self.wfile.write(bytes('<input type="submit" value="계산">', 'utf-8'))
            self.wfile.write(bytes('</form>', 'utf-8'))
            self.wfile.write(bytes('</body></html>', 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes('Not Found', 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        query = parse_qs(post_data)
        number = int(query['number'][0])

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')  # charset=utf-8 추가
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>구구단</title></head>', 'utf-8'))
        self.wfile.write(bytes('<body><h1>구구단</h1>', 'utf-8'))
        self.wfile.write(bytes('<h2>결과:</h2>', 'utf-8'))
        self.wfile.write(bytes('<ul>', 'utf-8'))
        for i in range(1, 10):
            result = f'{number} x {i} = {number * i}'
            self.wfile.write(bytes(f'<li>{result}</li>', 'utf-8'))
        self.wfile.write(bytes('</ul>', 'utf-8'))
        self.wfile.write(bytes('</body></html>', 'utf-8'))

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print('서버가 시작되었습니다.')
    print(f'http://localhost:{PORT}/ 로 접속하세요.')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
