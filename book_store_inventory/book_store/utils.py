from book_store.models import Category, SubCategory

def get_categories():
    category_list = Category.objects.all() 
    subcategory_dict = {}
    for category in category_list:
        subcategory_list = SubCategory.objects.filter(category=category)
        subcategory_dict[category.slug] = subcategory_list
    return category_list, subcategory_dict