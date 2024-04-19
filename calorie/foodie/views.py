from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from. models import message
import requests
import json

# Create your views here.


def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers = {'X-Api-Key': 'VUerTln93pt2/+TnIKoUPQ==M8dzugt2UdkaXtxG'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
    

def room(request):
    if request.method == 'POST':
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url, headers= {'X-Api-Key': 'VUerTln93pt2/+TnIKoUPQ==M8dzugt2UdkaXtxG'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})

def loginPage(request):
    page = 'login'
    if request.user.is_authentic:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user: User.objects.get(email=email)
        except:
            message.error(request, "User does not exist")
            
        User: authenticate(request, email= email, password= password)

        if user is not None:
            login(request,User)
            return redirect('home')
        
        else:
            message.error(request, "You have just enter a wrong username or password")
    context = {'page': page}


def logout(request):
    if User.is_valid:
        return (request, 'home.html')




    

# def loginPage(request):
#     page = 'login'
#     if request.user.is_authentic:
#         return redirect('home')

#     if request.method == 'POST':
#         email = request.POST.get('email').lower()
#         password = request.POST.get('password')

#         try:
#             user: User.objects.get(email= email)
#         except:
#             message.error(request, "User does not exist")

#         User: authenticate(request, email= email, password= password)

#         if user is not None:
#             login(request, User)
#             return redirect('home')
           
#         else:
#             message.error(request, "You have just entered either wrong username or password")
#     context = {'page': page}