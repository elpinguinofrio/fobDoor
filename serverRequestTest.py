#import requests
import urllib.request
import json
import datetime
from dateutil.parser import parse


def read_user_info(code):
    url = "http://192.168.0.110:8003/state/members/" + str(code)
    obj = {}
    try:
        raw_json = urllib.request.urlopen(url).read().decode('utf8')
        obj = json.loads(raw_json)
    except:
        pass
    return obj

def user_get_duedate(user_info):
    raw_date = user_info['membershipDue']
    date = parse(raw_date)
    return date

duedate = user_get_duedate(read_user_info("0007978161"))
now = datetime.datetime.now()

print(str(now))
print(str(duedate))

print(duedate.replace(tzinfo=None) > now.replace(tzinfo=None))