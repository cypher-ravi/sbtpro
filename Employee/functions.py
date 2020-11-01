from django.http import HttpResponse
from Employee.models import Employee
from dashboard.models import Branch


def assign_branch_to_employee(employee_city,employee_state,user):
    branch_filter_by_city = Branch.objects.filter(branch_name__icontains=employee_city)
    branch_filter_by_state = Branch.objects.filter(branch_name__icontains=employee_state)
    employee_obj = Employee.objects.filter(user=user).first()
    if branch_filter_by_city.exists():
        employee_obj.branch = branch_filter_by_city[0]
        employee_obj.save()
        return HttpResponse('assign_branch_to_employee by city')
    elif branch_filter_by_state.exists():
        employee_obj.branch = branch_filter_by_state[0]
        employee_obj.save()
        return HttpResponse('assign_branch_to_employee by state')
    else: 
        branch = Branch.objects.filter(branch_type__icontains='root')
        employee_obj.branch = branch[0]
        employee_obj.save()
        return HttpResponse('root_branch_assign_to_employee')
           