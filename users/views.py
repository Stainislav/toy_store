from users.models import User
from django.shortcuts import render


def sign_up(request):
    
    return render(request, 'sign_up.html', locals())

