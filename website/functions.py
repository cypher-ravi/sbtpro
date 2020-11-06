from .models import Plan
import requests
import math 

def send_sms_message(number):
    #url = API for sending message for download link
    message = f"Thank you for your great interest \nDownload Our App For\n Discount and Exciting offers {app_link_for_playstore}"
    app_link_for_playstore = requests.get("https://rb.gy/teh3kc")
    
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
