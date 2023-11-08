from django.db import models
from django.contrib.auth.models import User

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'Мужчина'),
    (FEMALE, 'Женщина')
)


FAMILY = 1
FREE = 2

FAMIL = (
    (FAMILY, 'Да'),
    (FREE, 'Нет')
)

YES = 1
NO = 2

ANIMALS = (
    (YES, 'Да'),
    (NO, 'Нет')
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13, default='+996', verbose_name='Введите номер телефона')
    date_birth = models.DateField(verbose_name='Ваша дата рождения')
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Укажите пол')
    age = models.IntegerField(max_length=100, verbose_name='Сколько вам лет ?')
    hobby = models.CharField(max_length=99, verbose_name='Ваше увлечение')
    job = models.CharField(max_length=50, verbose_name='Кем вы работаете')
    married = models.IntegerField(choices=FAMILY, verbose_name='У вас есть семья ?')
    height = models.CharField(max_length=5, verbose_name='какой у вас рост ?')
    animals = models.CharField(choices=ANIMALS, verbose_name='У вас есть питомец ?')
    name_animal = models.CharField(max_length=50, verbose_name='Укажите имя вашего питомца')


class RegisterSucces(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title