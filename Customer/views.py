from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


from .serializers import CustomerPlanSerializer,CustomerSerializer
from .models import Customer
from website.models import Order,Plan,Order_Payment
from website.validations import *
from django.views.decorators.csrf import csrf_exempt
from website.PayTm import CheckSum


User = get_user_model()

# Create your views here.
class NewCustomerAPI(viewsets.ModelViewSet):
    """
    This API creates new Customer,view and edit using viewsets

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        customer = Customer.objects.filter(customer_name=request.data['customer_name'])
        if customer.exists():
            return Response({'detail':'customer already exists'},status=status.HTTP_306_RESERVED) 
        data = request.data
        user = User.objects.filter(id=request.data['user'])
        print(user)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            for cust in user:
                cust.is_customer_registered = True
                cust.save()
            serializer.save()
            user = User.objects.filter(id=request.data['user']).values()
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
----------------------------------------------Payment Part------------------------------------------------------------

"""

def purchase(request,plan_id):
    # assuming coming from purchase form but for instance taking from purchase button from index.html
    # about paytm implimentation will here
    # discount won't work if empty
    try:
        # if request.user.is_authenticated:
        if request.method == 'POST':
            user_plus_customer = Customer.objects.get(user=request.POST.get('userid'))
            try:
                plan = Plan.object.get(plan_id = plan_id)
            except:
                return HttpResponse('Please enter a valid Plan Id')

            user_discount = request.POST.get('discount')
            if not plan.plan_amount == request.POST.get('amount') and not user_discount >=plan.minimumm_discount  and  not user_discount <= plan.maximum_discount:
                return HttpResponse('Sensitive Error')
            
                plan = Plan.objects.get(plan_name=plan_id) 
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
                    response_dict  = discount_validation(plan_id, discount, plan.plan_amount)
                    if response_dict['error'] != None:
                        return HttpResponse(response_dict['error'])
                    amount = discount * plan.plan_amount
                else:
                    amount = plan.plan_amount

                order = Order(name=name, user = request.user, email_id=email_id, address=address, city=city, state=state, zip_code=zip_code,
                              phone=phone, amount=amount, order_id=order_id, plan_id=plan, order_completed = False)
                order.save()

                # sending details to paytm gateway in form of dict
                detail_dict = {
                    "MID": MID,
                    "WEBSITE": "WEBSTAGING",
                    "INDUSTRY_TYPE_ID": "Retail",
                    "CUST_ID": str(email_id),
                    "CHANNEL_ID": "WEB",
                    "ORDER_ID": str(order_id),
                    "TXN_AMOUNT": str(amount),
                    "CALLBACK_URL": "http://192.168.29.249/:8000/customer/req_handler",
                }

                param_dict = detail_dict
                CheckSum.generateSignature
                param_dict['CHECKSUMHASH'] = CheckSum.generateSignature(
                    detail_dict, MKEY)
                # print('.................', param_dict)
                return render(request, 'redirect.html', {'detail_dict': param_dict})
            dict_for_review = {
                'id' : plan.plan_id,
                'name': plan.plan_name,
                'amount': plan.plan_amount,
                'description_1': plan.description_1,
                'description_2': plan.description_2,
                'description_3': plan.description_3,
                'description_4': plan.description_4,
            }

            return HttpResponse('Either amount or Discount not Matched')
        return render(request, 'test.html')
    except Exception as e:
        print("An Exception occur \n", e)
        return HttpResponse(f"There is an error{e}")
    


