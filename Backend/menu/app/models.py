from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name')
    slug = models.SlugField(max_length=64, verbose_name='Slug')
    ingredients = models.TextField(verbose_name='Ingredients')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(verbose_name='Photo', upload_to='menu_img', default='default_png')
    category = models.ForeignKey('Category', verbose_name="Category", related_name='cat', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="Name")
    slug = models.SlugField(max_length=32, verbose_name='Slug')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name