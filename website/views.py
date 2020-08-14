from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import FreeListing, Plans, Order, Service, Job, Upload_resume, Categories, TOP, ServiceContact,Vendors
# FOR PAYTM---------------------
from .PayTm import CheckSum
from django.views.decorators.csrf import csrf_exempt
# FOR PAYTM End---------------------

from django.contrib import messages
import random
from django.core.files.storage import FileSystemStorage
# To import for login,Signup
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from math import ceil

# Create your views here.
# ! NEVER SHOW MERCHANT ID AND KEY !
MID = "VdMxPH61970223458566"  # MERCHANT ID
MKEY = "1xw4WBSD%bD@ODkL"  # MERCHANT KEY


def index(request):

    category = Categories.objects.all()
    # Logic for services
    services = Service.objects.all()

    # Another section started
    vendor = TOP.objects.all()

    plans = Plans.objects.all()
    return render(request, 'website/index.html', {'plans': plans, 'category': category, 'services': services, 'vendor': vendor})


# Function to take input from form and send it through email
def freelisting(request):
    if request.method == 'POST':
        Company_name = request.POST.get('companyname', '')
        location = request.POST.get('location', '')
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        # send mail function from django.core.mail import send mail
        send_mail(
            subject='New Vendor registered',
            message=f"Company Name = {Company_name}\nName = {first_name + ' ' + last_name}\nMobile No. = {mobile}\nAddress = {city + ',' + state + ',' + zip_code}",
            from_email='rk7305758@gmail.com',
            recipient_list=['ronniloreo@gmail.com'],
            fail_silently=False
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
        )
        # checks on values of form and using django.contrib import message for alert messages
        if len(Company_name) < 5 or len(first_name) < 2 or len(last_name) < 2 or len(mobile) < 10:
            messages.error(request, 'Please fill the form correctly!')
        else:
            listing = FreeListing(Company_name=Company_name, location=location, first_name=first_name,
                                  last_name=last_name, city=city, state=state, zip_code=zip_code, mobile=mobile,
                                  email=email)
            listing.save()
            messages.success(request, 'Form submission successful. SBT Professional team Contact You within 24'
                                      'hours.')
    return render(request, 'website/listing.html')


def top(request):
    return HttpResponse('hey buddy!')


def customer_membership(request):
    plans = Plans.objects.all()

    return render(request, 'website/membership.html', {'plans': plans})


def jobs(request):
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
        messages.success(request, 'Form submission successful. SBT Professional team Contact You within 24 '
                                  '24 hours.')
        send_mail(
            subject='New Job seeker created resume',
            message=f"Employee Name = {name}\nMobile No. = {mobile}\nExperience = {experience}\nEducation = {education}",
            from_email='rk7305758@gmail.com',
            recipient_list=['montisharma5401@gmail.com'],
            fail_silently=False
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
        )
        return render(request, 'website/form.html')

    return render(request, 'website/form.html')


def upload_resume(request):
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
                msg = EmailMessage('New job Seeker on your website', 'name =' + name, 'rk7305758@gmail.com',
                                   ['ronniloreo@gmail.com'])
                msg.attach_file(file)
                msg.send()
            except Exception as e:
                print(e)
        else:
            messages.error(request, 'Before submit resume Enter your name')

    return render(request, 'website/form.html')


def shop(request):
    return HttpResponse('hey buddy!')


def download(request):
    return render(request, 'website/downloadapp.html')


# for handle resume files
def handle_uploaded_file(f):
    with open('website/static/upload/' + f.name, 'rb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            return f.name


def categories(request, slug):
    category = Categories.objects.filter(category_name=slug)
    return render(request, 'website/category.html', {'categories': category})


# A's here  ------------------

def purchase(request, slug):
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                plan = Plans.objects.get(plan_name=slug)
                # you can use any random id (must be unique!)
                order_id = random.randint(1, 9999)
                email_id = request.POST.get('email', '')
                name = request.POST.get('name', '')
                phone = request.POST.get('phone', '')
                address = request.POST.get(
                    'address1', '') + " " + request.POST.get('address2', '')
                state = request.POST.get('state', '')
                city = request.POST.get('city', '')
                zip_code = request.POST.get('zip_code', '')
                amount = plan.plan_amount
                plan_id = plan.plan_id
                order = Order(name=name, email_id=email_id, address=address, city=city, state=state, zip_code=zip_code,
                              phone=phone, amount=amount, order_id=order_id, plan_id=plan)
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
                    "CALLBACK_URL": "http://127.0.0.1:8000/sbtapp/req_handler",
                }

                param_dict = detail_dict
                CheckSum.generateSignature
                param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                    detail_dict, MKEY)
                # print('.................', param_dict)
                return render(request, 'website/redirect.html', {'detail_dict': param_dict})

            plan = Plans.objects.get(plan_name=slug)
            dict_for_review = {
                'name': plan.plan_name,
                'amount': plan.plan_amount,
                'description_1': plan.description_1,
                'description_2': plan.description_2,
                'description_3': plan.description_3,
                'description_4': plan.description_4,
            }

            return render(request, 'website/purchase_form.html', {'plan_review': dict_for_review})

        else:
            return render(request, 'website/login.html')

    except Exception as e:
        print("An Exception occur \n", e)
        return HttpResponse(e)


