from django.contrib import admin
from .models import Story
from .models import Blog
from .models import Image

# Register your models here.
admin.site.register(Story)
admin.site.register(Blog)
admin.site.register(Image)