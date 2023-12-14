from django.contrib import admin
from .models import Arctik


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'short_text')

    def short_text(self, obj):
        return obj.text[:20] + '...' if len(obj.text) > 20 else obj.text

    short_text.short_description = 'Short Text'



