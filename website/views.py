from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
from Vendor.models import KeyWord, Vendor, VendorServices
from Customer.models import *
from .DummyData import DummyData
# To import for login,Signup
"""
from django.contrib.auth.models import User
"""

import json
import math
import random


import requests
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
# validations
from django.core.validators import validate_email
from django.http import JsonResponse

#importing func from function.py
from .functions import *
from .models import *
# FOR PAYTM---------------------
from .PayTm import CheckSum
from .validations import *

# FOR PAYTM End-----------------------------------
# TODO
    # Need to create a function which change configuration of backend as well as frontend using our config.json
    # Nedd to add a order id function


# ! NEVER SHOW MERCHANT ID AND KEY !
MID = "VdMxPH61970223458566"  # MERCHANT ID
MKEY = "1xw4WBSD%bD@ODkL"  # MERCHANT KEY


with open("config.json", "r") as params:
    parameters = json.load(params)



def index(request):
    category = Categories.objects.all()
    # Logic for services
    services = Service.objects.all()

    # testimonials
    testimonials = AddTestimonial.objects.all()

    # Another section started
    vendor = TOP.objects.all()

    plans = Plan.objects.all()
    return render(request, 'website/index.html',
                  {'plans': plans, 'category': category, 'services': services, 'vendor': vendor,'testimonials':testimonials})

