from django.contrib import admin
from .models import Title
from .models import Tag
from .models import Title_tag
from .models import Volume
from .models import Chapter
from .models import TitleAdmin
from .models import VolumeAdmin

@admin.register(Tag)
@admin.register(Title_tag)
#@admin.register(Volume)
@admin.register(Chapter)
#@admin.register(Title)
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Volume,VolumeAdmin)
admin.site.register(Title,TitleAdmin)