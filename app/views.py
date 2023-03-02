from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
import json
from jugaad_data.nse import NSELive
from .serializer import CallbackRequestSerializer
from rest_framework.generics import CreateAPIView
from .models import Requestcallback
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage
import csv
    


def Home(request):
    return render(request, 'index.html')


def contactUs(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'service.html')

def webinar(request):
    return render(request, 'webinar.html')


def aboutUs(request):
    return render(request, "about.html")



@api_view(['GET'])
def liveData(request):
    n = NSELive()

    data={'nifty50':{},'banknifty':{}}
    nifty_bank = n.live_index("NIFTY BANK") 
    nifty_50 = n.live_index("NIFTY 50")

    data['nifty50'] = nifty_50['data']
    data['banknifty'] = nifty_bank['data']

    context = {'data':data}

    return Response(context)
    # return render(request, 'nifty_50.html',context)



# def live(request):
#     print("in live mode")
#     n = NSELive()
#     all_indices = n.all_indices()
#     indices_data = all_indices['data']
#     while True:
#         for idx in indices_data:
#             if idx['index'] == 'NIFTY 50' or idx['index'] == 'NIFTY BANK':
#                 value = str(("{} - {}".format(idx['index'], idx['last'])))
#                 context={'value':value}
#                 print("{} - {}".format(idx['index'], idx['last']))

#                 return render(request, 'index.html',context)

#         return render(request, 'index.html')


class callback_Request(CreateAPIView):  
    queryset = Requestcallback.objects.all()
    serializer_class = CallbackRequestSerializer


def exportcsv(request):
    students = Requestcallback.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=request-callback.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Full Name', 'Email', 'Phone Number'])
    studs = students.values_list('id','full_name', 'email', 'phone_number')
    for std in studs:
        writer.writerow(std)
    return response

