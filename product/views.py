from django.shortcuts import render

def index(request):
    context = {
        "var": "Stanislav"
    }
    return render(request, "index.html", context)
    
