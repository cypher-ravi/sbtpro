from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import FreeListing, Plans, Order, Service, Job, Upload_resume,Categories
# from .PayTm import CheckSum
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    services = Service.objects.all()

    category = Categories.objects.all()

    plans = Plans.objects.all()
    return render(request, 'website/index.html', {'plans': plans,'category':category}, {'services': services})


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
    return HttpResponse('hey buddy!')


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
