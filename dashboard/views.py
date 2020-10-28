from .forms import *
import json

# from django.views.generic import TemplateView
from django.views import generic 
from django.views import View
# from django.views.generic.edit import FormView
# from django.contrib import messages
# #from authentication app
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
# from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.shortcuts import redirect, render

# #models
from .models import *
from Employee.models import Employee
from Vendor.models import Vendor
# from website.models import *
# from django.contrib.auth import login
# #from app
from django.contrib.auth import get_user_model
# from django.shortcuts import render, get_object_or_404, redirect
# from django.template import loader
# from django.http import HttpResponse
# from django import template

# #functions
from .functions import *
# from django.core.mail import send_mail
# # Create your views here.

User = get_user_model()


with open('config.json', mode='r') as file:
    parameters = json.load(file)

api_key = parameters['key']

"""
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            loginusername = form.cleaned_data.get("username")
            loginpassword = form.cleaned_data.get("password")
            print(User.objects.filter(username= form.cleaned_data.get("username")))
            print(User.objects.filter(password= form.cleaned_data.get("password")))
            
            user = authenticate(request, username=loginusername,
                password=loginpassword)
            print(user)
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, 'Login Successful!')
                return redirect('dashboard:AdminHome')
            else:    
                return HttpResponse('Invalid credentials')  
        else:
            return HttpResponse('Error validating the form')   
    return render(request, "dashboard/accounts/auth-login.html", {"form": form})
            
"""
        
            
            
             
          


# # def register_user(request):

# #     msg     = None
# #     success = False

# #     if request.method == "POST":
# #         form = SignUpForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get("username")
# #             raw_password = form.cleaned_data.get("password1")
# #             user = authenticate(username=username, password=raw_password)

# #             msg     = 'User created.'
# #             success = True
            
# #             #return redirect("/login/")

# #         else:
# #             msg = 'Form is not valid'    
# #     else:
# #         form = SignUpForm()

# #     return render(request, "dashboard/accounts/register.html", {"form": form, "msg" : msg, "success" : success })




# @login_required(login_url="/sbtadmin/login/") 
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
                branch_user = User.objects.create(phone=new_branch.Mobile_No,password=make_password(
                              password_genrator()),is_staff=True)
             
                password = password_genrator()
                branch_user.is_staff = True
                branch_group = Group.objects.get(name='branch')
                branch_group.user_set.add(branch_user) 
                new_branch.user = branch_user
                # send_mail(
                #     subject='Your ID and Password',
                #     message=f"username = {branch_user.username}\npassword = {password}",
                #     from_email='rk7305758@gmail.com',
                #     recipient_list=[new_branch.EmailID],
                #     fail_silently=False
                #     # contact@sbtprofessionals.com
                #     # teamofprofessionals2015@gmail.com
                # )
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


class NewEmployeeView(View):
    """
    Save Branch Form to database
    TODO:Send Generated ID and Password Of Branch

    """
    template_name = "dashboard/forms/NewEmployeeForm.html"
    initial = {'key': 'value'}
    form_class = NewEmployeeForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            new_employee = Employee()
            response = check_if_employee_already_exists(form.cleaned_data['employee_name'])
            if response != None:
                messages.info(request,'Employee Already exists')
                return redirect('dashboard:NewEmployee')
            new_employee.employee_name = form.cleaned_data['employee_name']
            new_employee.father_name = form.cleaned_data['employee_father_name']
            new_employee.Mobile_No = form.cleaned_data['mobile_no']
            new_employee.Mobile_No_2 = form.cleaned_data['mobile_no_2']
            new_employee.Address1 = form.cleaned_data['employee_address']
            new_employee.Address2 = form.cleaned_data['employee_address_2']
            new_employee.city = form.cleaned_data['city']
            new_employee.state = form.cleaned_data['state']
            new_employee.zipcode = form.cleaned_data['zip_code']
            new_employee.country = form.cleaned_data['country']
            new_employee.EmailID = form.cleaned_data['employee_email_address']
            new_employee.joining_date = form.cleaned_data['joining_date']
            new_employee.gross_salary = form.cleaned_data['gross_salary']
            new_employee.gender = form.cleaned_data['gender']
            new_employee.date_of_birth = form.cleaned_data['date_of_birth']
            new_employee.extra_Info = form.cleaned_data['extra_info']
            new_employee.Contact_Person = form.cleaned_data['contact_person']
            new_employee.employee_designation = form.cleaned_data['employee_designation']
            new_employee.employee_is_active = form.cleaned_data['employee_is_active']
            new_employee.Image = form.cleaned_data['employee_img']
            new_employee.save()
            messages.success(request,'New Employee Added!')
            return redirect('dashboard:AdminHome')
        return render(request, self.template_name, {'form': form})


class AllEmployeeView(generic.ListView):
    """
    Display All Employees From Database
    """
    model = Employee
    paginate_by = 10
    template_name = 'dashboard/ViewsAll/all_employees.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


    
from django.views.static import serve
import os

def download_resume(request, *args, **kwargs):
    filepath = 'sbtdashboard/media/website/JobResumes/dummy_4NwMJgi.pdf'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
