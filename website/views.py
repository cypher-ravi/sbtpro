from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import FreeListing, Plans, Order, Service, Job, Upload_resume, Categories
# FOR PAYTM---------------------
from .PayTm import CheckSum
from django.views.decorators.csrf import csrf_exempt
# FOR PAYTM End---------------------

from django.contrib import messages
import random
from django.core.files.storage import FileSystemStorage
# To import for login sign up stuff--------
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse

# to test login logout sessions include html files i attached
# LIKE templates/AP/<files you have.html>
# Create your views here.
# ! NEVER SHOW MERCHANT ID AND KEY !
MID = "VdMxPH61970223458566"  # MERCHANT ID
MKEY = "1xw4WBSD%bD@ODkL"  # MERCHANT KEY


def index(request):
    services = Service.objects.all()

    category = Categories.objects.all()

    plans = Plans.objects.all()
    print(plans)
    return render(request, 'website/index.html', {'plans': plans, 'category': category}, {'services': services})


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
        resume = Job(name=name, mobile=mobile, education=education, experience=experience)
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
                order_id = random.randint(1, 9999)  # you can use any random id (must be unique!)
                email_id = request.POST.get('email', '')
                name = request.POST.get('name', '')
                phone = request.POST.get('phone', '')
                address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
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
                param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(detail_dict, MKEY)
                print('.................', param_dict)
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
        verify = CheckSum.verifySignature(response_dict, MKEY, response_check_sum)
        print(verify)
        print("..................", verify)
        if verify:
            return HttpResponse("payment successfull")
    return HttpResponse("Not successfull")


# --------------------------payment end ------------------------

@csrf_exempt
# user login logout and checks
def sign_up(request):
    # have exception of geting same user name
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('create_password')
        print(username, password)
        usr = User.objects.create_user(username=username, password=password)
        usr.save()
        return redirect(log_in)
    else:
        return render(request, 'website/register.html')


# @csrf_exempt
def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # checks if user is there in db
        print(user)
        if user is not None:  # if he is in db than create a seesion using login function
            login(request, user)
            messages.success(request,'Login successful')
            return redirect(index)
        else:
            messages.error(request,'Enter valid credentials')
            return render(request, 'website/login.html')
    return redirect(index)

# return redirect(index)


def logout_view(request):
    logout(request)
    # messages.success("loged out successfully")
    return redirect(index)


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
