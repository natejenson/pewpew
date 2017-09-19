from datetime import datetime
from urllib.request import Request, urlopen
import ssl
import time
import argparse

def ping(url, useragent):
    try:
        time = str(datetime.now())
        req = Request(url, headers={'User-Agent': useragent})
        response = urlopen(req, context=ssl._create_unverified_context())
        json = response.read()
        print('RESPONSE @', time, ' = ', response.getcode(), json)
    except IOError as e: 
        print('FAILURE @', time, ' = ', e)


def go(url, t, useragent):
    print('pinging ' + url + ' every ' + str(t) + ' seconds...')
    while(True):
        useragent = useragent or "pewpew"
        ping(url, useragent)
        time.sleep(t)

# run it!
parser = argparse.ArgumentParser(description='Send a GET request on an interval')
parser.add_argument('target', metavar='U', type=str, help='The URL to target')
parser.add_argument('t', metavar='T', type=int, help='The interval in seconds')
parser.add_argument('--useragent', dest='useragent', type=str, nargs='?', help='set the User-Agent header')
args = parser.parse_args()

go(args.target, args.t, args.useragent)
    
