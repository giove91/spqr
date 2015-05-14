from django.db import models

from django.contrib.auth.models import User


class Keyword(models.Model):
    GRAMMAR = 'G'
    SUBJECT = 'S'
    TYPE_CHOICES = (
        (GRAMMAR, 'Grammar'),
        (SUBJECT, 'Subject'),
    )

    keyword = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=GRAMMAR)
    
    class Meta:
        ordering = ('type', 'keyword')
    
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


class Result(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    
    num_views = models.IntegerField(default=0)
    num_correct = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Result of %s on %s' % (self.user.username, self.word.russian)



