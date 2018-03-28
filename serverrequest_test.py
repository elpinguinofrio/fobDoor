#import requests
import urllib.request
import json
import datetime
from dateutil.parser import parse

DEFAULT_USER_NAME = "Fucker"

def get_user_info(user_code):
    raw_json = urllib.request.urlopen("http://192.168.0.110:8003/state/members/" + str(user_code)).read().decode('utf8')
    obj = json.loads(raw_json)
    return obj

def user_get_duedate(user_info):
    return parse(user_info['membershipDue'])
    
def user_get_name(user_info):
    return user_info['name']

def check_can_the_user_get_in(user_code):
    try:
        # try to read date from DB
        user_info = get_user_info(user_code)
        print(user_info)
        duedate = user_get_duedate(user_info)
        name = user_get_name(user_info)
    except:
        # yesterday
        duedate = datetime.datetime.now() - datetime.timedelta(1)
        name = DEFAULT_USER_NAME
    now = datetime.datetime.now()

    print(str(now))
    print(str(duedate))

    door_access = duedate.replace(tzinfo=None) >= now.replace(tzinfo=None)
    return door_access

check_can_the_user_get_in("0007938944")