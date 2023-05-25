from config.payme import Payme
from django.shortcuts import render, redirect
from django.contrib import messages
from register.models import Person, BalanceHistoryModel
from django.contrib.auth.decorators import login_required
import os, binascii, datetime 




def check_deposit(request):
    user = request.user.id
    today = datetime.date.today()
    histories = BalanceHistoryModel.objects.filter(user=user, time__year=today.year, time__month=today.month, time__day=today.day)
    for history in histories:
        if history.payment == 'payme' and history.status == 'waiting':
            payment = Payme('63d242b9f9b3d2b5a85e015b')
            check = payment.info(history.check_id)
            if check['ok']:
                if check['payment'] == 'successfully':
                    edit = BalanceHistoryModel.objects.get(pk=history.pk)
                    edit.status = 'completed'
                    edit.save()
                    person = Person.objects.get(user=user)
                    person.balance += edit.amount
                    person.save()
                    messages.success(request, f"Your balance has been increased by {edit.amount} UZS", "Success: Payment")
            else:
                edit = BalanceHistoryModel.objects.get(pk=history.pk)
                edit.status = 'cancelled'
                edit.save()
                
    
def arender(request, template_name, content={}):
    check_deposit(request)
    person = Person.objects.get(user=request.user)
    current_datetime = datetime.datetime.now()
    content['person'] = person
    content['now'] = current_datetime
    return render(request, template_name, content)
    

@login_required(login_url='login')
def Dashboard(request):
    return arender(request, 'hosting/index.html')

@login_required(login_url='login')
def Deposit(request):
    if request.method == "POST":
        summ = request.POST.get('summ', 5000)
        type = request.POST.get('payment_type', 'payme')
        if type == 'payme' and summ:
            if int(summ) >= 1000:
                s = Payme('62f3d1efcad1c751635a3548')
                result = s.create(int(summ), f'ID: #{request.user.id}')
                if result["ok"]:
                    url = result['result']['pay_url']
                    BalanceHistoryModel.objects.create(user=request.user, payment=type, amount=summ, check_id=result['result']['id'])
                    return redirect(url)
                else:
                    messages.error(request, result['error'], 'Error: Payme')
            else:
                messages.error(request, "Minimal: 1000 UZS")
        else:
            messages.warning(request, "This payment system is under development", "Payment type")
    
    return arender(request, 'hosting/deposit.html')
    
@login_required(login_url='login')
def BalanceHistory(request):
    historys = BalanceHistoryModel.objects.filter(user=request.user).order_by("-id")
    return arender(request, 'hosting/balance_history.html', {'historys': historys})


def Site(request, site):
    return arender(request, "hosting/others/"+site)