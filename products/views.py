from django.shortcuts import render
from products.models import Product, ProductImage, Category


def home(request):

    # Choose images for active products only.
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")
    latex_balls    = Category.objects.filter(name="Латексные шары")
    foil_balls     = Category.objects.filter(name="Фольгированные шары")

    # Images to show.
    stuffed_toys_images       = product_images.filter(product__category__parent__name="Мягкие игрушки")
    boy_toys_images           = product_images.filter(product__category__parent__name="Игрушки для мальчиков")
    girl_toys_images          = product_images.filter(product__category__parent__name="Игрушки для девочек")
    special_for_you_images    = product_images.filter(product__special_for_you=True)    

    return render(request, "home.html", locals())


def products(request, category_id):

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")
    latex_balls    = Category.objects.filter(name="Латексные шары")
    foil_balls     = Category.objects.filter(name="Фольгированные шары")

    # Get product by ID.   
    category = Category.objects.get(id=category_id)
   
    # Choose images for active products only.
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)

    # Images at the down of a product page.
    images_to_show = products_images.filter(product__category__id=category_id)
   
    return render(request, "products.html", locals())


def product(request, product_id):

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")
    latex_balls    = Category.objects.filter(name="Латексные шары")
    foil_balls     = Category.objects.filter(name="Фольгированные шары")

    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()

    return render(request, 'product.html', locals())


def upper_first_char(word):
    # Get the first chararcter of a word.
    first_word = word[0].upper()
 
    word_list = []

    # Copy word to a list.
    for i in word:
        word_list.append(i)

    # Delete first character of a word.
    word_list.pop(0)

    word_string = ''
    
    # Copy list to a word string.
    for i in word_list:
        word_string = word_string + i

    # Add a first upper character to the whole other string.
    word = first_word + word_string

    return word

def search(request):
    
    data = request.POST
    product_name  = data.get("product_name")

    product_name = upper_first_char(product_name)   

    products_images = ProductImage.objects.filter(is_active=True, is_main=True)    
    images_to_show = products_images.filter(product__name__icontains=product_name)

    return render(request, "products.html", locals())

