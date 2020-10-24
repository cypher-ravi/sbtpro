import json
import random

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from website.models import Order, Order_Payment, Plan
from website.PayTm import CheckSum
from website.validations import *
from rest_framework import generics,mixins

from .models import Customer
from .serializers import CustomerPlanSerializer, CustomerSerializer

User = get_user_model()

with open('config.json', mode='r') as file:
    parameters = json.load(file)

print(parameters['key'])

# Create your views here.


class NewCustomerAPI(viewsets.ModelViewSet):
    """
    This API creates new Customer,view and edit using viewsets

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        create customer  by User ID
        """
        customer = Customer.objects.filter(
            user=request.data['user'])
        if customer.exists():
            return Response({'detail': 'customer already exists'}, status=status.HTTP_306_RESERVED)
        data = request.data
        user = User.objects.filter(id=request.data['user'])
        for i in user:
            if i.is_customer_registered == True:
                return Response('this user already a customer')
        print(user)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            for cust in user:
                cust.is_customer_registered = True
                cust.save()
            serializer.save(customer_is_active=True)
            user = User.objects.filter(id=request.data['user']).values()
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        """
        Update customer by user id
        """

        customer = Customer.objects.filter(
            user=request.data['user']).first()
        if customer != None:
            partial = kwargs.pop('partial', False)
            instance = customer
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response({'details':'updated'})

        


class CustomerDetail(generics.GenericAPIView):
    """
    Customer Detail By user ID

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        customer = Customer.objects.filter(user=pk)
        print(customer)
        if customer.exists():
            key = parameters['key']
            if slug == key:   
                serializer = CustomerSerializer(customer[0],many=False)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':'user not exists'})
        




        

"""
----------------------------------------------Payment Part------------------------------------------------------------

"""


def purchase(request, plan_id, user):
    if request.method == 'GET':
        customer_user = Customer.objects.filter(user=user).first()
        print(customer_user)
        plan = Plan.objects.filter(plan_id=plan_id)
        print(plan)
        discount = 10
        total = discount * plan[0].plan_amount
        if plan != None:
            if customer_user != None:
                return render(request, 'checkout2.html', {'plan': plan[0], 'customer': customer_user, 'total': total})
            else:
                return HttpResponse('invalid customer')
        else:
            return HttpResponse('Invalid plan and user')


def customer_card_purchase(request, plan_id, id, user):
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    # discount won't work if empty
        # if request.user.is_authenticated:
    if request.method == 'POST':
            # customer = 4
        plan_id = 1
        user_plus_customer = Customer.objects.get(customer_id=id)
        user = User.objects.filter(id=user).first()
        phone = user.phone

        print(user_plus_customer)
        try:
            plan = Plan.objects.get(plan_id=plan_id)
        except:
            return HttpResponse('Please enter a valid Plan Id')
        print('..............', request.POST.get('discount'))
        user_discount = int(request.POST.get('discount'))
        # user_amount = int(request.POST.get('amount'))#configure not done
        user_amount = 100
        if plan.plan_amount == user_amount and user_discount >= plan.minimum_discount and user_discount <= plan.maximum_discount:

            order_id = random.randint(1, 999999)
            email_id = user_plus_customer.EmailID
            name = user_plus_customer.customer_name
            address = user_plus_customer.Address
            state = user_plus_customer.state
            city = user_plus_customer.city
            zip_code = user_plus_customer.zipcode
            plan_id = plan.plan_id

            try:
                discount = int(request.POST.get('discount'))
            except ValueError:
                return HttpResponse('Please select a valid discount value')

            # Check if user not provide any discount value
            if discount != "" and discount != None:
                response_dict = discount_validation(
                    plan_id, discount, plan.plan_amount)
                if response_dict['error'] != None:
                    return HttpResponse(response_dict['error'])
                amount = discount * plan.plan_amount
            else:
                amount = plan.plan_amount

            order = Order(name=name, user=request.user, email_id=email_id, phone=phone, address=address, city=city,
                          state=state, zip_code=zip_code, amount=amount, order_id=order_id, plan_id=plan, order_completed=False)
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
                "CALLBACK_URL": "http://192.168.29.249:8000/customer/req_handler",
            }

            param_dict = detail_dict
            CheckSum.generateSignature
            param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                detail_dict, parameters['merchant_key'])
            # print('.................', param_dict)
            return render(request, 'redirect.html', {'detail_dict': param_dict})

        return HttpResponse('Either amount or Discount not Matched')
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

                return render(request, 'ordersucess.html', {'payment': payment_status})
            else:
                Order.objects.filter(
                    order_id=response_dict["ORDERID"]).delete()
                return HttpResponse('Order is not Placed Because of some error. Please <a href="/sbt/">Try Again </a>')
        else:
            payment_status = Order_Payment.objects.get(
                order_id=form["ORDERID"])
            # Session should create when order is get successfull

            return render(request, 'ordersucess.html', {'payment': payment_status})
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

            paytmParams["MID"] = MID
            paytmParams["ORDERID"] = slug

            checksum = CheckSum.generateSignature(paytmParams, MKEY)

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
