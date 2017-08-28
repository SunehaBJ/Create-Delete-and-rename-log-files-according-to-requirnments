import logging
import os
import sys
import config
from config import config

if __name__ == '__main__':
    obj = config('/var/www/cgi-bin/pythonPractice/test/','minutes', 2)
    obj.debug('abc')
