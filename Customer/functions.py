


from dashboard.models import Branch
from django.http.response import HttpResponse

from Customer.models import Customer


def assign_branch_to_customer(customer_city,customer_state,user):
    branch_filter_by_city = Branch.objects.filter(branch_name__icontains=customer_city)
    branch_filter_by_state = Branch.objects.filter(branch_name__icontains=customer_state)
    customer_obj = Customer.objects.filter(user=user).first()
    if branch_filter_by_city.exists():
        customer_obj.branch = branch_filter_by_city[0]
        customer_obj.save()
        return HttpResponse('assign_branch_to_customer by city')
    elif branch_filter_by_state.exists():
        customer_obj.branch = branch_filter_by_state[0]
        customer_obj.save()
        return HttpResponse('assign_branch_to_customer by state')
    else: 
        branch = Branch.objects.filter(branch_type__icontains='root')
        customer_obj.branch = branch[0]
        customer_obj.save()
        return HttpResponse('root_branch_assign_to_customer')
           