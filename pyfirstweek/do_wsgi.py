#！/usr/bin/python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)  #"""Create a new WSGI server listening on `host` and `port` for `app`"""
print('Serving HTTP on port 8000...')

httpd.serve_forever()   #Handle one request at a time until shutdown.