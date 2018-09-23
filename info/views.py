from django.shortcuts import render
from info.models import InfoPage
from products.models import Category


def about(request):
    
    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")

    text = InfoPage.objects.filter(name="О нас")

    return render(request, "blank.html", locals())


def delivery(request):

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")
    text = InfoPage.objects.filter(name="условия доставки")

    return render(request, "blank.html", locals())


def adress(request):

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")

    text = InfoPage.objects.filter(name="адрес")

    return render(request, "blank.html", locals())



def refund(request):

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")

    text = InfoPage.objects.filter(name="возврат")

    return render(request, "blank.html", locals())
