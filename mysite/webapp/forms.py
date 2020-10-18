from .models import PublicationsTable
from .models import AuthorsTable
from django.forms import ModelForm,TextInput


class PublicationsTableForm(ModelForm):
    class Meta:
        model = PublicationsTable
        fields = [
            "name", "source", "publicationType", "number_of_pages", "author_id",
        ]
        widgets = {
            "name": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите название'}),
            "source": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите источник(и)'}),
            "publicationType": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите тип'}),
            "number_of_pages": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите количество страниц'}),
            "author_id": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите ID Автора'}),
        }


class AuthorsTableForm(ModelForm):
    class Meta:
        model = AuthorsTable
        fields = [
            "surname", "name", "patronymic", "rank", "date_of_birth",
        ]
        widgets = {
            "surname": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите фамилию'}),
            "name": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите имя'}),
            "patronymic": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите отчество'}),
            "rank": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите звание'}),
            "date_of_birth": TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Введите дату рождения'}),
        }