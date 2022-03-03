#pylint: skip-file
import datetime
import logging

now = datetime.datetime.now().strftime("%x").replace("/",".") 
filename = now + ".log"

print(now, filename)
print(type(now))

''' Burada instance uzerinden config yapilmiyor, logging üzerinden genel bir konfig yapılıyor (bu şekilde iki farklı log dosyası yapmaya çalıştığımda, 
    ikisini tek bir dosya olarak algıladı, hem server hem client loglarını aynı dosyaya yazdı )
    
    logger.py'de server ve client log dosyasını özelleştirmek için konfigürasyonları instance üzerinden yaptım,
    bu sayede ikisine farklı özellikler verip birbirinden bağımsız olarak çalışmalarını sağladım.
'''

logging.basicConfig(filename= filename, level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') #dosyayı main'in oldugu yere acti

logging.info('is when this event was logged.')

