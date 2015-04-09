from django.contrib import admin
from words.models import Keyword, Word


class WordAdmin(admin.ModelAdmin):
    fields = ['russian', 'italian', 'keywords']
    filter_horizontal = ('keywords',)
    
    list_display = ('russian', 'italian')
    search_fields = ['russian', 'italian']

class KeywordAdmin(admin.ModelAdmin):
    fields = ['keyword', 'type']
    
    list_display = ('keyword', 'type')
    search_fields = ['keyword']
    list_filter = ('type',)


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Word, WordAdmin)