# Function to take input from form and send it through email
def freelisting(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        # Validate
        resp = form_validation(request.POST)
        if resp != None:
            messages.warning(request,resp)
            return redirect('website:listing')
        Company_name = request.POST.get('companyname', '')
        location = request.POST.get('location', '')
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        mobile = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        # send mail function from django.core.mail import send mail
        send_mail(
            subject='New Vendor registered',
            message=f"Company Name = {Company_name}\nName = {first_name + ' ' + last_name}\nMobile No. = {mobile}\nAddress = {city + ',' + state + ',' + zip_code}",
            from_email= parameters['from_email'],
            recipient_list=[parameters['to_email']],
            fail_silently=False
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
        )
        # checks on values of form and using django.contrib import message for alert messages
        if Company_name:

            listing = FreeListing(Company_name=Company_name, location=location, first_name=first_name,
                                  last_name=last_name, city=city, state=state, zip_code=zip_code, mobile=mobile,
                                  email=email)
            listing.save()
            messages.success(request, 'Form submission successful. SBT Professional team Contact You within 24'
                                      'hours.')
            return redirect('website:Sbthome')
    return render(request, 'website/forms/freelisting.html', {'vendor': vendor, 'category': category})


def customer_membership(request):
    category = Categories.objects.all()
    redirect1 = '/sbt/purchase'

    plans = Plan.objects.all()
    vendor = TOP.objects.all()

    return render(request, 'website/pages/membership.html', {'plans': plans, 'vendor': vendor, 'category': category,'redirect':redirect1})


def jobs(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    if request.method == "POST":
        name = request.POST.get('contactName', '')
        mobile = request.POST.get('contactmobile', '')
        education = request.POST.get('contactEducation', '')
        experience = request.POST.get('contactexperience', '')
        print(experience)

        # checks on values of form and using django.contrib import message for alert messages
        resume = Job(name=name, mobile=mobile,
                     education=education, experience=experience)
        resume.save()
        messages.success(request, 'Form submission successful. SBT Professional team Contact You within '
                                  '24 hours.')
        send_mail(
            subject='New Job seeker created resume',
            message=f"Employee Name = {name}\nMobile No. = {mobile}\nExperience = {experience}\nEducation = {education}",
            from_email= parameters['from_email'],
            recipient_list=[parameters['to_email']],
            fail_silently=False
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
        )
        return render(request, 'website/forms/job_form.html', {'vendor': vendor, 'category': category})

    return render(request, 'website/forms/job_form.html', {'vendor': vendor, 'category': category})


def upload_resume(request):
    category = Categories.objects.all()
    try:
        if request.method == "POST":
            name = request.POST.get('contactName', '')
            uploaded_resume = request.FILES['myfile']
            if name:
                resume = Upload_resume(name=name, Resume=uploaded_resume)
                resume.save()
                fs = FileSystemStorage()
                fs.save(uploaded_resume.name, uploaded_resume)
                messages.success(request,
                                 'Resume submission successful. SBT Professional team Contact You within 24 hours.')
                try:
                    file = settings.MEDIA_URL[1:] + str(uploaded_resume)
                    from django.core.mail import EmailMessage
                    msg = EmailMessage('New job Seeker on your website', 'name =' + name, parameters['from_email'],
                                       [parameters['to_email']])
                    msg.attach_file(file)
                    msg.send()
                except Exception as e:
                    messages.error(request,'Failed to uplaod Resume! Try Again.')
                    return redirect('website:Sbthome')
            else:
                messages.error(request, 'Before submit resume Enter your name')

        return render(request, 'website/job_form.html', {'category': category})
    except:
        return render(request, 'website/404.html')

def download(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        number = request.POST.get('number')
        if number.isnumeric():
            send_sms_message(number)
            messages.success(request,'Link sent successfully check your inbox!')
            return redirect('website:Sbthome')
        else:
            messages.warning(request,'Enter a number!')
            return render(request, 'website/pages/downloadapp.html', {'vendor': vendor, 'category': category})
    return render(request, 'website/pages/downloadapp.html', {'vendor': vendor, 'category': category})


def categories(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    filtered_categories = Categories.objects.filter(category_name=slug)
    related_sub_category = Subcategory.objects.all().filter(category_name__in=filtered_categories)
    return render(request, 'website/pages/category.html',
                  {'filtered_categories': filtered_categories, 'sub_category': related_sub_category,
                   'category': category,'vendor':vendor})


def sub_to_sub_category(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    related_sub_category = Subcategory.objects.all().filter(sub_category_name=slug)
    related_sub_sub_category = Sub_sub_category.objects.all().filter(sub_category_name__in=related_sub_category)
    params = {'slug': slug}
    if related_sub_sub_category.exists():
        return render(request, 'website/pages/subcategory.html',
                      {'sub_category': related_sub_category, 'related_sub_sub_category': related_sub_sub_category,
                       'category': category,'vendor':vendor})
    else:
        return render(request, 'website/forms/contact_via_category.html', {'slug': slug, 'category': category,'vendor':vendor})


# A's here  ------------------

def test(request):
    if request.method =="POST":
        resp = form_validation(request.POST)
        return HttpResponse(f"nahi chala{resp}")

    return render(request, 'website/auth_and_pass/test.html')


"""def purchase(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    # discount won't work if empty
    try:
        if request.user.is_authenticated:
            if request.method == "POST":

                # Validate
                resp = form_validation(request.POST)
                if resp != None:
                    return HttpResponse(resp)

                plan = Plan.objects.get(plan_name=slug)
                order_id = random.randint(1, 9999)
                email_id = request.POST.get('email', '')
                name = request.POST.get('name', '')
                phone = request.POST.get('phone', '')
                address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
                state = request.POST.get('state', '')
                city = request.POST.get('city', '')
                zip_code = request.POST.get('zip_code', '')
                plan_id = plan.plan_id
                print('..........',request.POST.get('discount'))
                try:
                    discount = int(request.POST.get('discount'))
                except ValueError:
                    return HttpResponse('Please select a valid discount value')
                # It checks that discount given according to card amount
                response_dict  = discount_validation(plan_id, discount, plan.plan_amount)
                if response_dict['error'] != None:
                    return HttpResponse(response_dict['error'])
                # only disocunt 0 to 30
                if discount != "":
                    amount = discount * plan.plan_amount
                else:
                    amount = plan.plan_amount

                order = Order(name=name, user = request.user, email_id=email_id, address=address, city=city, state=state, zip_code=zip_code,
                              phone=phone, amount=amount, order_id=order_id, plan_id=plan, order_completed = False)
                order.save()

                # sending details to paytm gateway in form of dict
                detail_dict = {
                    "MID": MID,
                    "WEBSITE": "WEBSTAGING",
                    "INDUSTRY_TYPE_ID": "Retail",
                    "CUST_ID": str(email_id),
                    "CHANNEL_ID": "WEB",
                    "ORDER_ID": str(order_id),
                    "TXN_AMOUNT": str(amount),
                    "CALLBACK_URL": "http://127.0.0.1:8000/sbt/req_handler",
                }

                param_dict = detail_dict
                CheckSum.generateSignature
                param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                    detail_dict, MKEY)
                # print('.................', param_dict)
                return render(request, 'website/order_process/redirect.html', {'detail_dict': param_dict})


            plan = Plan.objects.get(plan_name=slug)
            dict_for_review = {
                'id' : plan.plan_id,
                'name': plan.plan_name,
                'amount': plan.plan_amount,
                'description_1': plan.description_1,
                'description_2': plan.description_2,
                'description_3': plan.description_3,
                'description_4': plan.description_4,
            }

            return render(request, 'website/forms/purchase_form.html', {'plan': plan, 'plan_review': dict_for_review, 'category': category,'vendor':vendor})

        else: # if User is not Authenticated
            return render(request, 'website/auth_and_pass/login.html',{'slug':slug})
    except Exception as e:
        print("An Exception occur \n", e)
        return HttpResponse("There is an error")

@csrf_exempt
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        form = request.POST
        print(form["ORDERID"])

        # another if to handle if user load refresh
        is_order_exist = Order_Payment.objects.filter(order_id = form["ORDERID"]).exists()
        print('............................order', is_order_exist)
        if is_order_exist == False:
            # FOR ALL VALUES
            for i in form.keys():
                response_dict[i] = form[i]
                print(i, form[i])

                if i == "CHECKSUMHASH":
                    response_check_sum = form[i]

            verify = CheckSum.verifySignature(response_dict, MKEY, response_check_sum)
            print(verify)
            # response_dict["STATUS"] = "PENDING"
            print('.........response_dict["STATUS"]', response_dict["STATUS"])
            print("..................", verify)
            if verify and response_dict["STATUS"] != "TXN_FAILURE" or response_dict["STATUS"] == "PENDING":
                order_payment = Order_Payment()
                usr = User()

                # id = models.AutoField(primary_key = True)
                order = Order.objects.get(order_id = response_dict["ORDERID"])

                order_payment.order_summary = order
                # paytm responses
                order_payment.currency = response_dict["CURRENCY"]
                order_payment.gateway_name = response_dict["GATEWAYNAME"]
                order_payment.response_message = response_dict["RESPMSG"] # Txn Success
                # order_payment.bank_name = response_dict["BANKNAME"] # WALLET
                order_payment.Payment_mode = response_dict["PAYMENTMODE"]# PPI
                # MID = models.CharField(max_length=8) # VdMxPH61970223458566
                order_payment.response_code = response_dict["RESPCODE"] # 01
                order_payment.txn_id = response_dict["TXNID"]#  20200905111212800110168406201874634
                order_payment.txn_amount = response_dict["TXNAMOUNT"]#  2400.00
                order_payment.order_id = response_dict["ORDERID"]#  6556
                order_payment.status = response_dict["STATUS"]# TXN_SUCCESS
                order_payment.bank_txn_id = response_dict["BANKTXNID"] #  63209779
                order_payment.txn_date = response_dict["TXNDATE"] #  2020-09-05 18:51:59.0
                # order_payment.refund_amount =  #  0.00
                order_payment.save()
                payment_status = Order_Payment.objects.get(order_id = response_dict["ORDERID"])

                return render(request, 'website/order_process/order_success.html', {'payment':payment_status})
            else:
                Order.objects.filter(order_id= response_dict["ORDERID"]).delete()
                return HttpResponse('Order is not Placed Because of some error. Please <a href="/sbt/">Try Again </a>')
        else:
            payment_status = Order_Payment.objects.get(order_id = form["ORDERID"])
            # Session should create when order is get successfull

            return render(request, 'website/order_process/order_success.html', {'payment':payment_status})
    return HttpResponse('Invalid Request <a href="/sbt/"> Go back Home</a>')

def pricing_multiplier(request):
    if request.method =="POST":

        amount = int(request.POST.get('amount'))
        try:
            discount = int(request.POST.get('discount'))
        except ValueError:
            return JsonResponse({'discount_applied':'' ,'total':'', 'error': 'Expected integer'})
        plan_id = int(request.POST.get('plan_id'))
        response = discount_validation(plan_id, discount, amount)
        # response_dict = json.loads(response.getvalue().decode('utf-8'))
        # print(response_dict)
        return JsonResponse(response)

def order_status(request, slug):
    try:
        obj = Order_Payment.objects.get(order_id = slug)
        obj2 = obj.order_summary
        if obj2.user == request.user:
            paytmParams = dict()

            paytmParams["MID"]     = MID
            paytmParams["ORDERID"] = slug

            checksum = CheckSum.generateSignature(paytmParams, MKEY)

            paytmParams["CHECKSUMHASH"] = checksum

            post_data = json.dumps(paytmParams)

            # for Staging
            url = "https://securegw-stage.paytm.in/order/status"

            # for Production
            # url = "https://securegw.paytm.in/order/status"

            response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
            print(response)

            if response["STATUS"]=="TXN_SUCCESS":
                print("Updating Status")
                obj = Order_Payment.objects.get(order_id = slug)
                obj.status = response["STATUS"]
                obj.response_code = response["RESPCODE"]
                obj.response_message = response["RESPMSG"]
                obj.txn_date = response["TXNDATE"]
                obj.bank_name = response["BANKNAME"]
                obj.save()
                return HttpResponse("order success fully placed")

            return HttpResponse("order is still in pending state")

        elif request.user!=None and request.user.is_authenticated :
            return HttpResponse("Please insert correct orderid")
        else:
            return HttpResponse('Please Login <a href="/sbt/login"> Here First</a>')
    except Exception as e:
        return HttpResponse(f"Requested Order Not Found - {e}") # form to type in order id"""

''' Need to complete this function
def order_id_session(order_id):
    order = Order.objects.get(order_id = order_id)
    all_order = Order.objects.filter(user = order.user)
    order_ids = []
    for i in all_order:
        order_id.append(i)

    usr = request.user.username
    request.session['']
'''


# --------------------------payment/purchase end -----------------------




"""def sign_up(request):
    # have exception of geting same user name
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['create_password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists Please Consider Login')
            return redirect('website:SignUp')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists Please consider Login')
            return redirect('website:SignUp')

        # username validation stuff ----------------
        if len(username) > 15:
            messages.error(request, 'Username must be unique!!')
            return redirect('website:SignUp')

        if not username.isalnum():
            messages.error(
                request, 'Username should contain letters and numbers!!')
            return redirect('website:SignUp')

        # Email Validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Email is not valid')
            return redirect('website:SignUp')
        # Password valdation
        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return redirect('website:SignUp')
        # username should contain numbers and letters

        # create the user
        newuser = User.objects.create_user(username=username, email=email, password=password)
        if newuser.is_staff:
            print('yes')
        else:
            print('no')
        newuser.save()

        messages.success(request, "Your SBT Professionals account has been successfully created")
        return redirect('website:Login')
    else:
        return render(request, 'website/auth_and_pass/register.html')


def log_in(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        redirect_url = request.POST['url']
        try:
            redirect_slug = request.POST['slug']
            flag = True
        except:
            redirect_slug=None
        print('slug.........',redirect_slug)
        print('url.........',redirect_url)
        if User.objects.filter(email=loginusername).exists():
            usr_by_email = User.objects.get(email=loginusername)
            loginusername = usr_by_email.username

        user = authenticate(request, username=loginusername,
                            password=loginpass)  # checks if user is exist
        if user is not None :  # if user exist than create a session using login function
            if  redirect_slug !=None :
                login(request, user)
                messages.success(request, 'Login Successful!')
                return redirect('website:plan-purchase',slug=redirect_slug)

            if redirect_slug == None:
                login(request, user)
                messages.success(request, 'Login Successful!')
                return redirect('website:Sbthome')

        else:
            print('....................user->', user)
            messages.error(request, 'Invalid credentials,Please Try Again!')
            return redirect(log_in)
    return render(request, 'website/auth_and_pass/login.html')

"""
# return redirect(index)




def purchase(request, slug):# plan_id, user, amount,discount,role):
        vendor = TOP.objects.all()
        category = Categories.objects.all()


        plan = Plan.objects.get(plan_id =slug)
        dict_for_review = {
            'id' : plan.plan_id,
            'name': plan.plan_name,
            'amount': plan.plan_amount,
            'description_1': plan.description_1,
            'description_2': plan.description_2,
            'description_3': plan.description_3,
            'description_4': plan.description_4,
        }
        return render(request, 'website/forms/purchase_form.html', {'plan': plan, 'plan_review': dict_for_review, 'category': category,'vendor':vendor})

def customer_card_purchase(request, plan_id):
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    # discount won't work if empty
        # if request.user.is_authenticated:
    discount = request.POST.get('discount')
    if request.method == 'POST':
        if request.user.is_authenticated:
            plan = Plan.objects.get(plan_id = plan_id)

            print('..........',request.user)
            customer = Customer()
            customer.user = request.user
            # customer.customer_id = models.
            # 
            # 
            # 
            # (primary_key=True)
            customer.customer_name = request.POST.get('name')
            customer.last_name = 'Paliwal'
            customer.Address = request.POST.get('address')
            customer.city = request.POST.get('city')
            customer.state = request.POST.get('state')
            customer.zipcode = request.POST.get('zip_code')
            customer.EmailID = request.POST.get('email_id')
            customer.joining_date = timezone.datetime.now()
            customer.gender = 'Alpha Male'
            customer.extra_Info = 'got need a card to swipe'
            customer.Contact_Person = 'GEAZY'
            customer.customer_is_active = True
            customer.subscription_plan_taken = plan

            customer.save()
            user = User.objects.filter(id=request.user.id).first()
            phone = user.phone
            try:
                plan = Plan.objects.get(plan_id=plan_id)
            except:
                return HttpResponse('Please enter a valid Plan Id')

            try:
                discount = int(request.POST.get('discount'))
            except ValueError:
                return HttpResponse('Please select a valid discount value')

            user_amount= plan.plan_amount
            if discount != "" and discount != None:
                response_dict = discount_validation(plan_id, discount, user_amount)
                if response_dict['error'] != None:
                    return HttpResponse(response_dict['error'])
                amount = discount * plan.plan_amount
            else:
                amount = plan.plan_amount

            print('aya..........')
            order_id = random.randint(1, 999999)
            email_id = request.POST.get('email_id')
            name = request.POST.get('name')
            address =request.POST.get('address')
            state =  request.POST.get('state')
            city = request.POST.get('city')
            zip_code = request.POST.get('zip_code')
            plan_id = plan.plan_id

            # Check if user not provide any discount value

            print(user)
            print(type(user))
            order = Order(name=name, user=user, phone=phone, address=address, city=city,
                            state=state, zip_code=zip_code, amount=amount, discount=discount,order_id=order_id, plan_id=plan, order_completed=False,role='customer')
            order.save()

            # sending details to paytm gateway in form of dict
            detail_dict = {
                "MID": parameters['merchant_id'],
                "WEBSITE": "WEBSTAGING",
                "INDUSTRY_TYPE_ID": "Retail",
                "CUST_ID": str(email_id),
                "CHANNEL_ID": "WEB",
                "ORDER_ID": str(order_id),
                "TXN_AMOUNT": str(amount),
                "CALLBACK_URL": f'{parameters["BASE_URL"]}/api/req_handler',
            }

            param_dict = detail_dict
            CheckSum.generateSignature
            param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                detail_dict, parameters['merchant_key'])
            # print('.................', param_dict)
            return render(request, 'redirect.html', {'detail_dict': param_dict})

        return HttpResponse('Either amount or Discount not Matched')
    return render(request, 'checkout2.html', {'plan': plan})  # for checkout
    # except Exception as e:
    #     print("An Exception occur \n", e)
    #     return HttpResponse(e)


@csrf_exempt
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        form = request.POST
        print(form["ORDERID"])
        role = {
        'customer': 'customer',
        'vendor': 'vendor',
            }

        # another if to handle if user load refresh
        is_order_exist = Order_Payment.objects.filter(
            order_id=form["ORDERID"]).exists()
        print('............................order', is_order_exist)
        if is_order_exist == False:
            # FOR ALL VALUES
            for i in form.keys():
                response_dict[i] = form[i]
                print(i, form[i])

                if i == "CHECKSUMHASH":
                    response_check_sum = form[i]

            verify = CheckSum.verifySignature(
                response_dict, parameters['merchant_key'], response_check_sum)
            print(verify)
            # response_dict["STATUS"] = "PENDING"
            print('.........response_dict["STATUS"]', response_dict["STATUS"])
            print("..................", verify)
            if verify and response_dict["STATUS"] != "TXN_FAILURE" or response_dict["STATUS"] == "PENDING":
                order_payment = Order_Payment()
                usr = User
                # id = models.AutoField(primary_key = True)
                order = Order.objects.get(order_id=response_dict["ORDERID"])
               

                order_payment.order_summary = order
                # paytm responses
                order_payment.currency = response_dict["CURRENCY"]
                order_payment.gateway_name = response_dict["GATEWAYNAME"]
                # Txn Success
                order_payment.response_message = response_dict["RESPMSG"]
                # order_payment.bank_name = response_dict["BANKNAME"] # WALLET
                # PPI
                order_payment.Payment_mode = response_dict["PAYMENTMODE"]
                # MID = models.CharField(max_length=8) # VdMxPH61970223458566
                order_payment.response_code = response_dict["RESPCODE"]  # 01
                # 20200905111212800110168406201874634
                order_payment.txn_id = response_dict["TXNID"]
                # 2400.00
                order_payment.txn_amount = response_dict["TXNAMOUNT"]
                order_payment.order_id = response_dict["ORDERID"]  # 6556
                order_payment.status = response_dict["STATUS"]  # TXN_SUCCESS
                # 63209779
                order_payment.bank_txn_id = response_dict["BANKTXNID"]
                # 2020-09-05 18:51:59.0
                order_payment.txn_date = response_dict["TXNDATE"]
                # order_payment.refund_amount =  #  0.00
                order_payment.save()
                payment_status = Order_Payment.objects.get(
                    order_id=response_dict["ORDERID"])
                
                print('00.........',order.discount)
                if order.role == 'customer':
                    user = order_payment.order_summary.user
                    user.is_customer_paid =True 
                    user.customer_discount = order.discount
                    user.save()   
                    customer = Customer.objects.filter(user=user).first()
                    customer.subscription_plan_taken = order_payment.order_summary.plan_id
                    customer.save()
                else:
                    user = order_payment.order_summary.user
                    user.is_vendor_paid = True 
                    user.save()   
                    vendor = Vendor.objects.filter(user=user).first()
                    vendor.registration_fee = order_payment.order_summary.plan_id
                    vendor.save()
                print('Order payment..............................',order_payment.order_summary.user)
                print('Order payment..............................',type(order_payment))
              
                return render(request, 'ordersucess.html', {'payment': payment_status})
            else:
                Order.objects.filter(
                    order_id=response_dict["ORDERID"]).delete()
                return HttpResponse('Order is not Placed Because of some error. Please <a href="/sbt/">Try Again </a>')
        else:
            payment_status = Order_Payment.objects.get(
                order_id=form["ORDERID"])
            # Session should create when order is get successfull

            return HttpResponse('Your payment  failed')
    return HttpResponse('Invalid Request')


def pricing_multiplier(request):
    if request.method == "POST":

        amount = int(request.POST.get('amount'))
        try:
            discount = int(request.POST.get('discount'))
        except ValueError:
            return JsonResponse({'discount_applied': '', 'total': '', 'error': 'Expected integer'})
        plan_id = int(request.POST.get('plan_id'))
        response = discount_validation(plan_id, discount, amount)
        # response_dict = json.loads(response.getvalue().decode('utf-8'))
        # print(response_dict)
        return JsonResponse(response)


def order_status(request, slug):
    try:
        obj = Order_Payment.objects.get(order_id=slug)
        obj2 = obj.order_summary
        if obj2.user == request.user:
            paytmParams = dict()

            paytmParams["MID"] = parameters['merchant_id']
            paytmParams["ORDERID"] = slug

            checksum = CheckSum.generateSignature(paytmParams, parameters['merchant_key'])

            paytmParams["CHECKSUMHASH"] = checksum

            post_data = json.dumps(paytmParams)

            # for Staging
            url = "https://securegw-stage.paytm.in/order/status"

            # for Production
            # url = "https://securegw.paytm.in/order/status"

            response = requests.post(url, data=post_data, headers={
                                     "Content-type": "application/json"}).json()
            print(response)

            if response["STATUS"] == "TXN_SUCCESS":
                print("Updating Status")
                obj = Order_Payment.objects.get(order_id=slug)
                obj.status = response["STATUS"]
                obj.response_code = response["RESPCODE"]
                obj.response_message = response["RESPMSG"]
                obj.txn_date = response["TXNDATE"]
                obj.bank_name = response["BANKNAME"]
                obj.save()
                return HttpResponse("order success fully placed")

            return HttpResponse("order is still in pending state")

        elif request.user != None and request.user.is_authenticated:
            return HttpResponse("Please insert correct orderid")
        else:
            return HttpResponse('Please Login <a href="/sbt/login"> Here First</a>')
    except Exception as e:
        return HttpResponse(f"Requested Order Not Found - {e}")  # form to type in order id"""




def log_in(request):
    if request.method == 'POST':
        phno = request.POST.get('phonenumber')
        base_url = parameters["BASE_URL"]

        url = f'{base_url}/auth/send_sms_code/{phno}'
        response = requests.get(url)
        return render(request, 'website/auth_and_pass/type-otp.html', {'phone': phno})

    return render(request, 'website/auth_and_pass/login-otp.html')

def verify(request):
    if request.method == "POST":
        print('..........post')
        phno = request.POST.get('phonenumber')
        otp = request.POST.get('otp')
        base_url = parameters["BASE_URL"]

        url = f'{base_url}/auth/verify/{otp}/{phno}'
        response = requests.get(url)
        if response.status_code == 408 or response.status_code == 404: # 408 - Request Time Out
            messages.error(request, 'Login Failed')
            return redirect('website:verify')

        user = authenticate(request, phone=phno)
        if user is not None:
            login(request, user)
        messages.success(request, 'Login Successfull')
        return redirect('website:Sbthome')



def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out!')
    return redirect('website:Sbthome')

"""
def username_validator(request):
    if request.method == 'POST':
        usr = request.POST.get('user_name')
        data = {
            'is_taken': User.objects.filter(username__iexact=usr).exists()
        }
        if data['is_taken']:
            data['error_message'] = 'A user with this username already exists.'
        print(data)
    return JsonResponse(data)
"""

# A done here -------------------------------------



# For displaying Single TOP Info
def single_vendor(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    vendors = TOP.objects.filter(vendor_name=slug)
    return render(request, 'website/pages/team-single.html', {'vendors': vendors, 'category': category,'vendor':vendor})


def service_detail(request, slug):
    # for fetching services name from db
    services = Service.objects.filter(service_name=slug)
    category = Categories.objects.all()
    # fetch form data from html ,save it db and send email
    if request.method == 'POST':
        registrant_name = request.POST.get('contactName', '')
        registrant_mobile_no = request.POST.get('contactPhone', '')
        registrant_interest = request.POST.get('Interestlist', '')
        registrant_query = request.POST.get('contactMessage', '')
        if registrant_mobile_no:
            contact = ServiceContact(registrant_name=registrant_name, registrant_mobile_no=registrant_mobile_no,
                                     registrant_interest=registrant_interest, registrant_query=registrant_query)
            contact.save()
            send_mail(
                subject='New Customer registered for service',
                message=f"Customer Name = {registrant_name}\nMobile No. = {registrant_mobile_no}\nInterest Area = {registrant_interest}\nQuery message = {registrant_query}",
                from_email=parameters['from_email'],
                recipient_list=[parameters['to_email']],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Form submission successful. SBT Professional team Contact You within 24 hours')
            return redirect('website:Sbthome')
        else:
            messages.error(request, 'Form Not Submitted Try Again!!', {
                'services': services})
            return redirect(request, 'website/services-detail.html', {'services': services, 'category': category})

    return render(request, 'website/services-detail.html', {'services': services, 'category': category})


def search(request):
    category = Categories.objects.all()
    # try:
    query = request.GET['query']
    location = request.GET['location']
    print(location)
    if len(query) > 80 and len(location) > 20:
        vendor = Vendor.objects.none()
    else:
        or_lookup = (Q(city__icontains=location) & Q(Busniess_Type__category_name__icontains=query))
        vendors = Vendor.objects.filter(or_lookup)
        print(vendors)
    params = {'query': query, 'vendors': vendors, 'location': location,
                'category': category}
    return render(request, 'website/search/searchtest.html', params)






# function for define process of organisation
def process(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()

    return render(request, 'website/pages/process.html', {'vendor': vendor, 'category': category})


# for list all team of professionals
def top(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    team = TOP.objects.all()
    return render(request, 'website/pages/top2.html', {'vendor': vendor, 'team': team, 'category': category})



def search_top(request):
    category = Categories.objects.all()
    team = TOP.objects.all()
    vendor = TOP.objects.all()
    query = request.GET['query']
    if len(query) > 80:
        filtered_top_vendors = TOP.objects.none()
    else:
        or_lookup = (Q(vendor_name__icontains=query) | Q(Busniess_Type__category_name__icontains=query) | Q( vendor_work_desc__icontains=query))
        filtered_top_vendors = TOP.objects.filter(or_lookup)

        print(filtered_top_vendors)
    return render(request, 'website/search/search_top.html',
                  {'filtered_top_vendors': filtered_top_vendors, 'vendor': vendor, 'category': category,'query':query})


def trading(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        customer_name = request.POST.get('name', '')
        product_name = request.POST.get('product_name', '')
        address_from = request.POST.get('address_from', '')
        address_to = request.POST.get('address_to', '')
        mobile = request.POST.get('mobile', '')
        zip_code = request.POST.get('zip_code', '')
        customer = Trading(customer_name=customer_name, product_name=product_name, address_from=address_from,
                           address_to=address_to, mobile=mobile, zip_code=zip_code)
        customer.save()
        if product_name:
            send_mail(
                subject='New Customer registered for service',
                message=f"Customer Name = {customer_name}\nProduct Name = {product_name}\nAddress From = {address_from}\nAddress To = {address_to}\nMobile No. ={mobile}\nZip code = {zip_code}",
                from_email=parameters['from_email'],
                recipient_list=[parameters['to_email']],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Order successful.')
            return render(request, 'website/pages/trading-info.html', {'vendor': vendor, 'category': category})
        else:
            messages.error(request, 'Failed to Order Try Again!')
            return render(request, 'website/pages/trading-info.html', {'vendor': vendor, 'category': category})
    return render(request, 'website/pages/trading-info.html', {'vendor': vendor, 'category': category})


def faq(request):
    category = Categories.objects.all()
    faq_query = Faq.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        resp = form_validation(request.POST)
        if resp != None:
            messages.warning(request, resp)
            return redirect('website:faq')
        customer_name = request.POST.get('customer_name', '')
        mobile = request.POST.get('mobile', '')
        message = request.POST.get('message', '')
        query = QueryContact(customer_name=customer_name, mobile=mobile, message=message)
        query.save()
        if message:
            send_mail(
                subject='New Query from customer',
                message=f"Customer Name = {customer_name}\nMobile No. ={mobile}\nQueryMessage = {message}",
                from_email=parameters['from_email'],
                recipient_list=[parameters['to_email']],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Query Submittion successful.')
            return render(request, 'website/forms/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})
        else:
            messages.error(request, 'Failed to submit Try Again!')
            return render(request, 'website/forms/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})
    return render(request, 'website/forms/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})


def newsletter(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    return render(request, 'website/pages/coming-soon.html', {'vendor': vendor, 'category': category})


def tac(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    return render(request, 'website/pages/Terms_and_condition.html', {'vendor': vendor, 'category': category})


def feedback(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Email is not valid')
            return redirect('website:feedback')
        feed_back = request.POST['experience']
        Comments = request.POST.get('comments')
        customer_name = request.POST.get('name')

        if feed_back:
            customer_feedback = Feedback(feed_back=feed_back, Comments=Comments, customer_name=customer_name,
                                         email=email)
            customer_feedback.save()
            send_mail(
                subject='New feedback from customer',
                message=f"Customer Name = {customer_name}\nemail ={email}\nFeedback Message = {feed_back}",
                from_email=parameters['from_email'],
                recipient_list=[parameters['to_email']],
                fail_silently=False)
            messages.success(request, 'Form Submitted Successfully!')
            return HttpResponseRedirect('/sbt')
        else:
            messages.error(request, 'Form not submitted! TRY AGAIN')
            return render(request, 'website/forms/feedback.html', {'vendor': vendor, 'category': category})

    return render(request, 'website/forms/feedback.html', {'vendor': vendor, 'category': category})



def contact_via_service(request, slug):
    category = Categories.objects.all()
    flag = False
    if request.method == 'POST':
        resp = form_validation(request.POST)
        if resp != None:
            messages.warning(request,resp)
            return render(request, 'website/forms/form_category.html', {'slug': slug, 'category': category})
        try:
            s_category = Subcategory.objects.get(sub_category_name__exact=slug)
            ss_category = None
        except:
            flag = True

        if flag:
            ss_category = Sub_sub_category.objects.get(sub_sub_category_name__exact=slug)
            s_category = ss_category.sub_category_name
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        time = request.POST.get('time')
        obj = Contactviacategory(registrant_name=name, registrant_mobile_no=mobile, calling_time=time,
                                 service_name=s_category, sub_service_name=ss_category)
        obj.save()
        send_mail(
                subject='New Query from customer',
                message=f"Customer Name = {name}\nMobile No. ={mobile}\nservice = {str(s_category) + ' subcategory = '  + str(ss_category)}\n",
                from_email=parameters['from_email'],
                recipient_list=[parameters['to_email']],
                fail_silently=False)
        messages.success(request,
                         'Form submission successful. SBT Professional team Contact You On Your Chosen Time')
        return redirect('website:Sbthome')

    return render(request, 'website/forms/form_category.html', {'slug': slug, 'category': category})

# open Frenchise contact form
def frenchise(request):
    category = Categories.objects.all()
    if request.method == "POST":
        customer_name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('phone')
        address = request.POST.get('address')
        frenchise_option = request.POST['Interest']
        if frenchise_option:
            obj = FrenchiseContact(customer_name=customer_name, email=email, mobile_no=mobile_no, address=address,
                                   frenchise_option=frenchise_option)
            obj.save()
            send_mail(
                subject='New Frenchise customer',
                message=f"Customer Name = {customer_name}\nMobile No. ={mobile_no}\nAddress = {address}\nInterested in ={frenchise_option}",
                from_email=parameters['from_email'],
                recipient_list=[parameters['to_email']],
                fail_silently=False
            )
            messages.success(request,
                             'Form Submitted Successfully SBT Professionals Team Contacts You Within 24 hours!')
            return HttpResponseRedirect('/sbt/frenchise')
        else:
            messages.error(request, 'Form submittion Failed! TRY AGAIN')
            return render(request, 'website/forms/frenchise.html', {'category': category})

    return render(request, 'website/forms/frenchise.html', {'category': category})


def suggestions(request):
    if request.is_ajax():
        if 'term' in request.GET:
            obj = KeyWord.objects.filter(name__istartswith = request.GET.get('term'))

        keyword = list()
        for i in obj:
            print(i.name)
            keyword.append(i.name)
        return JsonResponse(keyword, safe=False)

def query(request):

    """
        How Search Works :
            Initially it takes the location using Mozilla Navigator and Geocode it to Coordinates.
            After that the Coordinates is added with km to search on range (To add km we define haver_sine_formula() function)
            Which take current latitutde and longitude as first two arguments respectively and km range as 3rd argumnet.

            * Infinity Scroll : 
                It uses paginator provided by django and with that simple js code with some imports all things are set to go.
                
                // Those impors are  -Waypoint CDN
                // - Infinite
                var infinite = new Waypoint.Infinite({
                    element: $('.infinite-container')[0],
                    onBeforePageLoad: function () {
                        $('.loading').show();
                    },
                    onAfterPageLoad: function ($items) {
                        $('.loading').hide();
                    }
                });

                the loader will laod the data inside the class="infinite-item" 
            !!THERE IS WORK NEEDED 
    """
    pagination = 10
    locator = Nominatim(user_agent='myGeocoder')
    loc = locator.geocode(request.POST.get('location'))
    
    # Also we can put a infinity loader which fetch more vendor by quering this and increasing this range value !Man Awesome.
    # This also increase optimizations
    # TODO
        # Need to add Relevancy of search which enable smart search
        # It work on two params i.e. keyword and coordinates.
        # We need the one which match with keyword as well as  location in range
        # Need to add GIF for reloading
    range = 10
    lat_p, lng_p = haver_sine_formula(loc.latitude, loc.longitude, range)
    lat_n, lng_n = haver_sine_formula(loc.latitude, loc.longitude, -range)
    print(loc.latitude)
    print(lat_p)
    print('loc.lng',loc.longitude)
    print('lng_p',lng_p)

    # lte -> less then equal
    # gte -> greater then equal

    vendor_in_pos_range2 = Vendor.objects.filter(Latitude__gte = loc.latitude, Latitude__lte = lat_p).\
        filter(Longitude__gte = loc.longitude, Longitude__lte = lng_p).\
            filter(keywords__name = request.POST.get('search'))

    all_vendor = Vendor.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_vendor, 10)
    try:
        vendor = paginator.page(page)
    except PageNotAnInteger:
        vendor = paginator.page(1)
    except EmptyPage:
        vendor = paginator.page(paginator.num_pages)

    return render(request, 'website/search/searchtest.html', {'vendors': vendor, 'query':query, 'location': location} )




def location(request):
    locator = Nominatim(user_agent='myGeocoder')
    loc = locator.reverse(f"{request.GET.get('lat')},{request.GET.get('lng')}")
    # >>> l = obj.reverse('57 29.687624800000002 76.9988556')
    # >>> l
    # Location(Sector 13, Model Town, Karnal, Haryana, 132001, India, (29.68744057560696, 76.99884150262069, 0.0))
    # >>> type(l)
    # <class 'geopy.location.Location'>
    # >>> l[0] 
    # 'Sector 13, Model Town, Karnal, Haryana, 132001, India'
    # >>> l[1] 
    # (29.68744057560696, 76.99884150262069)
    # >>> l[0] 
    # 'Sector 13, Model Town, Karnal, Haryana, 132001, India'
    print('loc[0]')
    return JsonResponse({'reverse_geoenc':loc[0]})

def search(request):
    category = Categories.objects.all()
    # try:
    query = request.GET['query']
    location = request.GET['location']
    print(location)
    if len(query) > 80 and len(location) > 20:
        vendor = Vendor.objects.none()
    else:
        or_lookup = (Q(city__icontains=location) & Q(Busniess_Type__category_name__icontains=query))
        vendors = Vendor.objects.filter(or_lookup)
        print(vendors)
    params = {'query': query, 'vendors': vendors, 'location': location,
                'category': category}
    return render(request, 'website/search/searchtest.html', params)

# Dummy Data add function
def create(request):
    obj = DummyData()
    obj.create(80)
    return HttpResponse('operation completed succesfully')

def format(request):
    obj = DummyData()
    obj.format()
    return HttpResponse('Data Deleted Successfully')

def test(request):
    locator = Nominatim(user_agent='myGeocoder')
    address = 'Sector 4, Model Town, Karnal, Haryana, 132001, India'
    coords = locator.geocode(address)
    lat_list_pos = []
    lng_list_pos = []
    lat_list_neg = []
    lng_list_neg = []

    lat = coords.latitude
    lng = coords.longitude

    for i in range(0, 40):
        lat2, lng2 = haver_sine_formula(lat, lng, i)
        lat_list_pos.append(lat2)
        lng_list_pos.append(lng2)

    for i in range(40, 0, -1):
        lat2, lng2 = haver_sine_formula(lat, lng, i)
        lat_list_neg.append(lat2)
        lng_list_neg.append(lng2)

    print(f'{lat2}, {lng2}')
    
    # queryset = Location.objects.filter(current_lat__gte=lat1, current_lat__lte=lat2)\
    #     .filter(current_long__gte=long1, current_long__lte=long2)

    return HttpResponse(f'{lat_list_pos} <br> {lat_list_neg} <br> {lng_list_pos} <br> {lng_list_neg}')

def vendor_review(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        
    return render(request, 'website/vendor_review_test.html')
    


#error handling view
def error_404_view(request,exception):
    return render(request,'website/error404.html')
