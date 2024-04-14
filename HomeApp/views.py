from django.shortcuts import render

def ViewHomePage(request):
    return render(request, 'HomeApp/Index.html')
