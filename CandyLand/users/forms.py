from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # 1. ИСПРАВЛЕНО: fields (с буквой s) и правильное имя поля 'email_user'
        fields = ['name_user', 'email_user', 'avatar']

        # 2. ИСПРАВЛЕНО: widgets (с буквой d)
        widgets = {
            'name_user': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите никнейм'
            }),
            # 3. ИСПРАВЛЕНО: Для модели TextField используем Textarea (компактный, в 1 строку)
            'email_user': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.com',
                'rows': 1,
                'style': 'resize: none;'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            })
        }
        labels = {
            'name_user': 'Никнейм',
            'email_user': 'Email',
            'avatar': 'Аватар'
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        # 4. ИСПРАВЛЕНО: правильные отступы и имя поля 'first_name'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            })
        }


class CustomUserCreationForm(UserCreationForm):
    # Явно объявляем поле email
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@mail.com',
            'class': 'form-control' # можно сразу добавить класс для красоты
        })
    )
    
    # Переопределяем встроенные поля паролей, чтобы задать им placeholder
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
            'id': 'id_password1' # жестко фиксируем ID для вашего JS-скрипта
        })
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'id': 'id_password2' # жестко фиксируем ID для вашего JS-скрипта
        })
    )

    class Meta:
        model = User
        # В fields указываем ТОЛЬКО реальные поля модели User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Введите имя пользователя',
                'id': 'id_username'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email
