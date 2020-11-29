import requests 
import time 
from datetime import datetime


def load_site_timer(url):
    start_timer= time.time()
    requests.get(url)
    response_time = time.time() - start_timer
    return response_time

print(load_site_timer('https://www.programiz.com/python-programming/datetime/current-time'))



def load_site_timer(url):
    start_timer= datetime.now()
    requests.get(url)
    response_time = datetime.now() - start_timer
    return response_time

print(load_site_timer('https://www.programiz.com/python-programming/datetime/current-time'))
