import json
from os import access
import pathlib
from django.db import reset_queries

import requests
from Customer.models import Customer
# from django.views.generic.edit import FormView
from django.contrib import messages
# #from authentication app
# #from app
# from website.models import *
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group
from django.core import exceptions
from django.db.models import Q
from django.db.models.aggregates import Avg
# from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
# from django.views.generic import TemplateView
from django.views import View, generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from Employee.models import Employee
from requests.api import request
from Vendor.models import Vendor

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


fn = pathlib.Path(__file__).parent.parent / 'config.json'
with open(fn,"r") as params:
    parameters = json.load(params)
api_key = parameters['key']

def search(request):
    if request.is_ajax():
        query = request.GET.get('query')
        obj = Branch.objects.filter(Q(branch_name__icontains = query) | Q(user__phone__icontains = query))
        data = list()
        for branch in obj:
            data.append({
               'phone': branch.user.phone,
               'branch_name': branch.branch_name,
               'Mobile_No': branch.Mobile_No,
               'city': branch.city,
               'state': branch.state,
               'EmailID': branch.EmailID,
            })
        data = json.dumps(data)
        print(data)
        return JsonResponse({'rv':query, 'obj':data})

    
        
            
        
        
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
            branch_user = Branch.objects.get(user=user)
            print(branch_user)
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
    branch_user = Branch.objects.filter(user=request.user).first()
    customers = Customer.objects.all()
   
    c_count =  customers.count()

    vendors = Vendor.objects.all()
    v_count =  vendors.count()
    
   
    active_vendors = Vendor.objects.filter(vendor_is_active=True)
    active_vendor_count = active_vendors.count()

    active_customers = Customer.objects.filter(customer_is_active=True)
    active_customer_count = active_customers.count()
    

    # if slug == api_key:
    return render(request, "dashboard/index.html",{'active_customers':active_customer_count,'active_vendors':active_vendor_count,'branch':branch_user,'user':request.user,'customers':c_count,'vendors':v_count})
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
        branch_user = Branch.objects.filter(user=request.user).first()
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form,'branch':branch_user})

    def post(self, request, *args, **kwargs):
        branch_user = Branch.objects.filter(user=request.user).first()
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
            new_branch.branch_type = form.cleaned_data['branch_type']
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
                    # district_group = Group.objects.get(name='district')
                    # district_group.user_set.add(district_group) 
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

class DetailBranchView(DetailView):
    model = Branch
    fields = '__all__'
    template_name = 'dashboard/accounts/profile.html'
    def get_context_data(self, **kwargs):
        # branch_user = Branch.objects.filter(user=self.user)
        context = super().get_context_data(**kwargs)
        # context['branch'] = branch_user
        return context


class UpdateBranch(View):
    """
    docstring
    """
    def post(self, request, *args, **kwargs):
        branch_user = Branch.objects.filter(id= self.kwargs['pk']).first()
        if branch_user != None:
            branch_user.landline_no = request.POST['phone']
            branch_user.EmailID = request.POST['email']
            branch_user.save()
            messages.success(request,'Details updated successully')
            return redirect('dashboard:AdminHome')
        # messages.info(request,'branch not exists')
        # return render(request,'dashboard/accounts/profile.html')

    



class AllEmployeeView(generic.ListView):
    """
    Display All Employees From Database
    """
    model = Employee
    paginate_by = 12
    template_name = 'dashboard/ViewsAll/all_employees.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context


# class EmployeeRequestView(View):
#     def get(self,request):
#         return render(request,'dashboard/Requests/EmployeeRequest.html')
        


class DetailEmployeeView(DetailView):
    model = Employee
    template_name = 'dashboard/detail-edit/employee-view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context



class NewcategoryView(View):
    template_name = "dashboard/forms/NewCategoryForm.html"
    initial = {'key': 'value'}
    form_class = NewCategoryForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        branch_user = Branch.objects.filter(user=request.user).first()
        return render(request, self.template_name, {'form': form,'branch':branch_user})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        branch_user = Branch.objects.filter(user=request.user).first()
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
        return render(request, self.template_name, {'form': form,'branch':branch_user})
           
class AllCategoriesView(generic.ListView):
    """
    Display All Categories From Database
    """
    model = Categories
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_categories.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context

class DetailCategoryView(DetailView):
    model = Categories
    template_name = 'dashboard/detail-edit/category-view.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context



# class TestView(View):
#     def get(self,request):
#         form =NewCategoryForm()
#         return render(request,'dashboard/tables/tables-basic.html',{'form':form})




# class NewVendorView(View):
#     def get(self,request):
#         form = NewVendorForm()
#         return render(request,'dashboard/forms/NewVendorForm.html',{'form':form})


# class VendorRequestView(View):
#     def get(self,request):
#         return render(request,'dashboard/Requests/VendorRequest.html')

class AllVendorsView(generic.ListView):
    """
    Display All Vendors From Database
    """
    model = Vendor
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_vendors.html'


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context



class DetailVendorView(DetailView):
    model = Vendor
    template_name = 'dashboard/detail-edit/vendor-view.html'

 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
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
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
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
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context





class AllBanner2View(View):
    def get(self,request):
        return render(request,'dashboard/ViewsAll/all_banner.html')


    
import os

from django.views.static import serve, template_translatable


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
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context

class DetailCustomerView(DetailView):
    model = Customer
    template_name = 'dashboard/detail-edit/customer-view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branch_user = Branch.objects.filter(user=context['view'].request.user).first()
        context['branch'] = branch_user
        return context


class BranchReportView(View):
    template_name = 'dashboard/forms/branch_report_form.html'
    initial = {'key': 'value'}
    form_class = BranchReportForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            branch_report = BranchReport()
            branch_report.branch = Branch.objects.filter(user=request.user).first()
            branch_report.title = form.cleaned_data['title']
            branch_report.report_detail = form.cleaned_data['description']
            branch_report.save()
            messages.success(request,'Report Submitted!')
            return redirect('dashboard:AdminHome')
        return render(request, self.template_name, {'form': form})



class ContactUsView(View):
    template_name = 'dashboard/forms/contact_us_form.html'
    initial = {'key': 'value'}
    form_class = ContactForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            branch_user_msg = BranchContact()
            branch_user_msg.branch = Branch.objects.filter(user=request.user).first()
            branch_user_msg.email = form.cleaned_data['email']
            branch_user_msg.desc = form.cleaned_data['description']
            branch_user_msg.save()
            url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={8683827398}&route=TA&msgtype=1&sms=Branch { branch_user_msg.branch} wants to contact you\n email is {branch_user_msg.email}\n message is {branch_user_msg.desc}"
            response = requests.request("GET",url)
            messages.success(request,'Message sent! Company executive will contact you as soon as possible')
            return redirect('dashboard:AdminHome')
        return render(request, self.template_name, {'form': form})
