from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    profession = models.CharField(max_length=50, verbose_name='Профессия')
    about = models.TextField(max_length=2000, verbose_name='Краткое описание')


class SocialLinks(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    link = models.URLField(max_length=500, unique=True)
    profile = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                verbose_name='Профиль', related_name='links')


class Education(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    speciality = models.CharField(max_length=100, verbose_name='Специальность')
    admission_year = models.IntegerField(verbose_name='Год поступления')
    graduation_year = models.IntegerField(verbose_name='Год окончания')
    description = models.TextField(max_length=2000, verbose_name='Описание')
