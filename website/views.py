from Customer.models import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
from django.core.mail import EmailMessage
from .DummyData import DummyData

# To import for login,Signup
"""
from django.contrib.auth.models import User
"""

import json
import math
import random
import re
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
MID = "bPYtDh39113697597251"  # MERCHANT ID
MKEY = "YX24Rc1vgjPCPs5@"  # MERCHANT KEY

fn = pathlib.Path(__file__).parent.parent / 'config.json'
with open(fn,"r") as params:
    parameters = json.load(params)

# def vendor_profile(request):
#     return render(request, 'template_name.html')
def menu_top(request):
    tops = TOP.objects.all()
    return {'TOPS': tops}

def vendor_profile(request):
    return render(request, 'website/vendor-profile.html')

def index(request):
    category = Categories.objects.all()
    # Logic for services
    services = Service.objects.all()

    # testimonials
    testimonials = AddTestimonial.objects.all()

    plans = Plan.objects.all()
    return render(request, 'website/index.html',
                  {'plans': plans, 'category': category, 'services': services,'testimonials':testimonials})

# Function to take input from form and send it through email
def freelisting(request):
    category = Categories.objects.all()
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
    return render(request, 'website/forms/freelisting.html', {'category': category})


def customer_membership(request):
    category = Categories.objects.all()
    redirect1 = '/sbt/purchase'

    plans = Plan.objects.all()

    return render(request, 'website/pages/membership.html', {'plans': plans, 'category': category,'redirect':redirect1})


def jobs(request):
    category = Categories.objects.all()
    if request.method == "POST":
        name = request.POST.get('contactName', '')
        mobile = request.POST.get('contactmobile', '')
        education = request.POST.get('contactEducation', '')
        experience = request.POST.get('contactexperience', '')
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
        return render(request, 'website/forms/job_form.html', {'category': category})

    return render(request, 'website/forms/job_form.html', {'category': category})


def upload_resume(request):
    category = Categories.objects.all()
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
                
                msg = EmailMessage('New job Seeker on your website', 'name =' + name, parameters['from_email'],
                                    [parameters['to_email']])
                msg.attach_file(file)
                msg.send()
            except:
                messages.error(request,'Failed to uplaod Resume! Try Again.')
                return redirect('website:Sbthome')
        else:
            messages.error(request, 'Before submit Resume Please Enter your name')

    return render(request, 'website/forms/job_form.html', {'category': category})

def download(request):
    category = Categories.objects.all()
    if request.method == 'POST':
        number = request.POST.get('number')
        if number.isnumeric():
            send_sms_message(number)
            messages.success(request,'Link sent successfully check your inbox!')
            return redirect('website:Sbthome')
        else:
            messages.warning(request,'Enter a number!')
            return render(request, 'website/pages/downloadapp.html', {'category': category})
    return render(request, 'website/pages/downloadapp.html', {'category': category})


def categories(request, slug):
    category = Categories.objects.all()
    filtered_categories = Categories.objects.filter(category_name=slug)
    related_sub_category = Subcategory.objects.all().filter(category_name__in=filtered_categories)
    return render(request, 'website/pages/category.html',
                  {'filtered_categories': filtered_categories, 'sub_category': related_sub_category,
                   'category': category})


def sub_to_sub_category(request, slug):
    category = Categories.objects.all()
    related_sub_category = Subcategory.objects.all().filter(sub_category_name=slug)
    related_sub_sub_category = Sub_sub_category.objects.all().filter(sub_category_name__in=related_sub_category)
    params = {'slug': slug}
    if related_sub_sub_category.exists():
        return render(request, 'website/pages/subcategory.html',
                      {'sub_category': related_sub_category, 'related_sub_sub_category': related_sub_sub_category,
                       'category': category})
    else:
        return render(request, 'website/forms/contact_via_category.html', {'slug': slug, 'category': category})



def test(request):
    if request.method =="POST":
        resp = form_validation(request.POST)
        return HttpResponse(f"nahi chala{resp}")

    return render(request, 'website/auth_and_pass/test.html')

@login_required(login_url="website:login")
def purchase_vendor(request, slug):
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
    return render(request, 'website/forms/purchase_form_customer.html', {'plan_review': dict_for_review, 'category': category})


@login_required(login_url="website:login")
def purchase_customer(request, slug):# plan_id, user, amount,discount,role):
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
    return render(request, 'website/forms/purchase_form_customer.html', {'plan': plan, 'plan_review': dict_for_review, 'category': category})