@csrf_exempt
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        dict(response_dict)
        print(type(response_dict))
        form = request.POST  # FOR ALL VALUES
        for i in form.keys():
            response_dict[i] = form[i]
            print(i, form[i])

            if i == "CHECKSUMHASH":
                response_check_sum = form[i]
        verify = CheckSum.verifySignature(
            response_dict, MKEY, response_check_sum)
        print(verify)
        print("..................", verify)
        if verify:
            return HttpResponse("payment successfull")
    return HttpResponse("Not successfull")


# --------------------------payment end ------------------------

# user login logout and checks
def sign_up(request):
    # have exception of geting same user name
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['create_password']
        confirm_password = request.POST['confirm_password']
        # checks for on inputs
        # username should under 10 character
        if len(username) > 15:
            messages.error(request, 'Username must be unique!!')
            return redirect(sign_up)
        # password and confirm password should be match
        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return redirect(sign_up)
        # username should contain numbers and letters
        if not username.isalnum():
            messages.error(
                request, 'Username should contain letters and numbers!!')
            return redirect(sign_up)

        # create the user
        newuser = User.objects.create_user(
            username=username, email=email, password=password)
        newuser.save()
        messages.success(
            request, "Your SBT Professionals account has been successfully created")
        return redirect(index)
    else:
        return render(request, 'website/register.html')


def log_in(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(request, username=loginusername,
                            password=loginpass)  # checks if user is exist

        if user is not None:  # if user exist than create a seesion using login function
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('Sbthome')
        else:
            messages.error(request, 'Invalid credentials,Please Try Again!')
            return redirect('Sbthome')
    return render(request, 'website/login.html')

# return redirect(index)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('Sbthome')


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

# A done here -------------------------------------

# For displaying Single TOP Info


def single_vendor(request, slug):
    vendor = TOP.objects.filter(vendor_name=slug)
    return render(request, 'website/team-single.html', {'vendors': vendor})


def service_detail(request, slug):
    # for fetching services name from db
    services = Service.objects.filter(service_name=slug)
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
                from_email='rk7305758@gmail.com',
                recipient_list=['ronniloreo@gmail.com'],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Form submission successful. SBT Professional team Contact You within 24 hours')
            return render(request, 'website/services-detail.html', {'services': services})
        else:
            messages.error(request, 'Form Not Submitted Try Again!!', {
                           'services': services})
            return redirect(request, 'website/services-detail.html', {'services': services})

    return render(request, 'website/services-detail.html', {'services': services})



def search(request):
    query = request.GET['query']
    location = request.GET['location']
    if len(query) > 80 and len(location) > 20:
        categories = Categories.objects.none()  
    else:
        categories_names = Categories.objects.filter(category_name__icontains=query)
       
        vendor_address_location1 = Vendors.objects.filter(Address1__icontains=location)
        vendor_address_location2 = Vendors.objects.filter(Address2__icontains=location)
        vendor_work_description = Vendors.objects.filter(Service_decsription__icontains=query)
        subcategories1 = Categories.objects.filter(sub_category_name1__icontains=query)
        subcategories2 = Categories.objects.filter(sub_category_name2__icontains=query)
        subcategories3 = Categories.objects.filter(sub_category_name3__icontains=query)
        subcategories4 = Categories.objects.filter(sub_category_name4__icontains=query)
        subcategories5 = Categories.objects.filter(sub_category_name5__icontains=query)
        subcategories6 = Categories.objects.filter(sub_category_name6__icontains=query)
        subcategories7 = Categories.objects.filter(sub_category_name7__icontains=query)
        subcategories8 = Categories.objects.filter(sub_category_name8__icontains=query)
        subcategories9 = Categories.objects.filter(sub_category_name9__icontains=query)
        subcategories10 = Categories.objects.filter(sub_category_name10__icontains=query)
        categories = categories_names.union(subcategories1,subcategories2,subcategories3,subcategories4,subcategories5,subcategories6,subcategories7,subcategories8,subcategories9,subcategories10)
        vendor_location = vendor_address_location1.union(vendor_address_location2,vendor_work_description)
        print(location)
    params =  {'categories':categories,'query':query,'vendor_location':vendor_location,'location':location}
    return render(request,'website/searchtest.html',params)