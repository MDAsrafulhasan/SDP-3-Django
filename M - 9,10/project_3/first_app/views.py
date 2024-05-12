from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    d = {'name' : 'soumick', 
         'age' : 14, 
         'lst':['c++','java','python'] , 
         'birthday' : datetime.datetime.now(),
         'courses' : [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 10000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 2000
        },
        {
            'id' : 3,
            'name' : 'java',
            'fee' : 30000
        },
    ]}
    return render(request,'home.html',d)

def login(request):
    return HttpResponse("Login karo mere dil me")