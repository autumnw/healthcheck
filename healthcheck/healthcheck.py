'''
Created on Jan 9, 2015

@author: Autumn
'''
from threading import Thread
import time
import subprocess
from httpserver import HealthCheckHttpServer
import json

import logging
logger = logging.getLogger(__name__)

class HealthCheck:
    
    def __init__(self, cfg):
        with open(cfg, 'rt') as f:
            config = json.load(f)
        self.interval = config['interval']
        self.command = config['command']
        self.check_server = None
    
    
    def check_status(self):
        try:
            logger.debug("cmd : %s" % self.command)
            p = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
            logger.debug("return code : %d" % p.returncode)
            if p.returncode == 0:
                if not self.check_server:
                    self.check_server = HealthCheckHttpServer()
                    self.check_server.start()
                else:
                    logger.info( "Http server is running")
            else:
                if self.check_server:
                    logger.info( "Stop http server" )
                    self.check_server.stop()
                    self.check_server = None
        except Exception as e:
            logger.exception(e)
        
    
    def start(self):
        while True:
            self.check_status()
            time.sleep(5)

## For testing
if __name__ == '__main__':
    check = HealthCheck()
    check.start()
    
