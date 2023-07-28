from django.core.validators import MinValueValidator
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name='نام برند')
    brand_nationality = models.CharField(max_length=50, verbose_name='ملیت برند')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='برند')
    model = models.CharField(max_length=100, unique=True, verbose_name='مدل')
    price = models.PositiveIntegerField(verbose_name='قیمت')  # models.IntegerField(validators=[MinValueValidator(0)])
    color = models.CharField(max_length=20, verbose_name='رنگ')  # In this field we could also add >> choices = [('red', 'قرمز'), ('blue', 'آبی')]
    screen_size = models.FloatField(validators=[MinValueValidator(0)], verbose_name='اندازه صفحه نمایش')
    is_available = models.BooleanField(default=True, verbose_name='وضعیت موجودی')
    manufacturing_country = models.CharField(max_length=50, verbose_name='کشور سازنده')
    date_added = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ اضافه شدن')
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True, verbose_name='نام در لینک')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'تلفن همراه'
        verbose_name_plural = 'تلفن های همراه'

    def save(self, *args, **kwargs):
        if not self.slug:
            if not Phone.objects.filter(slug=slugify(self.model)).exists():
                self.slug = slugify(self.model)
            else:
                self.slug = slugify(self.model) + '-' + get_random_string(5)
        super().save(*args, **kwargs)