def customer_card_purchase(request, plan_id):

    if request.method == 'POST':

        if request.user.is_authenticated:
            is_vendor = request.POST.get('is_vendor')
            discount = request.POST.get('discount')
            try:
                plan = Plan.objects.get(plan_id=plan_id)
            except:
                return HttpResponse('Please enter a valid Plan Id')

            customer = Customer()
            customer.user = request.user
            customer.customer_name = request.POST.get('name')
            customer.last_name = request.POST.get('l_name')
            customer.Address = request.POST.get('address')
            customer.city = request.POST.get('city')
            customer.state = request.POST.get('state')
            customer.zipcode = request.POST.get('zip_code')
            customer.EmailID = request.POST.get('email')
            customer.joining_date = timezone.datetime.now()
            customer.gender = request.POST.get('gender')
            customer.extra_Info = request.POST.get('extra_info')
            customer.Contact_Person = None
            customer.customer_is_active = True
            customer.subscription_plan_taken = plan

            customer.save()
            user = User.objects.filter(id=request.user.id).first()
            phone = user.phone
            
            try:
                discount = int(request.POST.get('discount'))
            except ValueError:
                return HttpResponse('Please select a valid discount value')

            user_amount= plan.plan_amount
            if discount != "" and discount != None:
                response_dict = discount_validation(plan_id, discount, user_amount, is_vendor)
                if response_dict['error'] != None:
                    return HttpResponse(response_dict['error'])
                amount = discount * plan.plan_amount
            else:
                amount = plan.plan_amount

            order_id = random.randint(1, 999999)
            email_id = request.POST.get('email')
            name = request.POST.get('name')
            address =request.POST.get('address')
            state =  request.POST.get('state')
            city = request.POST.get('city')
            zip_code = request.POST.get('zip_code')
            plan_id = plan.plan_id

            # Check if user not provide any discount value
            order = Order(name=name, email_id=email_id, user=user, phone=phone, address=address, city=city,
                            state=state, zip_code=zip_code, amount=amount, discount=discount,order_id=order_id, plan_id=plan, order_completed=False,role='customer')
            order.save()

            # sending details to paytm gateway in form of dict
            detail_dict = {
                "MID": parameters['merchant_id'],
                "WEBSITE": "DEFAULT",
                "INDUSTRY_TYPE_ID": "Retail",
                "CUST_ID": str(email_id),
                "CHANNEL_ID": "WEB",
                "ORDER_ID": str(order_id),
                "TXN_AMOUNT": str(amount),
                "CALLBACK_URL": f'{parameters["BASE_URL"]}/sbt/req_handler',
            }

            param_dict = detail_dict
            CheckSum.generateSignature
            param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                detail_dict, parameters['merchant_key'])
            return render(request, 'redirect.html', {'detail_dict': param_dict})
        return HttpResponse('Invalid Request')
    return render(request, 'checkout2.html', {'plan': plan})  


@csrf_exempt
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        form = request.POST
        role = {
        'customer' : 'customer',
        'vendor' : 'vendor',
        }

        is_order_exist = Order_Payment.objects.filter(order_id=form["ORDERID"]).exists()
        if is_order_exist == False:
            for i in form.keys():
                response_dict[i] = form[i]
                if i == "CHECKSUMHASH":
                    response_check_sum = form[i]

            verify = CheckSum.verifySignature(response_dict, parameters['merchant_key'], response_check_sum)
          
            if(verify and response_dict["STATUS"] != "TXN_FAILURE") or (verify and response_dict["STATUS"] == "PENDING"):
                order_payment = Order_Payment()
                usr = User
                try:
                    order = Order.objects.get(order_id=response_dict["ORDERID"])
                except:
                    return HttpResponse('Order Not Found')
                order_payment.order_summary = order
                order_payment.currency = response_dict["CURRENCY"]
                order_payment.gateway_name = response_dict["GATEWAYNAME"]
                order_payment.response_message = response_dict["RESPMSG"]
                order_payment.Payment_mode = response_dict["PAYMENTMODE"]
                order_payment.response_code = response_dict["RESPCODE"]  # 01
                order_payment.txn_id = response_dict["TXNID"]
                order_payment.txn_amount = response_dict["TXNAMOUNT"]
                order_payment.order_id = response_dict["ORDERID"]  # 6556
                order_payment.status = response_dict["STATUS"]  # TXN_SUCCESS
                order_payment.bank_txn_id = response_dict["BANKTXNID"]
                order_payment.txn_date = response_dict["TXNDATE"]
                order_payment.bank_name = response_dict["BANKNAME"]
                order_payment.save()
                payment_status = Order_Payment.objects.get(
                    order_id=response_dict["ORDERID"])

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
                return render(request, 'ordersucess.html', {'payment': payment_status})
            else:
                failed_payment = FailedPayment() 
                failed_payment.txn_date = response_dict["TXNDATE"]
                failed_payment.response_message = response_dict["RESPMSG"]
                failed_payment.response_code = response_dict["RESPCODE"]
                failed_payment.bank_txn_id = response_dict["BANKTXNID"]
                failed_payment.txn_id = response_dict["TXNID"]
                failed_payment.txn_amount = response_dict["TXNAMOUNT"]
                failed_payment.order_id = response_dict["ORDERID"] 
                failed_payment.status = response_dict["STATUS"]
                failed_payment.Payment_mode = response_dict["PAYMENTMODE"]
                failed_payment.gateway_name = response_dict["GATEWAYNAME"]
                failed_payment.currency = response_dict["CURRENCY"]
                failed_payment.save()

