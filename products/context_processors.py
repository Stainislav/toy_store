from .models import Category

def categories_processor(request):

    parent_categories = Category.objects.filter(parent=None, is_active=True)
            
    return locals()
