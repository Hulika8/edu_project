from django.contrib import admin
from .models import Course, Category, Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} #slug alanını name alanına göre otomatik doldurur.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

