from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=128)
    
    def __unicode__(self):
        return u'%s' % self.keyword


class Word(models.Model):
    russian = models.CharField(max_length=128)
    italian = models.CharField(max_length=128)
    
    keywords = models.ManyToManyField(Keyword, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.russian

