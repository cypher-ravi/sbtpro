from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import *

# Check If a Branch Already `exists` ,If exists redirect to new branch view
# @receiver(pre_save,sender=NewBranch)
# def check_if_branch_exist(sender, instance, *args, **kwargs):
#     if instance:
#         all_branches = NewBranch.objects.all()
#         for branch in all_branches:
#             if branch.branch_name == instance.branch_name 
    