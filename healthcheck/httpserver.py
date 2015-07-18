'''
Created on Jan 9, 2015

@author: Autumn
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

import logging
logger = logging.getLogger(__name__)

class HealthCheckHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("OKOKOK")
        return
    
class HealthCheckHttpServer(Thread):
    
    def __init__(self, port=10241):
        
        Thread.__init__(self)
        self.port = port
        self.server = HTTPServer(('', self.port), HealthCheckHandler)
        self.__closed__ = None
        
    def stop(self):
        self.server.server_close()
        self.__closed__ = True
    
        
    def is_stopped(self):
        return self.__closed__
    
        
    def run(self):
        
        try:
            
            logger.info( 'Started httpserver on port %d' % self.port)
            self.__closed__ = False
            self.server.serve_forever()
        
        except KeyboardInterrupt:
            logger.info( '^C received, shutting down the web server')
            self.server.socket.close()
            self.__closed__ = True

        except Exception as e:
            logger.exception(e)
    


