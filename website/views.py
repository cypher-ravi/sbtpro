from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .models import FreeListing, Plan, Order, Service, Job, Upload_resume, Categories, Sub_sub_category, TOP, \
    ServiceContact, Vendor, Subcategory, Trading, Faq, QueryContact, Feedback, Contactviacategory, FrenchiseContact,AddTestimonial
# FOR PAYTM---------------------
from .PayTm import CheckSum
from django.views.decorators.csrf import csrf_exempt
# FOR PAYTM End-------------------------------------

from django.contrib import messages
import random
from django.core.files.storage import FileSystemStorage
# To import for login,Signup
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# validations
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse


# Create your views here.
# ! NEVER SHOW MERCHANT ID AND KEY !
MID = "VdMxPH61970223458566"  # MERCHANT ID
MKEY = "1xw4WBSD%bD@ODkL"  # MERCHANT KEY


def index(request):
    category = Categories.objects.all()
    # Logic for services
    services = Service.objects.all()

    #testimonials
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
    return render(request, 'website/listing.html', {'vendor': vendor, 'category': category})


def customer_membership(request):
    category = Categories.objects.all()
    redirect1 = '/website/purchase'

    plans = Plan.objects.all()
    vendor = TOP.objects.all()

    return render(request, 'website/membership.html', {'plans': plans, 'vendor': vendor, 'category': category,'redirect':redirect1})


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
        return render(request, 'website/form.html', {'vendor': vendor, 'category': category})

    return render(request, 'website/form.html', {'vendor': vendor, 'category': category})


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
                    msg = EmailMessage('New job Seeker on your website', 'name =' + name, 'rk7305758@gmail.com',
                                       ['ronniloreo@gmail.com'])
                    msg.attach_file(file)
                    msg.send()
                except Exception as e:
                    print(e)
            else:
                messages.error(request, 'Before submit resume Enter your name')

        return render(request, 'website/form.html', {'category': category})
    except:
        return render(request, 'website/404.html')


