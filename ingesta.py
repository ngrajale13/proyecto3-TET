import wget
import time

url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
while True:
    wget.download(url)
    time.sleep(86400)