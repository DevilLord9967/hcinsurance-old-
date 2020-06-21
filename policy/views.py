from django.shortcuts import render
from .models import Policy
def index(request, policy_id):
    plist = Policy.objects.all()
    context={
        'pid':policy_id,
        'policylist':plist
    }
    return render(request,'policy/index.html',context)