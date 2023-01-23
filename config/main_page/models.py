from django.db import models


class ApartmentInfo(models.Model):
    title = models.CharField(max_length=500)                                # Заголовок объявления
    content = models.TextField(max_length=500, null=True, blank=True)       # Описание квартиры
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)
    address = models.CharField(max_length=100, null=True, blank=True)       # Адрес сдаваемой квартиры
    apartment_area = models.FloatField(max_length=30)                       # Площадь Квартиры
    price = models.FloatField(max_length=30, null=True, blank=True)         # Цена в месяц
    contact = models.IntegerField()                                         # Номер для связи с арендадателем
    published = models.DateTimeField(auto_now_add=True, db_index=True)      # Дата публикации
