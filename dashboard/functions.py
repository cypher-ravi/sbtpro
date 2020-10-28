from .models import * 
from django.http import HttpResponse
from website.models import *

# Check If a Branch Already `exists` ,If exists redirect to new branch view
def check_if_branch_already_exists(branchname):
    branch = Branch.objects.filter(branch_name=branchname)
    if branch.exists():
        return HttpResponse('Branch Already Exists!')
        
    
    
      

# Check If a category Already `exists` ,If exists redirect to new category view
def check_if_category_already_exists(categoryname):
    category = Categories.objects.filter(category_name__icontains=categoryname)
    if category.exists():
        return HttpResponse('category Already Exists!')
        
    

# Check If a employee Already `exists` ,If exists redirect to new category view
def check_if_employee_already_exists(employee_name):
    employee = Employee.objects.filter(employee_name=employee_name)
    if employee.exists():
        return HttpResponse('Employee Already Exists!')
        

# Check If a banner Already `exists` ,If exists redirect to new category view
def check_if_banner_already_exists(bannername):
    banner = Banner.objects.filter(banner_name=bannername)
    if banner.exists():
        return HttpResponse('banner Already Exists!')
        
def password_genrator():
    import string
    import random
    uppercase = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    password = []
    password.extend(list(uppercase))
    password.extend(list(lower_case))
    password.extend(list(digits))
    new_password = ''.join(random.sample(password,8))
    return new_password