#                 Order.objects.filter(
#                     order_id=response_dict["ORDERID"]).delete()
                return HttpResponse('Order is not Placed Because of some error. Please <a href="/sbt/">Try Again </a>')
        else:
            payment_status = Order_Payment.objects.get(
                order_id=form["ORDERID"])
            # Session should create when order is get successfull
            return HttpResponse('Order Alerady Placed')

    return HttpResponse('Invalid Request')


def pricing_multiplier(request):
    if request.method == "POST":
        is_vendor = request.POST.get('is_vendor')
        amount = int(request.POST.get('amount'))
        try:
            discount = int(request.POST.get('discount'))
        except ValueError:
            return JsonResponse({'discount_applied': '', 'total': '', 'error': 'Expected integer'})
        plan_id = int(request.POST.get('plan_id'))
        response = discount_validation(plan_id, discount, amount, is_vendor)
        # response_dict = json.loads(response.getvalue().decode('utf-8'))
        # print(response_dict)
        return JsonResponse(response)

# Best for Pending
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
#             url = "https://securegw-stage.paytm.in/order/status"

            # for Production
            url = "https://securegw.paytm.in/order/status"

            response = requests.post(url, data=post_data, headers={
                                     "Content-type": "application/json"}).json()

            if response["STATUS"] == "TXN_SUCCESS":
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
    except Exception:
        return HttpResponse(f"Requested Order Not Found")  # form to type in order id"""



def log_in(request):
    if request.method == 'POST':
        phno = request.POST.get('phonenumber')
        base_url = parameters["BASE_URL"]
        url = f'{base_url}/auth/{phno}'
        requests.get(url)
        return render(request, 'website/auth_and_pass/type-otp.html', {'phone': phno})

    return render(request, 'website/auth_and_pass/login-otp.html')

def verify(request):
    if request.method == "POST":
        phno = request.POST.get('phonenumber')
        otp = request.POST.get('otp')
        base_url = parameters["BASE_URL"]

        url = f'{base_url}/auth/{phno}/'
        data = {
            'otp':otp,
            'phone':phno
        }
        response = requests.post(url,data=data)
        # if response.status_code == 408 or response.status_code == 404: # 408 - Request Time Out
        #     messages.error(request, 'Login Failed')
        #     return redirect('website:verify')
        print(response.json())
        if response.json()['verified'] == True:
            user = User.objects.get(phone__iexact=phno)
            if user != None:
                login(request, user)
                messages.success(request, 'Login Successfull')
                return redirect('website:Sbthome')

        messages.success(request, 'Wrong OTP')
        return redirect('website:login')
       
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

def top_vendor_details(request, slug):
    category = Categories.objects.all()
    top = TOP.objects.filter(vendor_name=slug)
    return render(request, 'website/pages/top-detail.html', {'top': top, 'category': category})


# For displaying Single TOP Info
def single_vendor(request, slug):
    category = Categories.objects.all()
    vendors_detail =  Vendor.objects.filter(Company_Name=slug)
    vendors = TOP.objects.filter(vendor_name=slug)
    return render(request, 'website/pages/team-single.html', {'vendors': vendors_detail, 'category': category})


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
            return redirect(request, 'website/pages/services-detail.html', {'services': services, 'category': category})

    return render(request, 'website/pages/services-detail.html', {'services': services, 'category': category})


