from django.contrib.auth import get_user_model
from products.models import Product


# to use user model
User = get_user_model
current_user = User.objects.first()
Product.objects.create(user=current_user, title='new product', price=12.34)
current_user.product_set.all() # get all products of current user - Products foreign key

datas = [
  {'title': 'Product 1', 'price': 12.34},
  {'title': 'Product 2', 'price': 54.32},
  {'title': 'Product 3', 'price': 234.56},
]


# obj = Product(title='New Product', price=123.45)
# obj.save()

# new_product = Product.objects.create(title='New Product', price=123.45)

# first_product = datas[0]
# Product(**first_product)

# my_new_objs = []
# for new_data in datas:
#   my_new_objs.append(Product(**new_data))
# Product.objects.bulk_create(my_new_objs, ignore_conflicts=True)

Product.objects.bulk_create(**datas, ignore_conflicts=True)