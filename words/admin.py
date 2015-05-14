from django.contrib import admin
from words.models import Keyword, Word, Result


class WordAdmin(admin.ModelAdmin):
    fields = ['russian', 'italian', 'keywords']
    filter_horizontal = ('keywords',)
    
    list_display = ('russian', 'italian')
    list_filter = ('keywords', )
    search_fields = ['russian', 'italian']

class KeywordAdmin(admin.ModelAdmin):
    fields = ['keyword', 'type']
    
    list_display = ('keyword', 'type')
    search_fields = ['keyword']
    list_filter = ('type',)

class ResultAdmin(admin.ModelAdmin):
    fields = ['user', 'word', 'num_views', 'num_correct']
    
    list_display = ('__unicode__', 'user', 'word', 'num_views', 'num_correct')
    search_fields = ['user__username', 'word__russian', 'word__italian']
    list_filter = ('user',)


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Result, ResultAdmin)
