from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse
import json



def index(resquest):
    return HttpResponse ("This is the animals site")


def show_json(request):

    json_data = open('/animals.json')   
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(data1) # json formatted string

    json_data.close()

    return request



# Create your views here.
