from django.db import models
from django.urls import reverse


# Category 모델
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, db_index=True,
                unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    #def get_absolute_url(self):  #product 페이지 경로
        #return reverse()

