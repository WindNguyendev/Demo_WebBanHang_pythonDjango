from django.contrib import admin
from .models import Category, Product,Product_Featured,Distributor

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	"""docstring for BlogAdmin"""
	list_display = ('title','quantity_stock','price','active',)
	list_filter = ('category',)
	search_fields = ('title',)


	def get_ordering(self, request):

		if request.user.is_superuser:
			return('title','category','active')
		return('name',)
admin.site.register(Category)
admin.site.register(Product,BlogAdmin)
admin.site.register(Product_Featured)
admin.site.register(Distributor)



