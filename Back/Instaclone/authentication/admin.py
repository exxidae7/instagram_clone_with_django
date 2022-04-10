from django.contrib import admin
from .models import Post , User
# Register your models here.

admin.site.register(Post)
admin.site.register(User)


admin.site.site_header = "Instagram clone"
