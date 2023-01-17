from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = 'localhost'
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    data_file_address = 'data.txt'


    def _write_data_to_file(self, data):
        with open(self.data_file_address, 'a', encoding='utf-8') as list_file:
            list_file.write(data)
            list_file.write('\n')

    def do_GET(self):
        result_string = 'Hello, World wide web!'

        self.send_response(200)
        self.send_header("Content-type", "application/text")
        self.end_headers()
        self.wfile.write(bytes(result_string, "utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        data_from_request = str(post_data)

        self._write_data_to_file(data_from_request)

        self.send_response(201)
        self.send_header("Content-type", "application/text")
        self.end_headers()
        self.wfile.write(bytes(post_data))
        print(data_from_request)



if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
