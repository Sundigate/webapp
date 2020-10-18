from django.db import models


class PublicationsTable(models.Model):
    name = models.CharField('Публикация', max_length=20)
    source = models.CharField('Источник', max_length=50)
    publicationType = models.CharField('Тип публикации', max_length=20)
    number_of_pages = models.IntegerField('Число страниц')
    author_id = models.IntegerField('ID автора')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Публикация'
        verbose_name_plural='Публикации'


class AuthorsTable(models.Model):
    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    patronymic =  models.CharField('Отчество', max_length=20)
    rank = models.CharField('Звание', max_length=15)
    date_of_birth = models.DateTimeField('Дата рождения')

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'