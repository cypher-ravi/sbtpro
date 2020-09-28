from .models import Plan

def send_sms_message(number):
    #url = API for sending message for download link
    app_link_for_playstore = "https://rb.gy/teh3kc"
    message = f"Thank you for your great interest \nDownload Our App For\n Discount and Exciting offers {app_link_for_playstore}"
    
    return number

def discount_validation(plan_id, discount, amount):
    # to do make secure multiplier in purchase view
    # change the dict passing for plan_review
    try:
        print('try block')
        id = plan_id
        print(id)
        plan = Plan.objects.get(plan_id = id)
    except:  
        print('exception occured...')
        return ({'discount_applied':'' ,'total':'' ,'error': 'entered amount is invalid'})
    if plan.plan_amount == amount:
        if  discount == 0:
            return ({'discount_applied':'' ,'total':'' ,'error': 'Value should not be 0'})
        print('plan')
        print(discount)
        if discount >= plan.minimum_discount and discount <= plan.maximum_discount:
            print('min max')
            amount = plan.plan_amount
            # default_val = 100
            
            total = discount * amount
            return ({'discount_applied': discount,'total':total ,'error': None})
        else:
            print('else min max')
            return ({'discount_applied':'' ,'total':'' ,'error': 'entered amount is invalid'})
    else:
        print('critical error')
        return ({'discount_applied':'' ,'total':'' ,'error': 'Plan Amount is Invalid'})
    return ({'error':'Invalid Request'})