def download(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    return render(request, 'website/downloadapp.html', {'vendor': vendor, 'category': category})


def categories(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    filtered_categories = Categories.objects.filter(category_name=slug)
    related_sub_category = Subcategory.objects.all().filter(category_name__in=filtered_categories)
    return render(request, 'website/category.html',
                  {'filtered_categories': filtered_categories, 'sub_category': related_sub_category,
                   'category': category,'vendor':vendor})


def sub_to_sub_category(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    related_sub_category = Subcategory.objects.all().filter(sub_category_name=slug)
    related_sub_sub_category = Sub_sub_category.objects.all().filter(sub_category_name__in=related_sub_category)
    params = {'slug': slug}
    if related_sub_sub_category.exists():
        return render(request, 'website/subcategory.html',
                      {'sub_category': related_sub_category, 'related_sub_sub_category': related_sub_sub_category,
                       'category': category,'vendor':vendor})
    else:
        return render(request, 'website/form_category.html', {'slug': slug, 'category': category,'vendor':vendor})


# A's here  ------------------

def purchase(request, slug):
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                plan = Plan.objects.get(plan_name=slug)
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

            plan = Plan.objects.get(plan_name=slug)
            dict_for_review = {
                'name': plan.plan_name,
                'amount': plan.plan_amount,
                'description_1': plan.description_1,
                'description_2': plan.description_2,
                'description_3': plan.description_3,
                'description_4': plan.description_4,
            }

            return render(request, 'website/purchase_form.html', {'plan_review': dict_for_review, 'category': category,'vendor':vendor})

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

def sign_up(request):
    # have exception of geting same user name
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['create_password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists Please Consider Login')
            return redirect(sign_up)

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists Please consider Login')
            return redirect(sign_up)

        # username validation stuff ----------------
        if len(username) > 15:
            messages.error(request, 'Username must be unique!!')
            return redirect(sign_up)

        if not username.isalnum():
            messages.error(
                request, 'Username should contain letters and numbers!!')
            return redirect(sign_up)

        # Email Validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Email is not valid')
            return redirect(sign_up)
        # Password valdation
        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return redirect(sign_up)
        # username should contain numbers and letters

        # create the user
        newuser = User.objects.create_user(username=username, email=email, password=password)
        if newuser.is_staff:
            print('yes')
        else:
            print('no')
        newuser.save()

        messages.success(request, "Your SBT Professionals account has been successfully created")
        return redirect(log_in)
    else:
        return render(request, 'website/register.html')


def log_in(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        if User.objects.filter(email=loginusername).exists():
            usr_by_email = User.objects.get(email=loginusername)
            loginusername = usr_by_email.username

        user = authenticate(request, username=loginusername,
                            password=loginpass)  # checks if user is exist
        if user is not None:  # if user exist than create a session using login function
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect(index)
        else:
            print('....................user->', user)
            messages.error(request, 'Invalid credentials,Please Try Again!')
            return redirect(log_in)
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
    vendor = TOP.objects.all()
    category = Categories.objects.all()
    vendors = TOP.objects.filter(vendor_name=slug)
    return render(request, 'website/team-single.html', {'vendors': vendors, 'category': category,'vendor':vendor})


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
                from_email='rk7305758@gmail.com',
                recipient_list=['ronniloreo@gmail.com'],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Form submission successful. SBT Professional team Contact You within 24 hours')
            return render(request, 'website/services-detail.html', {'services': services, 'category': category})
        else:
            messages.error(request, 'Form Not Submitted Try Again!!', {
                'services': services})
            return redirect(request, 'website/services-detail.html', {'services': services, 'category': category})

    return render(request, 'website/services-detail.html', {'services': services, 'category': category})


def search(request):
    category = Categories.objects.all()
    try:
        query = request.GET['query']
        location = request.GET['location']
        if len(query) > 80 and len(location) > 20:
            categories = Categories.objects.none()
        else:
            categories_names = Categories.objects.filter(category_name__icontains=query)
            vendor_address_location1 = Vendor.objects.filter(Address1__icontains=location)
            vendor_address_location2 = Vendor.objects.filter(Address2__icontains=location)
            vendor_work_description = Vendor.objects.filter(Service_decsription__icontains=query)

            vendor_location = vendor_address_location1.union(vendor_address_location2, vendor_work_description)
            categories = categories_names
            print(location)
            print(categories)

        params = {'categories': categories, 'query': query, 'vendor_location': vendor_location, 'location': location,
                  'category': category}
        return render(request, 'website/searchtest.html', params)
    except :
        return render(request, 'website/coming-soon.html', {'category': category})


# function for define process of organisation
def process(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()

    return render(request, 'website/process.html', {'vendor': vendor, 'category': category})


# for list all team of professionals
def top(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    team = TOP.objects.all()
    return render(request, 'website/top2.html', {'vendor': vendor, 'team': team, 'category': category})


def search_top(request):
    category = Categories.objects.all()
    team = TOP.objects.all()
    vendor = TOP.objects.all()
    query = request.GET['query']
    if len(query) > 80:
        filtered_top_vendors = TOP.objects.none()
    else:
        top_vendors = TOP.objects.filter(vendor_name__icontains=query)
        top_vendors_business_type = TOP.objects.filter(Busniess_Type__icontains=query)
        top_vendors_work = TOP.objects.filter(vendor_work_desc__icontains=query)
        filtered_top_vendors = top_vendors.union(top_vendors_business_type, top_vendors_work)
        print(filtered_top_vendors)
    return render(request, 'website/search_top.html',
                  {'filtered_top_vendors': filtered_top_vendors, 'vendor': vendor, 'category': category})


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
                from_email='rk7305758@gmail.com',
                recipient_list=['ronniloreo@gmail.com'],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Order successful.')
            return render(request, 'website/trading-info.html', {'vendor': vendor, 'category': category})
        else:
            messages.error(request, 'Failed to Order Try Again!')
            return render(request, 'website/trading-info.html', {'vendor': vendor, 'category': category})
    return render(request, 'website/trading-info.html', {'vendor': vendor, 'category': category})


def faq(request):
    category = Categories.objects.all()
    faq_query = Faq.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '')
        mobile = request.POST.get('mobile', '')
        message = request.POST.get('message', '')
        query = QueryContact(customer_name=customer_name, mobile=mobile, message=message)
        query.save()
        if message:
            send_mail(
                subject='New Query from customer',
                message=f"Customer Name = {customer_name}\nMobile No. ={mobile}\nQueryMessage = {message}",
                from_email='rk7305758@gmail.com',
                recipient_list=['ronniloreo@gmail.com'],
                fail_silently=False)
            # contact@sbtprofessionals.com
            # teamofprofessionals2015@gmail.com
            messages.success(request,
                             'Query Submittion successful.')
            return render(request, 'website/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})
        else:
            messages.error(request, 'Failed to submit Try Again!')
            return render(request, 'website/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})
    return render(request, 'website/faq.html', {'faqs': faq_query, 'vendor': vendor, 'category': category})


def newsletter(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    return render(request, 'website/coming-soon.html', {'vendor': vendor, 'category': category})


def tac(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    return render(request, 'website/Terms_and_condition.html', {'vendor': vendor, 'category': category})


def feedback(request):
    category = Categories.objects.all()
    vendor = TOP.objects.all()
    if request.method == 'POST':
        feed_back = request.POST['experience']
        Comments = request.POST.get('comments')
        customer_name = request.POST.get('name')
        email = request.POST.get('email')
        if feed_back:
            customer_feedback = Feedback(feed_back=feed_back, Comments=Comments, customer_name=customer_name,
                                         email=email)
            customer_feedback.save()
            messages.success(request, 'Form Submitted Successfully!')
            return render(request, 'website/feedback.html', {'vendor': vendor, 'category': category})
        else:
            messages.error(request, 'Form not submitted! TRY AGAIN')
            return render(request, 'website/feedback.html', {'vendor': vendor, 'category': category})

    return render(request, 'website/feedback.html', {'vendor': vendor, 'category': category})


# contact through category for service handler view
def contact_via_service(request, slug):
    category = Categories.objects.all()
    flag = False
    if request.method == 'POST':
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
        messages.success(request,
                         'Form submission successful. SBT Professional team Contact You On Your Chosen Time')
        return render(request, 'website/form_category.html', {'slug': slug, 'category': category})

    return render(request, 'website/form_category.html', {'slug': slug, 'category': category})


# open Frenchise contact form
def frenchise(request):
    category = Categories.objects.all()
    if request.method == "POST":
        customer_name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile')
        address = request.POST.get('address')
        frenchise_option = request.POST['Interest']
        if frenchise_option:
            obj = FrenchiseContact(customer_name=customer_name, email=email, mobile_no=mobile_no, address=address,
                                   frenchise_option=frenchise_option)
            obj.save()
            send_mail(
                subject='New Frenchise customer',
                message=f"Customer Name = {customer_name}\nMobile No. ={mobile_no}\nAddress = {address}\nInterested in ={frenchise_option}",
                from_email='rk7305758@gmail.com',
                recipient_list=['ronniloreo@gmail.com'],
                fail_silently=False
            )
            messages.success(request,
                             'Form Submitted Successfully SBT Professionals Team Contacts You Within 24 hours!')
            return HttpResponseRedirect('/website/frenchise')
        else:
            messages.error(request, 'Form submittion Failed! TRY AGAIN')
            return render(request, 'website/frenchise.html', {'category': category})

    return render(request, 'website/frenchise.html', {'category': category})





#error handling view
def error_404_view(request,exception):
    return render(request,'website/error404.html')
