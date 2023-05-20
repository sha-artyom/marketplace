from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(max_length=200, verbose_name="Название")
    email = models.EmailField()
    country = models.CharField(max_length=250, verbose_name="Страна", blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name="Город", blank=True, null=True)
    street = models.CharField(max_length=70, verbose_name="Улица", blank=True, null=True)
    house_number = models.IntegerField(verbose_name="Номер дома", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    model = models.CharField(max_length=150, verbose_name="Модель")
    release_date = models.DateField(auto_now_add=True, verbose_name="Дата выхода продукта на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Factory(BaseModel):
    products = models.ManyToManyField(Product, verbose_name="Продукты")

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.title


class RetailNetwork(BaseModel):
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    provider = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name="Поставщик")
    debt = models.IntegerField(verbose_name="Задолженность")

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return self.title


class PrivateBusinessman(BaseModel):
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    provider = GenericForeignKey('content_type', 'object_id')
    debt = models.IntegerField(verbose_name="Задолженность")

    objects = models.Manager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Частный предприниматель'
        verbose_name_plural = 'Частные предприниматели'

    def __str__(self):
        return self.title
