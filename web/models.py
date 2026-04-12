from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    profession = models.CharField(max_length=50, verbose_name='Профессия')
    about = models.TextField(max_length=2000, verbose_name='Краткое описание')


