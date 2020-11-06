import random
from website.PayTm import CheckSum
from website.validations import discount_validation
from django.http.response import HttpResponse, JsonResponse
from Customer.models import Customer
from authentication.serializers import UserSerializer
import json
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import requests
from Customer.serializers import CustomerPlanSerializer
from dashboard.models import Banner
from dashboard.serializers import AllBannerSerializer
from django.conf import settings
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, viewsets
from rest_framework.metadata import SimpleMetadata
from rest_framework.response import Response
from rest_framework.views import APIView
# from Vendor.models import Vendor
from Vendor.serializers import *
from website.models import Categories, Order, Order_Payment, Plan
from Vendor.pagination import PaginationForVendor

from .serializers import *

with open("config.json", "r") as params:
    parameters = json.load(params)

from authentication.pagination import PaginationForVendorAndCategory
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


User = get_user_model()
    
class CategorySearchView(generics.ListAPIView):
    """
    Search API for categroies 
    """
    queryset = Categories.objects.all()
    pagination_class = PaginationForVendorAndCategory
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']

class VendorSearchView(generics.ListAPIView):
    """
    Search API for vendors + category_id
    """
    
    pagination_class = PaginationForVendor
    serializer_class = VendorSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Company_Name']

    def get_queryset(self):
        vendors = Vendor.objects.filter(Busniess_Type=self.kwargs['category_id'])
        return vendors



