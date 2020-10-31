# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import VALID_STATE_CHOICES,GENDER_CHOICES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


BRANCH_TYPE_CHOICES = (
    ("state", "state"),
    ("district", "district"),
    ("tehsil", "tehsil"),
    ("village", "village"),

)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "value"       : "",
                "class"       : "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "value"       : "ApS12_ZZs8",                
                "class"       : "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class NewBranchForm(forms.Form):
    """
    form for New Branch

    """
    branch_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Branch name",
                "class" : "form-control",
                "aria-label" : "Branchname",
                "aria-describedby" : "basic-addon1",
                "type" : "text",
                "id" : "input-branchname",
            }
        ))
    branch_email_address = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Branch Email Address",
                "class" : "form-control",
                "type" : "email",
                "id" : "input-email",
            }
        ))
    mobile_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "MobileNo",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-mobile",

            }
        )
    )
    mobile_no_2 = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "MobileNo 2",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-mobile2",

            }
        )
    )
    landline_number = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Landline number",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-landline-number",

            }
        )
    )
    regsitration_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Enter Registration date",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-register",

            }
        )
    )
    branch_is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "id" : "active"
            }
        ),
        required=False)
    branch_address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1234 Main St",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputAddress",
            }
        ))
    branch_address_2 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Apartment, studio, or floor",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputAddress2",
            }
        ))
    branch_city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "karnal",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputCity",
            }
        )) 

    branch_state = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "type" : "text",
                "id" : "inputState",
                "class" : "form-control form-control-alternative",
            },
        choices=VALID_STATE_CHOICES
        )
        
    )
    branch_type = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "type" : "text",
                "id" : "inputtype",
                "class" : "form-control form-control-alternative",
            },
        choices=BRANCH_TYPE_CHOICES
        )
        
    )
    branch_country = CountryField(blank_label='(select country)').formfield(required=False,widget=CountrySelectWidget(attrs={
        'class':'form-control ',
        "id" : "input-country",
        "type" : "text",
    }))
    zip_code = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Postal code",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputZip",

            }
        )
    )
    extra_info = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "A few words about branch...",
                "class" : "form-control form-control-alternative",

            }
        )
    )
    branch_contact_person = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Contact Person",
                "class" : "form-control",
                "type" : "text",
                "id" : "contact-person",
            }
        ))
    branch_img = forms.ImageField(required=False,
                    widget=forms.FileInput(
                        attrs={
                            "type" : "file",
                            "class" : "custom-file-input",
                            "id" : "inputGroupFile04",
                            "aria-describedby" : "inputGroupFileAddon04",
                        }
                    ))
   

class NewEmployeeForm(forms.Form):
    """
    form for New Employee

    """
    employee_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee name",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-employee-name",
            }
        ))
    employee_father_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Father name",
                "class" : "form-control ",
                "type" : "text",
                "id" : "input-father-name",
            }
        ))

    employee_email_address = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email Address",
                "class" : "form-control ",
                "type" : "email",
                "id" : "input-email",
            }
        ))
    mobile_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Mobile number",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-mob1",

            }
        )
    )
    mobile_no_2 = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Mobile number 2",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-mob2",

            }
        )
    )
    joining_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Joining Date",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-joindate",

            }
        )
    )
    gross_salary = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Gross salary",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-gross-salary",

            }
        )
    )
    gender = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "type" : "text",
                "id" : "input-gender",
                "class" : "form-control",
            },
        choices=GENDER_CHOICES
        )
        
    )
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Date Of Birth",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-dob",

            }
        )
    )
    employee_is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "id" : "active"
            }
        ),
        required=False)
    employee_address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address 1",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-address",
            }
        ))
    employee_address_2 = forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
            "placeholder" : "Address 2",
            "class" : "form-control",
            "type" : "text",
            "id" : "input-address2",
        }
    ))
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "karnal",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-city",
            }
        )) 

    state = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "type" : "text",
                "id" : "input-state",
                "class" : "form-control",
            },
        choices=VALID_STATE_CHOICES
        )
        
    )
    country = CountryField(blank_label='(select country)').formfield(required=False,widget=CountrySelectWidget(attrs={
        'class':'form-control form-control-alternative',
        "id" : "input-country",
        "type" : "text",
    }))
    zip_code = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Postal code",
                "class" : "form-control",
                "type" : "number",
                "id" : "input-zip",

            }
        )
    )
    extra_info = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "A few words about employee...",
                "class" : "form-control ",
                " aria-label" : "With textarea ",

            }
        )
    )
    contact_person = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Contact Person",
                "class" : "form-control",
                "type" : "text",
                "id" : "contact-person",
            }
        ))
    employee_designation= forms.CharField(
    required=True,
    widget=forms.TextInput(
        attrs={
            "placeholder" : "Employee Designation",
            "class" : "form-control",
            "type" : "text",
            "id" : "input-employee-designation",
        }
    ))
    employee_img = forms.ImageField(required=False,
                    widget=forms.FileInput(
                        attrs={
                            "type" : "file",
                            "class" : "custom-file-input",
                            "id" : "inputGroupFile04",
                            "aria-describedby" : "inputGroupFileAddon04",
                        }
                    ))
    employee_is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "id" : "active"
            }
        ),
        required=True)


