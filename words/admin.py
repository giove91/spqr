from django.contrib import admin
from words.models import Keyword, Word


class WordAdmin(admin.ModelAdmin):
    fields = ['russian', 'italian', 'keywords']
    filter_horizontal = ('keywords',)
    list_display = ('russian', 'italian')
    search_fields = ['russian', 'italian']



admin.site.register(Keyword)
admin.site.register(Word, WordAdmin)
