import logging
import os
import datetime
from logging.handlers import RotatingFileHandler
import time
from subprocess import call
from time import gmtime, strftime
import re
import logging.handlers
 
import myRotatingFileHandler

path = ''
Interval = ''
Value = 0

class config:
    def __init__(self, givenPath, interval, value):
        global path
        global Interval
        global Value
        path = givenPath
        Interval = interval
        Value = value

    def remove_file_by_days(self):
        now = time.time()
        cutoff = now - (value * 86400)
        files = os.listdir(path)
        file_path = os.path.join(path)

        for xfile in files:
            filePath = file_path + xfile
            if os.path.isfile(filePath):
                t = os.stat(filePath)
                c = t.st_ctime
                if c < cutoff:
                    print 'removing file...'
                    print filePath
                    os.remove(filePath)

    def remove_file_by_hours(self):
        dir_to_search = os.listdir(path)
        for file in filenames:
            curpath = os.path.join(path, file)
            file_modified = datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(hours = Value):
                print 'removing file...'
                print curpath
                os.remove(curpath)

    def remove_file_by_minutes(self):
        dir_to_search = os.listdir(path)
        for file in dir_to_search:
            curpath = os.path.join(path, file)
            file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
            if datetime.datetime.now() - file_modified > datetime.timedelta(hours = Value/60 ):
                print 'removing file...'
                print curpath
                os.remove(curpath)

    def logger(self , inputStr):
        dateTime = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        fileName = 'log-'+dateTime+'.log'
        Path = path 
        logger = logging.getLogger("Rotating Log")
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = myRotatingFileHandler.myRotatingFileHandler(Path, maxBytes=1024000*10, backupCount=5)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
 
        for i in range(1000000):
            logger.debug("This is test log line %s" % i)
    
    def debug(self, inputStr):
        if Interval == 'days':
            self.remove_file_by_days()
        if Interval == 'hours':
            self.remove_file_by_hours()
        if Interval == 'minutes':
            self.remove_file_by_minutes()
        self.logger(inputStr)
