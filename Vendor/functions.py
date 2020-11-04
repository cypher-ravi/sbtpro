

import base64

from PIL import Image
from django.contrib.auth import get_user_model


from django.http.response import HttpResponse
from Vendor.models import Vendor
from dashboard.models import Branch




def assign_branch_to_vendor(vendor_city,vendor_state,user):
    branch_filter_by_city = Branch.objects.filter(branch_name__icontains=vendor_city)
    branch_filter_by_state = Branch.objects.filter(branch_name__icontains=vendor_state)
    vendor_obj = Vendor.objects.filter(user=user).first()
    if branch_filter_by_city.exists():
        vendor_obj.branch = branch_filter_by_city[0]
        vendor_obj.save()
        return HttpResponse('assign_branch_to_vendor by city')
    elif branch_filter_by_state.exists():
        vendor_obj.branch = branch_filter_by_state[0]
        vendor_obj.save()
        return HttpResponse('assign_branch_to_vendor by state')
    else: 
        branch = Branch.objects.filter(branch_type__icontains='root')
        vendor_obj.branch = branch[0]
        vendor_obj.save()
        return HttpResponse('root_branch_assign_to_vendor')           


# def convert_to_image_and_save_to_VendorImages(images,user):
#    images_received = json.loads(request.data['vendor_images'])
            # print(len(images_received))
            # images=list()
            # for i in range(0,6):
            #     if i<len(images_received):
            #         images.append(images_received[i]['image'])
            #     else:
            #         # images.append(None)
