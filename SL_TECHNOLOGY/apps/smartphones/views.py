from django.shortcuts import render

# Create your views here.
def smartphones(request):
    return render(request,'smartphones.html')