from Customer.models import Customer
import json
from django.core import exceptions

import requests
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# from django.views.generic.edit import FormView
from django.contrib import messages
# from website.models import *
from django.contrib.auth import login,logout
# #from app
from django.contrib.auth import get_user_model,authenticate
# #from authentication app
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.views.generic import TemplateView
from django.views import View, generic
from Employee.models import Employee
from Vendor.models import Vendor
from django.contrib.auth.hashers import check_password

from .forms import *
# #functions
from .functions import *
# #models
from .models import *

# from django.shortcuts import render, get_object_or_404, redirect
# from django.template import loader
# from django.http import HttpResponse
# from django import template

# from django.core.mail import send_mail
# # Create your views here.

User = get_user_model()


with open('config.json', mode='r') as file:
    parameters = json.load(file)

api_key = parameters['key']


def login_view(request):
    print('......POST')
    if request.method == "POST":
        print('......POST')
        loginusername = request.POST.get("phone")
        loginpassword = request.POST.get("password")
        print(loginusername)
        print(loginpassword)
        user = User.objects.get(phone=loginusername)
        user.check_password(loginpassword)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('dashboard:AdminHome')
        else:    
            return HttpResponse('Invalid credentials')  
    return render(request, "dashboard/accounts/auth-login.html")
            

        
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('dashboard:login')      
             
          



@login_required(login_url="/sbtadmin/login/") 
def index(request):

    # if slug == api_key:
    return render(request, "dashboard/index.html")
    # else:
        # return HttpResponse('not allowed to access')


# # @login_required(login_url="/sbtadmin/login/")
# def profile(request):
#     return render(request, "dashboard/profile.html")

class NewBranchView(View):
    """
    Save Branch Form to database
    TODO:Send Generated ID and Password Of Branch
    TODO:check if branch with a user already exists

    """
    template_name = "dashboard/forms/NewBranchForm.html"
    initial = {'key': 'value'}
    form_class = NewBranchForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_branch = Branch()
            response = check_if_branch_already_exists(form.cleaned_data['branch_name'])
            if response != None:
                messages.info(request,'Branch Already exists')
                # return HttpResponse('branch already exists')
                return redirect('dashboard:NewBranch')
             
            new_branch.branch_name = form.cleaned_data['branch_name']
            new_branch.Mobile_No = form.cleaned_data['mobile_no']
            new_branch.Mobile_No_2 = form.cleaned_data['mobile_no_2']
            new_branch.Address1 = form.cleaned_data['branch_address']
            new_branch.Address2 = form.cleaned_data['branch_address_2']
            new_branch.city = form.cleaned_data['branch_city']
            new_branch.state = form.cleaned_data['branch_state']
            new_branch.zipcode = form.cleaned_data['zip_code']
            new_branch.country = form.cleaned_data['branch_country']
            new_branch.EmailID = form.cleaned_data['branch_email_address']
            new_branch.regsitration_date = form.cleaned_data['regsitration_date']
            new_branch.landline_no = form.cleaned_data['landline_number']
            new_branch.extra_Info = form.cleaned_data['extra_info']
            new_branch.Contact_Person = form.cleaned_data['branch_contact_person']
            new_branch.branch_is_active = form.cleaned_data['branch_is_active']
            new_branch.Image = form.cleaned_data['branch_img']
            if new_branch.branch_is_active:
                from django.contrib.auth.hashers import make_password
                branch_user = User.objects.filter(phone=form.cleaned_data['mobile_no']).first()
                print(branch_user)  
                if branch_user != None:   
                    branch_user.set_password(make_password(password_genrator()))
                    branch_user.is_staff = True
                    branch_user.is_branch_user = True
                    branch_group = Group.objects.get(name='branch')
                    branch_group.user_set.add(branch_user) 
                    branch_user.save()
                    new_branch.user = branch_user
                    new_branch.save()  
                    password = password_genrator()
                    url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={branch_user.phone}&route=TA&msgtype=1&sms=Your USER ID = {branch_user.phone}\n password is {password}"
                    response = requests.request("GET",url)
                    print(response)
                    messages.success(request,'New Branch Created!')
                    return redirect('dashboard:AdminHome')
                else:
                    branch_user = User.objects.create(phone=new_branch.Mobile_No)
                
                    password = password_genrator()
                    print('...............',password)
                    url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={branch_user.phone}&route=TA&msgtype=1&sms=Your USER ID = {branch_user.phone}\n password is {password}"
                    response = requests.request("GET",url)
                    print(response)
                    branch_user.is_staff = True
                    branch_user.is_branch_user = True
                    branch_user.set_password(make_password(password_genrator()))
                    branch_group = Group.objects.get(name='branch')
                    branch_group.user_set.add(branch_user) 
                    branch_user.save()
                    new_branch.user = branch_user
                    new_branch.save()
                    messages.success(request,'New Branch Created!')
                    return redirect('dashboard:AdminHome')
        # return render(request, self.template_name, {'form': form})
           
    
    
