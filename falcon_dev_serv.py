from wsgiref import simple_server

from falcon_frm.app import app


ip_address = '127.0.0.1'
port = 8888

if __name__ == '__main__':
    httpd = simple_server.make_server(ip_address, port, app)
    httpd.serve_forever()
