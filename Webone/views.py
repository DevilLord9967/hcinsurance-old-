from django.shortcuts import render

def temp(req):
    return render(req,'temp.html')