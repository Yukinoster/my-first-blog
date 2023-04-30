from django.contrib import admin
###以下追加###
from .models import Post

admin.site.register(Post)
# Register your models here.