class AllBranchView(generic.ListView):
    """
    Display All Branches From Database
    """
    model = Branch
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_branches.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




class AllEmployeeView(generic.ListView):
    """
    Display All Employees From Database
    """
    model = Employee
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_employees.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class EmployeeRequestView(View):
    def get(self,request):
        return render(request,'dashboard/Requests/EmployeeRequest.html')

class NewcategoryView(View):
    template_name = "dashboard/forms/NewCategoryForm.html"
    initial = {'key': 'value'}
    form_class = NewCategoryForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_category = Categories()
            response = check_if_category_already_exists(form.cleaned_data['category_name'])
            if response != None:
                messages.info(request,'Category Already exists')
                return redirect('dashboard:NewCategory')
            new_category.category_name = form.cleaned_data['category_name']
            new_category.category_is_active = form.cleaned_data['active']
            new_category.category_description = form.cleaned_data['description']
            new_category.Image = form.cleaned_data['img']
            new_category.save()
            messages.success(request,'New Category Created!')
            return redirect('dashboard:NewCategory')
        return render(request, self.template_name, {'form': form})
           
class AllCategoriesView(generic.ListView):
    """
    Display All Categories From Database
    """
    model = Categories
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_categories.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DetailCategoryView(DetailView):
    model = Categories
    template_name = 'dashboard/detail-edit/category-edit.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class TestView(View):
    def get(self,request):
        form =NewCategoryForm()
        return render(request,'dashboard/ui/ui-button.html',{'form':form})




class NewVendorView(View):
    def get(self,request):
        form = NewVendorForm()
        return render(request,'dashboard/forms/NewVendorForm.html',{'form':form})


class VendorRequestView(View):
    def get(self,request):
        return render(request,'dashboard/Requests/VendorRequest.html')

class AllVendorsView(generic.ListView):
    """
    Display All Vendors From Database
    """
    model = Vendor
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_vendors.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class AllResumeView(generic.ListView):
    """
    Display All Resumes From Database
    """
    model = Upload_resume
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_resumes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
    
class NewBannerView(View):
    template_name = "dashboard/forms/NewBannerForm.html"
    initial = {'key': 'value'}
    form_class = NewBannerForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_banner = Banner()
            response = check_if_banner_already_exists(form.cleaned_data['banner_name'])
            if response != None:
                messages.info(request,'Banner Already exists')
                return redirect('dashboard:NewBanner')
            new_banner.banner_name = form.cleaned_data['banner_name']
            new_banner.banner_img = form.cleaned_data['img']
            new_banner.save()
            messages.success(request,'New Banner Created!')
            return redirect('dashboard:AdminHome')
        return render(request, self.template_name, {'form': form})

class NewBanner2View(View):
    def get(self,request):
        form = NewBanner2Form()
        return render(request,'dashboard/forms/NewBannerForm.html',{'form':form})


class AllBannerView(generic.ListView):
    """
    Display All Banner From Database
    """
    model = Banner
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_banner.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





class AllBanner2View(View):
    def get(self,request):
        return render(request,'dashboard/ViewsAll/all_banner.html')


    
import os

from django.views.static import serve


def download_resume(request, *args, **kwargs):
    filepath = 'sbtdashboard/media/website/JobResumes/dummy_4NwMJgi.pdf'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))



class AllCustomerView(generic.ListView):
    """
    Display All Customer From Database
    """
    model = Customer
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_customer.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context