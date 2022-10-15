from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 9500)# Порт сервера сменен, во избежании путаниц с предыдущими Лабораторными работами
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()