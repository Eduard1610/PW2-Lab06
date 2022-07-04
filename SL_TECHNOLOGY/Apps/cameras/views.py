from django.shortcuts import render

# Create your views here.
def cameras(request):
    return render(request,'cameras.html')