class FrenchiseRequestAPIView(generics.CreateAPIView):
    """
    This API accepts post requests for franchise requests 
    """
    queryset = FrenchiseContact.objects.all()
    serializer_class = FrenchiseRequestSerializer
    metadata_class = SimpleMetadata

    def post(self, request, format=None):
        key = parameters['key']
        # if slug == key:
        serializer = FrenchiseRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            name = request.data['name']
            mobile_no = request.data['mobile_no']
            email = request.data['email']
            address = request.data['address']
            frenchise_option = request.data['franchise_option']
            company_name = request.data['company_name']
            message = request.data['message']
            url = f'http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={+918683827398}&route=TA&msgtype=1&sms=New Frenchise request \n\nName ={name} \nMobile= {mobile_no} \nEmail= {email}\nAddress= {address} \nFrenchise option= {frenchise_option} \nMessage= {message} \nCompany Name= {company_name}'
            response = requests.request("GET",url)
            return Response({'sent':'True'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class AppFeedBackAPIView(generics.CreateAPIView):
    """
    This API accepts post requests for Feedback 
    """
    queryset = AppFeedBack.objects.all()
    serializer_class = AppFeedBackSerializer
    metadata_class = SimpleMetadata

    def post(self, request, format=None):
        key = parameters['key']
        # if slug == key:
        serializer = AppFeedBackSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'sent':'True'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





          

 #--------------------------------------------ViewSets----------------------------------------------------------                  
 
class NewCategoryAPI(viewsets.ModelViewSet):
    """
    This Paginated API creates new category and delete,update via id using viewsets

    """
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationForVendorAndCategory
    
   



class ToptList(viewsets.ReadOnlyModelViewSet):
    """
    This API creates new Top,view and edit using viewsets

    """
    queryset = TOP.objects.all()
    serializer_class = TOPSerializer

    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            top = TOP.objects.all()
            serializer = TOPSerializer(top,many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class PlanList(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = CustomerPlanSerializer
    """
    List of all Plans

    """
    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            plan = Plan.objects.all()
            serializer = CustomerPlanSerializer(plan,many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PlanDetail(viewsets.ReadOnlyModelViewSet):
    """
    Plan Detail By ID

    """
    serializer_class = CustomerPlanSerializer
    queryset = Plan.objects.all()
    
    def get(self, request,plan_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            serializer = CustomerPlanSerializer(plan, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class BannersList(viewsets.ReadOnlyModelViewSet):
    """
    List of all Banners

    """
    queryset = Banner.objects.all()
    serializer_class = AllBannerSerializer

    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            serializer = AllBannerSerializer(banner, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserPaymentStatus(generics.GenericAPIView):
    """
    user object By user ID

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        user = User.objects.filter(id=pk)
        if user.exists():
            key = parameters['key']
            if slug == key:   
                serializer = UserSerializer(user[0],many=False)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':'user not exists'})
        









"""
----------------------------------------------Payment Part------------------------------------------------------------

"""


def purchase(request, plan_id, user,amount,discount,role):
    plan_id = int(plan_id)
    user = int(user)
    amount = int(amount)
    discount = int(discount)
    if request.method == 'GET':
        if role == 'customer':
            customer_user = Customer.objects.filter(user=user).first()
            print(customer_user)
            plan = Plan.objects.filter(plan_id=plan_id)
            total = discount * plan[0].plan_amount
            if plan != None:
                if customer_user != None:
                    return render(request, 'checkout2.html', {'role':role, 'plan': plan[0], 'customer': customer_user, 'total': total,'amount':amount, 'discount': discount,'user':user})
                else:
                    return HttpResponse('Please sign up for customer first')
            else:
                return HttpResponse('Invalid plan and user')
        else:
            vendor_user = Vendor.objects.filter(user=user).first()
            print(vendor_user)
            plan = Plan.objects.filter(plan_id=plan_id)
            total = plan[0].plan_amount
            if plan != None:
                if vendor_user != None:
                    return render(request, 'checkout2.html', {'role':role, 'plan': plan[0], 'vendor': vendor_user, 'total': total,'amount':amount, 'discount': discount,'user':user})
                else:
                    return HttpResponse('invalid vendor')
            else:
                return HttpResponse('Invalid plan and user')



def customer_card_purchase(request, plan_id, customer_id, user,role):
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    # discount won't work if empty
        # if request.user.is_authenticated:
    
    if request.method == 'POST':
        plan_id = plan_id
        if role == 'customer':
            user_plus_customer = Customer.objects.get(customer_id=customer_id)
            user = User.objects.filter(id=user).first()
            phone = user.phone
            print(user_plus_customer)
            try:
                plan = Plan.objects.get(plan_id=plan_id)
            except:
                return HttpResponse('Please enter a valid Plan Id')

            try:
                discount = int(request.POST.get('discount'))
            except ValueError:
                return HttpResponse('Please select a valid discount value')

            user_amount = request.POST.get('amount')
            if discount != "" and discount != None:
                response_dict = discount_validation(plan_id, discount, int(user_amount))
                if response_dict['error'] != None:
                    return HttpResponse(response_dict['error'])
                amount = discount * plan.plan_amount
            else:
                amount = plan.plan_amount

            print('aya..........')
            order_id = random.randint(1, 999999)
            email_id = user_plus_customer.EmailID
            name = user_plus_customer.customer_name
            address = user_plus_customer.Address
            state = user_plus_customer.state
            city = user_plus_customer.city
            zip_code = user_plus_customer.zipcode
            plan_id = plan.plan_id

            # Check if user not provide any discount value

            print(user)
            print(type(user))
            order = Order(name=name, user=user, email_id=email_id, phone=phone, address=address, city=city,
                            state=state, zip_code=zip_code, amount=amount, discount=discount,order_id=order_id, plan_id=plan, order_completed=False,role=role)
            order.save()

            # sending details to paytm gateway in form of dict
            detail_dict = {
                "MID": parameters['merchant_id'],
                "WEBSITE": "WEBSTAGING",
                "INDUSTRY_TYPE_ID": "Retail",
                "CUST_ID": str(email_id),
                "CHANNEL_ID": "WEB",
                "ORDER_ID": str(order_id),
                "TXN_AMOUNT": str(amount),
                "CALLBACK_URL": "http://192.168.29.249:8000/api/req_handler",
            }

            param_dict = detail_dict
            CheckSum.generateSignature
            param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                detail_dict, parameters['merchant_key'])
            # print('.................', param_dict)
            return render(request, 'redirect.html', {'detail_dict': param_dict})

            return HttpResponse('Either amount or Discount not Matched')
        elif role == 'vendor':
            discount = int(request.POST.get('discount'))
            user_plus_vendor = Vendor.objects.get(vendor_id=customer_id)
            user = User.objects.filter(id=user).first()
            phone = user.phone
            print(user_plus_vendor)
            try:
                plan = Plan.objects.get(plan_id=plan_id)
            except:
                return HttpResponse('Please enter a valid Plan Id')

            user_amount = int(request.POST.get('amount'))

            print('aya..........')
            order_id = random.randint(1, 999999)
            email_id = user_plus_vendor.EmailID
            name = user_plus_vendor.Company_Name
            address = user_plus_vendor.Address1
            state = user_plus_vendor.state
            city = user_plus_vendor.city
            zip_code = user_plus_vendor.PinCode
            plan_id = plan.plan_id

            # Check if user not provide any discount value

            print(user)
            print(type(user))
            order = Order(name=name, user=user, email_id=email_id, phone=phone, address=address, city=city,
                            state=state, zip_code=zip_code, amount=user_amount,discount=discount, order_id=order_id, plan_id=plan, order_completed=False,role=role)
            order.save()
            print('..................',order)

            # sending details to paytm gateway in form of dict
            detail_dict = {
                "MID": parameters['merchant_id'],
                "WEBSITE": "WEBSTAGING",
                "INDUSTRY_TYPE_ID": "Retail",
                "CUST_ID": str(email_id),
                "CHANNEL_ID": "WEB",
                "ORDER_ID": str(order_id),
                "TXN_AMOUNT": str(user_amount),
                "CALLBACK_URL": f"http://192.168.29.249:8000/api/req_handler",
            }

            param_dict = detail_dict
            CheckSum.generateSignature
            param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                detail_dict, parameters['merchant_key'])
            # print('.................', param_dict)
            return render(request, 'redirect.html', {'detail_dict': param_dict})
        return render(request, 'checkout2.html', {'plan': plan})  # for checkout
    # except Exception as e:
    #     print("An Exception occur \n", e)
    #     return HttpResponse(e)


@csrf_exempt
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        form = request.POST
        print(form["ORDERID"])
        role = {
        'customer': 'customer',
        'vendor': 'vendor',
            }

        # another if to handle if user load refresh
        is_order_exist = Order_Payment.objects.filter(
            order_id=form["ORDERID"]).exists()
        print('............................order', is_order_exist)
        if is_order_exist == False:
            # FOR ALL VALUES
            for i in form.keys():
                response_dict[i] = form[i]
                print(i, form[i])

                if i == "CHECKSUMHASH":
                    response_check_sum = form[i]

            verify = CheckSum.verifySignature(
                response_dict, parameters['merchant_key'], response_check_sum)
            print(verify)
            # response_dict["STATUS"] = "PENDING"
            print('.........response_dict["STATUS"]', response_dict["STATUS"])
            print("..................", verify)
            if verify and response_dict["STATUS"] != "TXN_FAILURE" or response_dict["STATUS"] == "PENDING":
                order_payment = Order_Payment()
                usr = User
                # id = models.AutoField(primary_key = True)
                order = Order.objects.get(order_id=response_dict["ORDERID"])
               

                order_payment.order_summary = order
                # paytm responses
                order_payment.currency = response_dict["CURRENCY"]
                order_payment.gateway_name = response_dict["GATEWAYNAME"]
                # Txn Success
                order_payment.response_message = response_dict["RESPMSG"]
                # order_payment.bank_name = response_dict["BANKNAME"] # WALLET
                # PPI
                order_payment.Payment_mode = response_dict["PAYMENTMODE"]
                # MID = models.CharField(max_length=8) # VdMxPH61970223458566
                order_payment.response_code = response_dict["RESPCODE"]  # 01
                # 20200905111212800110168406201874634
                order_payment.txn_id = response_dict["TXNID"]
                # 2400.00
                order_payment.txn_amount = response_dict["TXNAMOUNT"]
                order_payment.order_id = response_dict["ORDERID"]  # 6556
                order_payment.status = response_dict["STATUS"]  # TXN_SUCCESS
                # 63209779
                order_payment.bank_txn_id = response_dict["BANKTXNID"]
                # 2020-09-05 18:51:59.0
                order_payment.txn_date = response_dict["TXNDATE"]
                # order_payment.refund_amount =  #  0.00
                order_payment.save()
                payment_status = Order_Payment.objects.get(
                    order_id=response_dict["ORDERID"])
                
                print('00.........',order.discount)
                if order.role == 'customer':
                    user = order_payment.order_summary.user
                    user.is_customer_paid =True 
                    user.customer_discount = order.discount
                    user.save()   
                    customer = Customer.objects.filter(user=user).first()
                    customer.subscription_plan_taken = order_payment.order_summary.plan_id
                    customer.save()
                else:
                    user = order_payment.order_summary.user
                    user.is_vendor_paid = True 
                    user.save()   
                    vendor = Vendor.objects.filter(user=user).first()
                    vendor.registration_fee = order_payment.order_summary.plan_id
                    vendor.save()
                print('Order payment..............................',order_payment.order_summary.user)
                print('Order payment..............................',type(order_payment))
              
                return render(request, 'ordersucess.html', {'payment': payment_status})
            else:
                Order.objects.filter(
                    order_id=response_dict["ORDERID"]).delete()
                return HttpResponse('Order is not Placed Because of some error. Please <a href="/sbt/">Try Again </a>')
        else:
            payment_status = Order_Payment.objects.get(
                order_id=form["ORDERID"])
            # Session should create when order is get successfull

            return HttpResponse('Your payment  failed')
    return HttpResponse('Invalid Request')


def pricing_multiplier(request):
    if request.method == "POST":

        amount = int(request.POST.get('amount'))
        try:
            discount = int(request.POST.get('discount'))
        except ValueError:
            return JsonResponse({'discount_applied': '', 'total': '', 'error': 'Expected integer'})
        plan_id = int(request.POST.get('plan_id'))
        response = discount_validation(plan_id, discount, amount)
        # response_dict = json.loads(response.getvalue().decode('utf-8'))
        # print(response_dict)
        return JsonResponse(response)


def order_status(request, slug):
    try:
        obj = Order_Payment.objects.get(order_id=slug)
        obj2 = obj.order_summary
        if obj2.user == request.user:
            paytmParams = dict()

            paytmParams["MID"] = parameters['merchant_id']
            paytmParams["ORDERID"] = slug

            checksum = CheckSum.generateSignature(paytmParams, parameters['merchant_key'])

            paytmParams["CHECKSUMHASH"] = checksum

            post_data = json.dumps(paytmParams)

            # for Staging
            url = "https://securegw-stage.paytm.in/order/status"

            # for Production
            # url = "https://securegw.paytm.in/order/status"

            response = requests.post(url, data=post_data, headers={
                                     "Content-type": "application/json"}).json()
            print(response)

            if response["STATUS"] == "TXN_SUCCESS":
                print("Updating Status")
                obj = Order_Payment.objects.get(order_id=slug)
                obj.status = response["STATUS"]
                obj.response_code = response["RESPCODE"]
                obj.response_message = response["RESPMSG"]
                obj.txn_date = response["TXNDATE"]
                obj.bank_name = response["BANKNAME"]
                obj.save()
                return HttpResponse("order success fully placed")

            return HttpResponse("order is still in pending state")

        elif request.user != None and request.user.is_authenticated:
            return HttpResponse("Please insert correct orderid")
        else:
            return HttpResponse('Please Login <a href="/sbt/login"> Here First</a>')
    except Exception as e:
        return HttpResponse(f"Requested Order Not Found - {e}")  # form to type in order id"""
