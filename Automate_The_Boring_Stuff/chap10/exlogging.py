#!/usr/bin/env python
#logging.py

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s priority=%(levelname)s message=%(message)s')
logging.debug('Start of program')

logging.info('hello')