class NewCategoryForm(forms.Form):
    """
    form for New Category

    """
    category_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Category Name",
                "class" : "form-control ",
                "type" : "text",
                "id" : "basic-addon1",
            }
        ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id" : "desc",
                "placeholder" : "Description",
                "class" : "form-control ",
                "aria-label" : "desc",

            }
        )
    )
    img = forms.ImageField(required=False)
    active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "id" : "active"
            }
        ),
        required=False)



class NewVendorForm(forms.Form):
    """
    form for New Vendor

    """
    name_of_company = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name Of Company",
                "class" : "form-control",
                "aria-label" : "Companyname",
                "aria-describedby" : "basic-addon1",
                "type" : "text",
                "id" : "input-company-name",
            }
        ))
    vendor_address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1234 Main St",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputAddress",
            }
        ))
    vendor_address_2 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Apartment, studio, or floor",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputAddress2",
            }
        ))
    mobile_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "MobileNo",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-mobile",

            }
        )
    )
    mobile_no_2 = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "MobileNo 2",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-mobile2",

            }
        )
    )
    fax_number = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Fax Number",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-fax",

            }
        )
    )
    vendor_email_address = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Vendor Email Address",
                "class" : "form-control",
                "type" : "email",
                "id" : "input-email",
            }
        ))
    
    vendor_website_url = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Website url",
                "class" : "form-control",
                "type" : "url",
                "id" : "input-url",
            }
        )
    )
    vendor_android_app_url = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Android App url",
                "class" : "form-control",
                "type" : "url",
                "id" : "input-app-url",
            }
        )
    )

    vendor_contact_person = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Contact Person",
                "class" : "form-control",
                "type" : "text",
                "id" : "contact-person",
            }
        ))
    landline_number = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Landline number",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-landline-number",

            }
        )
    )
    date_company_was_established = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Established date",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-register",

            }
        )
    )
    vendor_is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "id" : "active"
            }
        ),
        required=False)
    
    vendor_city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "karnal",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputCity",
            }
        )) 

    vendor_state = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "type" : "text",
                "id" : "inputState",
                "class" : "form-control form-control-alternative",
            },
        choices=VALID_STATE_CHOICES
        )
        
    )
    vendor_country = CountryField(blank_label='(select country)').formfield(required=False,widget=CountrySelectWidget(attrs={
        'class':'form-control ',
        "id" : "input-country",
        "type" : "text",
    }))
    zip_code = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Postal code",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputZip",

            }
        )
    )
    extra_info = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "A few words about branch...",
                "class" : "form-control form-control-alternative",

            }
        )
    )
    employee_id_reference = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee name / ID",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-employee",
            }
        )
    )
    tin_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Tin No.",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputTin",

            }
        )
    )
    pan_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Pan No.",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputPan",

            }
        )
    )
    gst_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Gst No.",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputGst",

            }
        )
    )
    

class NewBannerForm(forms.Form):
    """
    form for New Banner

    """
    banner_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Banner Name",
                "class" : "form-control ",
                "type" : "text",
                "id" : "basic-addon1",
            }
        ))
    
    img = forms.ImageField(
        required=True,
        )
        
class NewBanner2Form(forms.Form):
    """
    form for New Banner

    """
    banner_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Banner Name",
                "class" : "form-control ",
                "type" : "text",
                "id" : "basic-addon1",
            }
        ))
    
    img = forms.ImageField(
        required=True,widget=forms.FileInput(
            attrs={
                
                "class" : "custom-file-input ",
                "type" : "file",
                "id" : "inputImg",
                "aria-describedby" : "inputGroupFileAddon04",
            }
        ))
        
    
class BranchReportForm(forms.Form):
    """
    form for submittion of branch report

    """
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "title",
                "class" : "form-control ",
                "type" : "text",
                "id" : "title",
            }
        ))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "description",
                "class" : "form-control ",
                "type" : "text",
                "id" : "description",
            }
        ))
    
        
class ContactForm(forms.Form):
    """
    form for submittion of branch report

    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Enter Email",
                "class" : "form-control ",
                "type" : "email",
                "id" : "Email",
            }
        ))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Message",
                "class" : "form-control ",
                "type" : "text",
                "id" : "description",
            }
        ))
    
        
    