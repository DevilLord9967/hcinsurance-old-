from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from client.models import Client, Reciept
from policy.models import Client_Policy
from Webone.settings import MEDIA_URL


def index(request):
    reciept = Reciept.objects.order_by('-date').filter(client_name__email=request.user.username)
    policy = Client_Policy.objects.order_by('-id').filter(uname=request.user.username)
    context = {
        'reciept': reciept,
        'policy': policy
    }
    return render(request, 'client/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('client')
        else:
            messages.ERROR(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'client/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out Successfully')
        return redirect('login')
    else:
        return redirect('client')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = fname + ' ' + lname
        DOB = request.POST['dob']
        email = request.POST['email']
        address = request.POST['address']
        mobile1 = request.POST['mobile1']
        mobile2 = request.POST['mobile2']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Policy details

        if User.objects.filter(username=email).exists():
            messages.error(request, 'e-mail is already registered')
            return redirect('register')
        else:
            if (pass1 != pass2):
                messages.error(request, 'Passwords do not match')
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, password=pass1, email=email, first_name=fname,
                                                last_name=lname)
                user.save()
                client = Client.objects.create(name=name, email=email, DOB=DOB, mobile1=mobile1, mobile2=mobile2,
                                               address=address)
                client.save()
                return render(request, 'client/registered.html')
    else:
        return render(request, 'client/register.html')


def addpolicy(request):
    if request.method == 'POST':
        pnum = request.POST['policy_number']
        plnum = request.POST['plan_number']
        mode = request.POST['mode']
        payterm = request.POST['payterm']
        maturity_term = request.POST['maturityterm']
        premium = request.POST['premium']
        DOC = request.POST['doc']
        if Client_Policy.objects.filter(policy_number=pnum).exists():
            messages.error(request, 'Policy number is already registered')
            return redirect('add_policy')
        else:
            policy = Client_Policy.objects.create(policy_number=pnum, plan_number=plnum, mode=mode,
                                                  maturity_term=maturity_term, premium=premium, paying_term=payterm,
                                                  DOC=DOC, uname=request.user.username)
            policy.save()
            messages.success(request, 'Policy added successfully')
            return redirect('add_policy')
    else:
        return render(request, 'client/add_policy.html')


def image(request):
    img = Reciept.objects.all()
    return render(request, 'client/image.html', {"img": img, 'media_url': MEDIA_URL})