@csrf_exempt
def req_handler(request):
    if request.method == 'POST':
        response_dict = dict()
        form = request.POST
        print(form["ORDERID"])

        # another if to handle if user load refresh
        is_order_exist = Order_Payment.objects.filter(order_id = form["ORDERID"]).exists()
        print('............................order', is_order_exist)
        if is_order_exist == False:
            # FOR ALL VALUES
            for i in form.keys():
                response_dict[i] = form[i]
                print(i, form[i])

                if i == "CHECKSUMHASH":
                    response_check_sum = form[i]

            verify = CheckSum.verifySignature(response_dict, MKEY, response_check_sum)
            print(verify)
            # response_dict["STATUS"] = "PENDING"
            print('.........response_dict["STATUS"]', response_dict["STATUS"])
            print("..................", verify)
            if verify and response_dict["STATUS"] != "TXN_FAILURE" or response_dict["STATUS"] == "PENDING":
                order_payment = Order_Payment()
                usr = User
                # id = models.AutoField(primary_key = True)
                order = Order.objects.get(order_id = response_dict["ORDERID"])
                
                order_payment.order_summary = order
                # paytm responses 
                order_payment.currency = response_dict["CURRENCY"]
                order_payment.gateway_name = response_dict["GATEWAYNAME"]
                order_payment.response_message = response_dict["RESPMSG"] # Txn Success
                # order_payment.bank_name = response_dict["BANKNAME"] # WALLET
                order_payment.Payment_mode = response_dict["PAYMENTMODE"]# PPI
                # MID = models.CharField(max_length=8) # VdMxPH61970223458566
                order_payment.response_code = response_dict["RESPCODE"] # 01
                order_payment.txn_id = response_dict["TXNID"]#  20200905111212800110168406201874634
                order_payment.txn_amount = response_dict["TXNAMOUNT"]#  2400.00
                order_payment.order_id = response_dict["ORDERID"]#  6556
                order_payment.status = response_dict["STATUS"]# TXN_SUCCESS
                order_payment.bank_txn_id = response_dict["BANKTXNID"] #  63209779
                order_payment.txn_date = response_dict["TXNDATE"] #  2020-09-05 18:51:59.0
                # order_payment.refund_amount =  #  0.00
                order_payment.save()
                payment_status = Order_Payment.objects.get(order_id = response_dict["ORDERID"])

                return render(request, 'order_success.html', {'payment':payment_status})
            else:
                Order.objects.filter(order_id= response_dict["ORDERID"]).delete()
                return HttpResponse('Order is not Placed Because of some error. Please <a href="/sbt/">Try Again </a>')
        else:
            payment_status = Order_Payment.objects.get(order_id = form["ORDERID"])
            # Session should create when order is get successfull

            return render(request, 'order_success.html', {'payment':payment_status}) 
    return HttpResponse('Invalid Request')

def pricing_multiplier(request):    
    if request.method =="POST":

        amount = int(request.POST.get('amount')) 
        try:
            discount = int(request.POST.get('discount'))
        except ValueError:
            return JsonResponse({'discount_applied':'' ,'total':'', 'error': 'Expected integer'})
        plan_id = int(request.POST.get('plan_id'))
        response = discount_validation(plan_id, discount, amount)
        # response_dict = json.loads(response.getvalue().decode('utf-8'))
        # print(response_dict)
        return JsonResponse(response)

def order_status(request, slug):
    try:
        obj = Order_Payment.objects.get(order_id = slug)
        obj2 = obj.order_summary
        if obj2.user == request.user:            
            paytmParams = dict()

            paytmParams["MID"]     = MID
            paytmParams["ORDERID"] = slug

            checksum = CheckSum.generateSignature(paytmParams, MKEY)

            paytmParams["CHECKSUMHASH"] = checksum

            post_data = json.dumps(paytmParams)

            # for Staging
            url = "https://securegw-stage.paytm.in/order/status"

            # for Production
            # url = "https://securegw.paytm.in/order/status"

            response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
            print(response)

            if response["STATUS"]=="TXN_SUCCESS":
                print("Updating Status")
                obj = Order_Payment.objects.get(order_id = slug)
                obj.status = response["STATUS"]
                obj.response_code = response["RESPCODE"]
                obj.response_message = response["RESPMSG"]
                obj.txn_date = response["TXNDATE"]
                obj.bank_name = response["BANKNAME"]
                obj.save()
                return HttpResponse("order success fully placed")

            return HttpResponse("order is still in pending state")
        
        elif request.user!=None and request.user.is_authenticated :
            return HttpResponse("Please insert correct orderid")
        else:
            return HttpResponse('Please Login <a href="/sbt/login"> Here First</a>')
    except Exception as e:
        return HttpResponse(f"Requested Order Not Found - {e}") # form to type in order id"""
