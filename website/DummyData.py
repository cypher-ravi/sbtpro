from faker import Faker
from Vendor.models import *
from authentication.models import User
from website.models import Categories

class DummyData():
    lat_list = [29.66517435, 29.665181102451847, 29.665187052675083, 29.665192200669416, 29.665196546434586, 29.665200089970394, 29.66520283127667, 29.665204770353274, 29.66520590720011, 29.665206241817128, 29.665205774204313, 29.66520450436168, 29.665202432289302, 29.66519955798727, 29.66519588145573, 29.665191402694855, 29.665186121704863, 29.665180038486007, 29.6651731530386, 29.66516546536295, 29.665156975459446, 29.6651476833285, 29.665137588970556, 29.665126692386107, 29.66511499357568, 29.665102492539848, 29.66508918927921, 29.665075083794413, 29.665060176086136, 29.665044466155123, 29.66502795400211, 29.66501063962792, 29.664992523033376, 29.664973604219362, 29.664953883186804, 29.664933359936644, 29.664912034469886, 29.66488990678757, 29.664866976890753, 29.664843244780567, 29.66481871045815, 29.664843244780567, 29.664866976890753, 29.66488990678757, 29.664912034469886, 29.664933359936644, 29.664953883186804, 29.664973604219362, 29.664992523033376, 29.66501063962792, 29.66502795400211, 29.665044466155123, 29.665060176086136, 29.665075083794413, 29.66508918927921, 29.665102492539848, 29.66511499357568, 29.665126692386107, 29.665137588970556, 29.6651476833285, 29.665156975459446, 29.66516546536295, 29.6651731530386, 29.665180038486007, 29.665186121704863, 29.665191402694855, 29.66519588145573, 29.66519955798727, 29.665202432289302, 29.66520450436168, 29.665205774204313, 29.665206241817128, 29.66520590720011, 29.665204770353274, 29.66520283127667, 29.665200089970394, 29.665196546434586, 29.665192200669416, 29.665187052675083, 29.665181102451847]
    lng_list = [76.99499434128728, 77.00533254669534, 77.0156707534089, 77.02600896126306, 77.03634717009292, 77.0466853797336, 77.0570235900202, 77.06736180078781, 77.07770001187154, 77.0880382231065, 77.0983764343278, 77.10871464537053, 77.11905285606981, 77.12939106626072, 77.13972927577838, 77.15006748445789, 77.16040569213436, 77.1707438986429, 77.18108210381858, 77.19142030749654, 77.20175850951189, 77.21209670969972, 77.22243490789513, 77.23277310393324, 77.24311129764915, 77.25344948887796, 77.26378767745479, 77.27412586321475, 77.28446404599293, 77.29480222562447, 77.30514040194446, 77.31547857478799, 77.32581674399022, 77.33615490938622, 77.34649307081114, 77.35683122810005, 77.3671693810881, 77.3775075296104, 77.38784567350204, 77.39818381259818, 77.40852194673388, 77.39818381259818, 77.38784567350204, 77.3775075296104, 77.3671693810881, 77.35683122810005, 77.34649307081114, 77.33615490938622, 77.32581674399022, 77.31547857478799, 77.30514040194446, 77.29480222562447, 77.28446404599293, 77.27412586321475, 77.26378767745479, 77.25344948887796, 77.24311129764915, 77.23277310393324, 77.22243490789513, 77.21209670969972, 77.20175850951189, 77.19142030749654, 77.18108210381858, 77.1707438986429, 77.16040569213436, 77.15006748445789, 77.13972927577838, 77.12939106626072, 77.11905285606981, 77.10871464537053, 77.0983764343278, 77.0880382231065, 77.07770001187154, 77.06736180078781, 77.0570235900202, 77.0466853797336, 77.03634717009292, 77.02600896126306, 77.0156707534089, 77.00533254669534]

    
    COUNTER = 1
    def create(self, iterations):
        f = Faker()

        CATEGORY = [
            'Product Stores',
            'Education & Training',
            'Travel &Transport',
            'Education & Training',
            'Health & wellness',
            'Product Stores',
            'Product Stores',
            'Hotel & Restaurants',
            'Fashion',
            'Hotel & Restaurants',
            'Hotel & Restaurants',
            'Education & Training',
            'Health & wellness',
            'Hotel & Restaurants',
            'Properties & Rentals',
            'Education & Training',
            'Hotel & Restaurants',
            'IT & Computer Service',
        ]

        STATUS = ['', 'verified', 'new']


        for i in range(0, iterations):
            # User Creation
            obj = User()

            obj.phone = 9+f.random_int(0,99999999)
            obj.first_name = f.first_name()
            obj.otp_count = f.random_int(0,9)
            obj.key = None
            obj.is_active =f.boolean()
            obj.is_verified = f.boolean()

            obj.is_vendor_registered =f.boolean()
            obj.is_vendor_paid = f.boolean()

            obj.is_branch_user = f.boolean()

            obj.is_customer_registered = f.boolean()
            obj.is_customer_paid = f.boolean()

            obj.is_employee_registered =  f.boolean()
            obj.is_employee_paid =  f.boolean()

            obj.save()

            #  User end--------------------------------------


            objCategory = Categories()
            # category_id = models.AutoField(primary_key=True)
            objCategory.category_name = f.word()
            objCategory.Image = 'default.jpg'
            objCategory.category_is_active = f.boolean()
            objCategory.save()


            keywordObj = KeyWord()
            # id = models.AutoField(primary_key = True)
            keywordObj.name = f.word()
            keywordObj.save()


            # service_id = models.AutoField(primary_key=True)
            servicesObj = VendorServices()
            servicesObj.service_id = self.COUNTER +i
            self.title = f.text()
            servicesObj.title = self.title[:20]
            self.description = f.text()
            servicesObj.description = self.description[:200]
            servicesObj.service_is_active = f.boolean()
            servicesObj.save()

    
            videoObject = VendorVideos()
            # videoObject.video_id = #models.AutoField(primary_key=True)
            self.title = f.text()
            videoObject.title = self.title[:20]
            videoObject.video_url = f.url()
            videoObject.save()


            # image_id = models.AutoField(primary_key=True)
            imageObject = VendorImages()
            self.title = f.text()
            imageObject.title = self.title[:20]
            imageObject.image_url = 'default.jpg'
            imageObject.save()


            vendorObj = Vendor()
            vendorObj.vendor_id = self.COUNTER + i
            vendorObj.user = obj
            # vendor_id =
            vendorObj.Name = f.first_name()
            vendorObj.Company_Name = f.company()
            vendorObj.Busniess_Type = objCategory
            # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,blank=True,null=True)
            vendorObj.Service_decsription = f.text()
            vendorObj.Mobile_No = str(9+f.random_int(0,99999999))
            vendorObj.Mobile_No_2 = str(9+f.random_int(0,99999999))
            vendorObj.Address1 = f.address()
            vendorObj.Address2 = f.address()
            vendorObj.city = f.city()
            vendorObj.state = f.state()
            vendorObj.PinCode = f.postcode()
            vendorObj.Contact_Person = f.first_name()
            vendorObj.EmailID = f.email()
            vendorObj.Landline = str(9+f.random_int(0,99999999))
            vendorObj.GST_No = f.random_int()
            vendorObj.Pan_No = f.random_int()
            vendorObj.TIN_No = f.random_int()
            vendorObj.Registered_Trade_Name = vendorObj.Name
            vendorObj.Facebook_URL = ''
            vendorObj.Twitter_URL =''
            vendorObj.website_URL =''
            vendorObj.established_date = f.date()
            vendorObj.Status  = STATUS[f.random_int(0,2)]
            vendorObj.Other_Info = ''
            vendorObj.Discount_Percentage = f.random_int(0, 100)
            vendorObj.Longitude = self.lng_list[i] # f.longitude() 
            vendorObj.Latitude = self.lat_list[i] # f.latitude()
            vendorObj.submit_date = f.date()
            vendorObj.Image = 'default.jpg'
            vendorObj.type_of_commodity_or_business = ''
            vendorObj.geograpgical_area = ''
            vendorObj.business_history_with_sbt= ''
            obj = Plan.objects.get(plan_id = f.random_int(4,6))
            vendorObj.registration_fee = obj
            vendorObj.vendor_is_active = f.boolean()
            vendorObj.budget = str(f.random_int(0,1000))
            vendorObj.save()

            vendorObj.keywords.add(keywordObj) # MtoM

            # employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
        
    def format(self):
        User.objects.all().delete()
        Vendor.objects.all().delete()
        VendorServices.objects.all().delete()
        VendorImages.objects.all().delete()
        VendorVideos.objects.all().delete()
        Categories.objects.all().delete()
        KeyWord.objects.all().delete()

