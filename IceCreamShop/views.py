from django.shortcuts import render

def home_page(request):
    # return HttpResponse("this is home page.")
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")

def services_page(request):
    return render(request, "services.html")
