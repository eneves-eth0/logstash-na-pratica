#!/usr/bin/python
import datetime
import time
import random
import sys
import argparse
from faker import Faker
from faker.providers import internet

log_lines = 1000
fake = Faker()
tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
status_code = ['200','301','302','400','401','403','404','500']

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = 'access_log_'+timestr+'.log'
f = open(filename,'w')
for _ in range(log_lines):
    ip = fake.ipv4()
    otime = fake.date_time_between('-1M')
    dt = otime.strftime('%d/%b/%Y:%H:%M:%S')
    vrb = fake.http_method()
    uri = fake.uri_path()
    resp = random.choice(status_code)
    byte = int(random.gauss(5000,50))
    ref = fake.uri()
    user_agent = fake.user_agent()
    f.write('%s - - [%s %s00] "%s /%s HTTP/1.0" %s %s "%s" "%s"\n' % (ip,dt,tz,vrb,uri,resp,byte,ref,user_agent))
    f.flush()
f.close()