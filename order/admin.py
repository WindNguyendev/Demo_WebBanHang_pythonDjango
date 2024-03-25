from django.contrib import admin
from .models import Order,Order_item

# Regisadmin.ModelAdimnur models here.
# class BlogAdmin(admin.ModelAdmin):
# 	"""docstring for BlogAdmin"""
# 	list_display = ('name','name_pr','quantity','total','created_at','is_status','is_completed')
# 	list_filter = ('is_completed',)
# 	search_fields = ('name_pr',)
# 	actions = ('set_status',)
# 	date_hierarchy = 'created_at'

# 	def get_ordering(self, request):

# 		if request.user.is_superuser:
# 			return('name','name_pr','-created_at')
# 		return('name',)
# 	def set_status(self, request, queryset):
# 		queryset.update(is_completed=True)



admin.site.register(Order)
admin.site.register(Order_item)