from .models import Plan
import requests
def send_sms_message(number):
    #url = API for sending message for download link
    message = f"Thank you for your great interest \nDownload Our App For\n Discount and Exciting offers {app_link_for_playstore}"
    app_link_for_playstore = requests.get("https://rb.gy/teh3kc")
    
    return number
