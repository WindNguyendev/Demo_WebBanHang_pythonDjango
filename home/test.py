
from .models import Category, Product

i = Category.objects.all()

for a in i:
    print(a.title)