from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    profession = models.CharField(max_length=50, verbose_name='Профессия')
    about = models.TextField(max_length=2000, verbose_name='Краткое описание')
    avatar = models.URLField(max_length=255, blank=True, verbose_name='Аватар')


class Contacts(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='contacts')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    address = models.CharField(max_length=255, verbose_name='Аддрес')


class SocialLinks(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    link = models.URLField(max_length=500, unique=True)
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                verbose_name='Профиль', related_name='links')


class Education(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='educations')
    name = models.CharField(max_length=255, verbose_name='Название')
    speciality = models.CharField(max_length=100, verbose_name='Специальность')
    admission_year = models.IntegerField(verbose_name='Год поступления')
    graduation_year = models.IntegerField(verbose_name='Год окончания')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')


class Information(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='info')
    title = models.CharField(max_length=255, verbose_name='Заголовок')


class Experience(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='experiences')
    company = models.CharField(max_length=255, verbose_name='Компания')
    position = models.CharField(max_length=255, verbose_name='Долдность')
    start_year = models.IntegerField(verbose_name='Год начала')
    end_year = models.IntegerField(verbose_name='Год окончания')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')


class Skills(models.Model):
    class LevelSize(models.IntegerChoices):
        JUNIOR = 1, 'Junior'
        MIDDLE = 2, 'Middle'
        SENIOR = 3, 'Senior'


    name = models.CharField(max_length=255, verbose_name='Название')
    level = models.IntegerField(choices=LevelSize.choices, verbose_name='Уровень')
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='skills')

