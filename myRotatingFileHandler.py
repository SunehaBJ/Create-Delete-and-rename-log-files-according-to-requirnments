import datetime
#import logger 
import os
import sys
import logging
from logging.handlers import BaseRotatingHandler
import time


class myRotatingFileHandler(BaseRotatingHandler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0):
        dateTime = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        
        filename = filename +'/log-'+dateTime+'.log'       
        if maxBytes > 0:
            mode = 'a'
        BaseRotatingHandler.__init__(self, filename, mode, encoding, delay)
        self.maxBytes = maxBytes
        self.backupCount = backupCount

    def doRollover(self):
        dateTime = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        #fileName = 'log-'+dateTime+'.log'
        df = ''
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sf = self.baseFilename+'/'+'log-'+ datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.log'
                df = self.baseFilename+'/'+'log-'+ datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.log'
                if os.path.exists(sf):
                    if os.path.exists(df):
                        os.remove(df)
                    os.rename(sf, df)
            wkspFldr = os.path.dirname(self.baseFilename)
            df = wkspFldr+'/'+'log-'+ datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.log'
            print 'LOG FILE ---> ',df
            if os.path.exists(df):
                os.remove(df)
            if os.path.exists(self.baseFilename):
                os.rename(self.baseFilename, df)
        if not self.delay:
            self.stream = self._open()

    def shouldRollover(self, record):
        if self.stream is None:                 # delay was set...
            self.stream = self._open()
        if self.maxBytes > 0:                   # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream.seek(0, 2)  #due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        return 0
