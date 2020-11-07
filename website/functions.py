import pathlib
from .models import Plan
import requests
import math 
import json



fn = pathlib.Path(__file__).parent.parent / 'config.json'
with open(fn,"r") as params:
    parameters = json.load(params)

phone = parameters['admin_phone']
app_url = parameters['app_link']

def send_sms_message(number):
    #url = API for sending message for download link
    app_link_for_playstore = app_url
    message = f"Thank you for your great interest ,Download Our App For Discount and Exciting offers"
    url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={number}&route=TA&msgtype=1&sms={message} \n {app_link_for_playstore}"
    response = requests.request("GET",url)
    return number

def haver_sine_formula(lat, lng, distance):
    # Haversine formula = https://en.wikipedia.org/wiki/Haversine_formula
    R = 6378.1  # earth radius
    bearing = 1.57  # 90 degrees bearing converted to radians.
    distance = distance  # distance in km

    lat1 = math.radians(lat)  # lat in radians
    lng1 = math.radians(lng)  # long in radians

    lat2 = math.asin(math.sin(lat1)*math.cos(distance/R) +
                        math.cos(lat1)*math.sin(distance/R)*math.cos(bearing))

    lng2 = lng1 + math.atan2(math.sin(bearing)*math.sin(distance/R)*math.cos(lat1),
                                math.cos(distance/R)-math.sin(lat1)*math.sin(lat2))

    lat2 = math.degrees(lat2)
    lng2 = math.degrees(lng2)

    return lat2, lng2
