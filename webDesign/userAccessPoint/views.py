from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request, 'uap/base.html')