from django.contrib import admin
from .models import DishCategory, Dish, About, Service, Galerys, Reservation, Events

# Register your models here.

# admin.site.register(Dish)
#admin.site.register(About)
#admin.site.register(Service)
#admin.site.register(Galerys)
#admin.site.register(Reservation)
admin.site.register(Events)

# @admin.register(Dish)
# class DishAdmin(admin.ModelAdmin):
# 	list_display = ['title', 'position', 'is_visible', 'category', 'is_special', 'is_signature', 'is_recomendet', 'price', 'discount', 'ingradients', 'photo']
# 	list_filter = ['is_visible', 'is_special', 'is_signature', 'category']
# 	list_editable = ['position', 'is_visible', 'category', 'is_special', 'is_signature', 'is_recomendet', 'price', 'discount', 'ingradients', 'photo']
# @admin.register(DishCategory)
# class DishCategoryAdmin(admin.ModelAdmin):
# 	list_display = ['title', 'position', 'is_visible']
# 	list_filter = ['is_visible']
# 	list_editable = ['position', 'is_visible']
#
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
	list_display = ['title', 'position', 'is_visible', 'category', 'is_special', 'is_signature', 'is_recomendet', 'price', 'discount', 'ingradients', 'photo']
	list_filter = ['is_visible', 'is_special', 'is_signature', 'category']
	list_editable = ['position', 'is_visible', 'category', 'is_special', 'is_signature', 'is_recomendet', 'price', 'discount', 'ingradients', 'photo']

class DishInlane(admin.TabularInline):
	model = Dish
@admin.register(DishCategory)
class CategoryWithDishesAdmin(admin.ModelAdmin):
	list_display = ['title', 'position', 'is_visible']
	list_filter = ['is_visible']
	list_editable = ['position', 'is_visible']
	inlines = [DishInlane]

@admin.register(About)
class Abouty(admin.ModelAdmin):
	list_display = ['title', 'body', 'is_visible']
	list_filter = ['is_visible']
	list_editable = ['body', 'is_visible']

@admin.register(Galerys)
class Galery(admin.ModelAdmin):
	list_display = ['photo', 'is_visible']
	list_filter = ['is_visible']
	list_editable = ['is_visible']

@admin.register(Service)
class Servicy(admin.ModelAdmin):
	list_display = ['title', 'position', 'is_visible']
	list_filter = ['is_visible']
	list_editable = ['position', 'is_visible']

@admin.register(Reservation)
class Reservat(admin.ModelAdmin):
	list_display = ['name', 'phone', 'visit_date', 'visit_time', 'is_processed']
	list_filter = ['is_processed', 'visit_date', 'name']
	list_editable = ['phone', 'visit_date', 'visit_time', 'is_processed']