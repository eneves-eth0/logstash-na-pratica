#!/usr/bin/python
import time
import datetime
import pytz
import numpy
import random
import gzip
import zipfile
import sys
import argparse
from faker import Faker
from faker.providers import internet
from random import randrange
#from tzlocal import get_localzone

fake = Faker()
#otime = datetime.datetime.now()
tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
#fake.add_provider(internet)
status_code = ['200','301','302','400','401','403','404','500']
for _ in range(100):
    ip = fake.ipv4()
    otime = fake.date_time_between('-1M')
    dt = otime.strftime('%d/%b/%Y:%H:%M:%S')
    vrb = fake.http_method()
    uri = fake.uri_path()
    resp = random.choice(status_code)
    byte = int(random.gauss(5000,50))
    ref = fake.uri()
    user_agent = fake.user_agent()
    #,vrb,uri,resp,byt
    print(f'%s - - [%s %s00] "%s /%s HTTP/1.0" %s %s "%s" "%s"' % (ip,dt,tz,vrb,uri,resp,byte,ref,user_agent))