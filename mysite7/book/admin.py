from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'price', 'publish',)
    list_display_links = ('title',)


admin.site.register(Book, BookAdmin)
# linda/pwd:linda123
