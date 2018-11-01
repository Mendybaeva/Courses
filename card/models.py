from django.db import models

CONTACT_CHOICES = (
    (1, 'Телефон'),
    (2, 'Facebook'),
    (3, 'e-mail'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    imgpath = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "{}".format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    logo = models.CharField(max_length=100, verbose_name='Логотип')
    category = models.ForeignKey(Category, null=True, related_name='category',
                                 on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return "{}".format(self.name)


class Branch(models.Model):
    latitude = models.CharField(max_length=100, verbose_name='Ширина')
    longitude = models.CharField(max_length=100, verbose_name='Долгота')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Географические данные'
        verbose_name_plural = 'Географические данные'

    def __unicode__(self):
        return self.address


class Contact(models.Model):
    type = models.IntegerField(choices=CONTACT_CHOICES, default=1, verbose_name='Варианты')
    value = models.CharField(max_length=100, verbose_name='Значение')
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Контактные данные'
        verbose_name = 'Контактные данные'

    def __unicode__(self):
        return self.type
