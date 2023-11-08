from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

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


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите ваш номер')
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    age = forms.IntegerField(required=True, verbose_name='Сколько вам лет ?')
    hobby = forms.CharField(max_length=99, verbose_name='Ваше увлечение')
    job = forms.CharField(max_length=50, verbose_name='Кем вы работаете ?')
    family = forms.IntegerField(choices=FAMILY, verbose_name='У вас есть семья ?')
    height = forms.CharField(max_length=5, verbose_name='какой у вас рост ?')
    animals = forms.CharField(choices=ANIMALS, verbose_name='У вас есть питомец ?')
    name_animal = forms.CharField(max_length=50, verbose_name='Укажите имя вашего питомца')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_birth',
            'gender',
            'age',
            'hobby',
            'job',
            'married',
            'animal',
            'height',
            'name_animal',
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
