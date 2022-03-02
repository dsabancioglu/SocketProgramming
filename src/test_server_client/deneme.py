#pylint: skip-file
import datetime
import logging

now = datetime.datetime.now().strftime("%x").replace("/",".") 
filename = now + ".log"
print(now, filename)
print(type(now))
# # logging.basicConfig(filename='{}.log'.format(now.strftime("%x")), level=logging.INFO)
# x= "bb.log"
logging.basicConfig(filename= filename, level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') #dosyayı main'in oldugu yere acti

logging.info('is when this event was logged.')

