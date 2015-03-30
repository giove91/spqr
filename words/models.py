from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=128, unique=True)
    
    class Meta:
        ordering = ('keyword',)
    
    def __unicode__(self):
        return u'%s' % self.keyword


class Word(models.Model):
    russian = models.CharField(max_length=128, unique=True)
    italian = models.CharField(max_length=128)
    
    keywords = models.ManyToManyField(Keyword, blank=True)
    
    class Meta:
        ordering = ('russian', 'italian')
    
    def __unicode__(self):
        return u'%s' % self.russian

