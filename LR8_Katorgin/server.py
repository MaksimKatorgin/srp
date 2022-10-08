from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 9000)# Порт сервера сменен, во избежании путаниц с Лабораторной работой №7
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