def search(request):
    category = Categories.objects.all()
    # try:
    query = request.GET['query']
    location = request.GET['location']
    if len(query) > 80 and len(location) > 20:
        vendors = Vendor.objects.none()
    else:
        or_lookup = (Q(city__icontains=location) & Q(Busniess_Type__category_name__icontains=query))
        vendors = Vendor.objects.filter(or_lookup)
    params = {'query': query, 'vendors': vendors, 'location': location,
                'category': category}
    return render(request, 'website/search/searchtest.html', params)






# function for define process of organisation
def process(request):
    category = Categories.objects.all()

    return render(request, 'website/pages/process.html', {'category': category})


# for list all team of professionals
def top(request):
    category = Categories.objects.all()
    team = TOP.objects.all()
    return render(request, 'website/pages/top2.html', {'team': team, 'category': category})



def search_top(request):
    category = Categories.objects.all()
    team = TOP.objects.all()
    query = request.GET['query']
    if len(query) > 80:
        filtered_top_vendors = TOP.objects.none()
    else:
        or_lookup = (Q(vendor_name__icontains=query) | Q(Busniess_Type__category_name__icontains=query) | Q( vendor_work_desc__icontains=query))
        filtered_top_vendors = TOP.objects.filter(or_lookup)
    return render(request, 'website/search/search_top.html',
                  {'filtered_top_vendors': filtered_top_vendors, 'category': category,'query':query})


def trading(request):
    category = Categories.objects.all()
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
            return render(request, 'website/pages/trading-info.html', {'category': category})
        else:
            messages.error(request, 'Failed to Order Try Again!')
            return render(request, 'website/pages/trading-info.html', {'category': category})
    return render(request, 'website/pages/trading-info.html', {'category': category})


def faq(request):
    category = Categories.objects.all()
    faq_query = Faq.objects.all()
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
            return render(request, 'website/forms/faq.html', {'faqs': faq_query,'category': category})
        else:
            messages.error(request, 'Failed to submit Try Again!')
            return render(request, 'website/forms/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})
    return render(request, 'website/forms/faq.html', {'faqs': faq_query,'category': category})


def newsletter(request):
    category = Categories.objects.all()
    return render(request, 'website/pages/coming-soon.html', {'category': category})


def tac(request):
    category = Categories.objects.all()
    return render(request, 'website/pages/Terms_and_condition.html', {'category': category})


def feedback(request):
    category = Categories.objects.all()
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

    return render(request, 'website/forms/feedback.html', {'category': category})



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
            obj = FrenchiseContact(name=customer_name, email=email, mobile_no=mobile_no, address=address,
                                   franchise_option=frenchise_option)
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
    try:

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
        # lte -> less then equal
        # gte -> greater then equal

        vendor_in_pos_range2 = Vendor.objects.filter(Latitude__gte = loc.latitude, Latitude__lte = lat_p).\
            filter(Longitude__gte = loc.longitude, Longitude__lte = lng_p).\
                filter(keywords__name = request.POST.get('search'))

        all_vendor = Vendor.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(vendor_in_pos_range2, 10)
        try:
            vendor = paginator.page(page)
        except PageNotAnInteger:
            vendor = paginator.page(1)
        except EmptyPage:
            vendor = paginator.page(paginator.num_pages)

        return render(request, 'website/search/searchtest.html', {'vendors': vendor, 'query':query, 'location': location} )
    except:
        return HttpResponse('some error occured')



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
    return JsonResponse({'reverse_geoenc':loc[0]})

def search(request):
    category = Categories.objects.all()
    # try:
    query = request.GET['query']
    location = request.GET['location']
    if len(query) > 80 and len(location) > 20:
        vendors = Vendor.objects.none()
    else:
        or_lookup = (Q(city__icontains=location) & Q(Busniess_Type__category_name__icontains=query))
        vendors = Vendor.objects.filter(or_lookup)
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


    # queryset = Location.objects.filter(current_lat__gte=lat1, current_lat__lte=lat2)\
    #     .filter(current_long__gte=long1, current_long__lte=long2)

    return HttpResponse(f'{lat_list_pos} <br> {lat_list_neg} <br> {lng_list_pos} <br> {lng_list_neg}')

def vendor_review(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')

    return render(request, 'website/vendor_review_test.html')


def refund_policy(request):
    return render(request, 'website/pages/refund-policy.html')

def privacy_policy(request):
    return render(request, 'website/pages/privacy-policy.html')

#error handling view
def error_404_view(request,exception):
    return render(request,'website/error404.html')
