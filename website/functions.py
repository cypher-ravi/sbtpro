from .models import Plan

def send_sms_message(number):
    #url = API for sending message for download link
    app_link_for_playstore = "https://rb.gy/teh3kc"
    message = f"Thank you for your great interest \nDownload Our App For\n Discount and Exciting offers {app_link_for_playstore}"
    
    return number
