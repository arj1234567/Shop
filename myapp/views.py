from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages
from django.http import JsonResponse
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def registerAction(request):
    name = request.POST['name']
    age = request.POST['age']
    phone = request.POST['phone']
    address = request.POST['address']
    gender = request.POST['gender']
    username = request.POST['username']
    password = request.POST['password']
    user = register_tb(Name=name,Age=age,phone_no=phone,Address=address,Gender=gender,Username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,'Registration was succesfull....')
    return redirect('register')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = register_tb.objects.filter(Username = username,password = password)
    if user.count()>0:
        messages.add_message(request,messages.INFO,'Login Succesfull..')
        request.session['userid'] = user[0].id
        return render(request,'userhome.html')
    else:
        messages.add_message(request,messages.INFO,'Login Failed')
        return redirect('login')
    
def viewuser(request):
    user = register_tb.objects.all()
    return render(request,'viewuser.html',{'us':user})
def deleteUser(request,id):
    user = register_tb.objects.filter(id=id).delete()
    return redirect('viewuser')
def editUser(request,id):
    user = register_tb.objects.filter(id=id)
    return render(request,'editUser.html',{'us':user})
def editAction(request):
    id =request.POST['id']
    name = request.POST['name']
    age = request.POST['age']
    phone = request.POST['phone']
    address = request.POST['address']
    gender = request.POST['gender']
    username = request.POST['username']
    password = request.POST['password']
    user = register_tb.objects.filter(id=id).update(Name =name,Age=age,phone_no =phone,Address =address,Gender =gender,Username =username,password=password)
    return redirect('viewuser')
def images(request):
    return render(request,'images.html')
def uploadAction(request):
    if len(request.FILES)>0:
        img = request.FILES['images']
    else:
        img ="no file"
    image =image_tb(image =img)
    image.save()
    return redirect('images')
def viewimages(request):
    images  = image_tb.objects.all()
    return render(request,'viewimages.html',{'img': images})
def viewcity(request):
    city = city_tb.objects.all()
    return render(request,'viewcity.html',{'cit': city})
def getplace(request):
    city=request.GET['c']
    place=place_tb.objects.filter(cid_id=city)
    return render(request,'getplace.html',{'pl':place})
def mouseEvent(request):
    return render(request,'mouseEvent.html')

def getuser(request):
    user=request.GET['us']
    data=register_tb.objects.filter(Username=user)
    if len(data)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})

# Create your views here.
