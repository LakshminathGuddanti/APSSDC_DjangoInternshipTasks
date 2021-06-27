from django.http.response import HttpResponse
from django.shortcuts import render


users = {}
# Create your views here.
def home(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        password = request.POST.get('password')
        address = request.POST.get('address')
        check1 = request.POST.getlist('check1')
        print(request.POST)
        print(check1)
        exampleRadios = request.POST.get('exampleRadios')
        users[email]=password
        print(users)
        context = {
            'fname':fname,
            'lname':lname,
            'email':email,
            'phoneno':phoneno,
            'radio':exampleRadios,
            'address':address,
            'check1':check1,
            'password':password
        }
        return render(request,'init/details.html',context)
    return render(request,"init/index.html")

def loginForm(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        if users[email] == password:
            print("pass")
            return HttpResponse("<p>You are successfully Logged In</p>")
    context={}
    return render(request,'init/loginform.html',context)
