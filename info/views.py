from django.shortcuts import render
from info.models import InfoPage


def about(request):

    text = InfoPage.objects.filter(name="О нас")

    return render(request, "blank.html", locals())


def delivery(request):

    text = InfoPage.objects.filter(name="условия доставки")

    return render(request, "blank.html", locals())


def adress(request):

    text = InfoPage.objects.filter(name="адрес")

    return render(request, "blank.html", locals())



def refund(request):

    text = InfoPage.objects.filter(name="возврат")

    return render(request, "blank.html", locals())
