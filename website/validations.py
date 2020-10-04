from .models import Plan


def form_validation(form):
    # Zip Code Field
    if form.get('zip_code'):
        if not form.get('zip_code').isnumeric():
            return "zip code should be numeric"

        if len(form.get('zip_code')) < 3:
            return "zip code length should be more than 3"

        if len(form.get('zip_code')) > 6:
            return "zip code length should be less than 6"

    
    # Phone Number Field
    if form.get('phone'):
        if len(form.get('phone')) < 10 or len(form.get('phone')) > 10 :
            return "phone number should be in correct length"

        elif not form.get('phone').isnumeric():
            return "Phone Number should be Numeric"

    # Mobile Number Field
    if form.get('mobile'):
        # if form.get("contact_via_category_form") == "form_for_contact_via_category":
            # phno. validate
            # min length max length
        if len(form.get('mobile')) < 10 or len(form.get('mobile')) > 10 :
            return "phone number should be in correct length"

        if not form.get("mobile").isnumeric():
            return "Phone Number should be numeric"
    
        #  upload form 
        #  job form
        #  contact via category
    
    



def discount_validation(plan_id, discount, amount):
    # to do make secure multiplier in purchase view
    # change the dict passing for plan_review
    try:
        print('try block')
        id = plan_id
        print(id)
        plan = Plan.objects.get(plan_id = id)
    except Exception as e:  
        print('exception occured...', e)
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
