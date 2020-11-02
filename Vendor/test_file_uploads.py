
import requests
import json

# url = 'http://127.0.0.1:8000/api/v1/posts/'
# patch_url = 'http://127.0.0.1:8000/api/v1/posts/2/'
url = 'http://192.168.29.249:8000/vendor/VendorAPI/'
with open('D:/workspace sbt/restapifordeployement/sbtdashboard/media/buasinesslisting.jpg', 'rb') as f:
  
    f_aws = open('D:/workspace sbt/restapifordeployement/sbtdashboard/media/beauty_services.jpg', 'rb')
    f_ami = open('D:/workspace sbt/restapifordeployement/sbtdashboard/media/computer.jpg', 'rb')

    multiple_files = [
        ('vendor_images', ('beauty_services.jpg', f_aws)),
        ('vendor_images', ('computer.jpg', f_ami)),
    ]

    data = dict()
    data['user'] = 35
    data['Name'] = 'oreo'



    # res = requests.post(url, data, files=files, headers={'content_type': 'multipart/form-data'})
    res = requests.post(url, data=data, files=multiple_files, headers={'content_type': 'multipart/form-data'})
    # res = requests.patch(patch_url, data=patch_data,  files=multiple_files, headers={'content_type': 'multipart/form-data'})
    print(res.text)
