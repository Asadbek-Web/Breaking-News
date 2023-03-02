from django.contrib import admin
from .models import News, Category, Contact

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publish_time', 'status']
    list_filter = ['category', 'status', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}    # slug ni o'zi avtomatik tarzda yozib ketadi
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
