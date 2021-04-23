from django.db import models
from django.urls import reverse

class Tag(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)  # from above table/class
    image = models.ImageField(default='', blank=True, upload_to='images')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Flower, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])