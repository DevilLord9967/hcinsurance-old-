from django.shortcuts import render
from policy.models import Policy
from django.core.paginator import Paginator


def index(request):
    plist = Policy.objects.all().order_by('-name')
    paginator=Paginator(plist,6)
    page=request.GET.get('page')
    plist= paginator.get_page(page)

    context = {
        'policylist': plist
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')
