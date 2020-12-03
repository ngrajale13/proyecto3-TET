import wget
import time
import boto3

s3 = boto3.resource('s3')
url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
while True:
    data = open(wget.download(url), 'rb')
    s3.Bucket('proyect3-tet').put_object(Key='test.json', Body=data)
    time.sleep(86400)