from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def lunch(requst):
    menu_list = ['한식', '양식', '중식', '일식', '금식']
    pick = random.choice(menu_list)
    
    return render(requst, 'lunch.html', {'pick':pick})
    
def lotto(request):
    magic_number = random.sample(range(1, 46), 6)
    #num = ','.join(magic_number)
    return render(request, 'lotto.html', {'magic_number':magic_number})
    
def hello(request, name):
    return render(request, 'hello.html', {'name' : name })
    
def cube(request, num):
    three = num ** 3
    return render(request, 'cube.html', {'three' : three})
    