#pylint: skip-file
import logging
import datetime

 # logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%I:%M:%S')

def setup_logger(name):
    now = datetime.datetime.now().strftime("%x").replace("/",".") 
    file_name = name + now + ".log"
    logger = logging.getLogger(name + "logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger