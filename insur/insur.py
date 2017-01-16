#!/usr/bin/env python
#coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

import sys

from app import application

from tornado.options import define,options
define("port",default=8888,help="run on th given port",type=int)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
	main()