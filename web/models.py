from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    profession = models.CharField(max_length=50, verbose_name='Профессия')
    about = models.TextField(max_length=2000, verbose_name='Краткое описание')


class SocialLinks(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    link = models.URLField(max_length=500, unique=True)
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                verbose_name='Профиль', related_name='links')


class Education(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='links')
    name = models.CharField(max_length=255, verbose_name='Название')
    speciality = models.CharField(max_length=100, verbose_name='Специальность')
    admission_year = models.IntegerField(verbose_name='Год поступления')
    graduation_year = models.IntegerField(verbose_name='Год окончания')
    description = models.TextField(max_length=2000, verbose_name='Описание')


class Experience(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='links')
    company = models.CharField(max_length=255, verbose_name='Компания')
    position = models.CharField(max_length=255, verbose_name='Долдность')
    start_year = models.IntegerField(verbose_name='Год начала')
    end_year = models.IntegerField(verbose_name='Год окончания')
    description = models.TextField(max_length=2000, verbose_name='Описание')


class Skills(models.Model):
    class LevelSize(models.IntegerChoices):
        JUNIOR = 1, 'Junior'
        MIDDLE = 2, 'Middle'
        SENIOR = 3, 'Senior'

    name = models.CharField(max_length=255, verbose_name='Название')
    level = models.IntegerField(choices=LevelSize.choices, verbose_name='Уровень')
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE,
                                 verbose_name='Профиль', related_name='links')


class Technologies(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    profiles = models.ManyToManyField('web.Profile', related_name='technologies', verbose_name='Профили',
                                      through='web.TechnologiesProfiles')


class TechnologiesProfiles(models.Model):
    profiles = models.ForeignKey('web.Profile', on_delete=models.CASCADE)
    technologies = models.ForeignKey('web.Technologies',  on_delete=models.CASCADE)
