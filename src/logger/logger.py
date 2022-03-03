#pylint: skip-file
import logging
import datetime
import sys

sys.dont_write_bytecode = True

def setup_logger(name):
    now = datetime.datetime.now().strftime("%x").replace("/",".") 
    file_name = name + now + ".log"
    logger = logging.getLogger(name + "logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s %(message)s','%I:%M:%S:%f')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger