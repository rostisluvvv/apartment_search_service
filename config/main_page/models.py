from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    def __str__(self):
        return self.name


class ApartmentInfo(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')                                     # Заголовок объявления
    content = models.TextField(max_length=500, null=True, blank=True)                                     # Описание квартиры
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='Адрес')               # Адрес сдаваемой квартиры
    apartment_area = models.FloatField(max_length=30, verbose_name='Площадь')                             # Площадь Квартиры
    price = models.FloatField(max_length=30, null=True, blank=True)                                       # Цена в месяц
    contact = models.IntegerField(verbose_name='Контакты')                                                # Номер для связи с арендадателем
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата Публикации')    # Дата публикации
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name = 'Категория')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']