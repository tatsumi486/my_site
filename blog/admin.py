from django.contrib import admin

# Register your models here.
from .models import BlogPost, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_filter= ("author","tags","date",) #filter on the right
    list_display = ("title","date","author",) #the columns we see
    prepopulated_fields={"slug":("title",)}

admin.site.register(BlogPost,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
