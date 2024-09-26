from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'Text',
                'placeholder': 'Введите имя',
            }
        ),
        required=True,
        validators=[RegexValidator(r'[^0-9а-аА-ЯёЁ]', 'Неверный тип имени')],      
    )
    
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'Email',
                'placeholder': 'Введите почту',
            }
        ),
        required=True
    )
    
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль',
            }
        ),
        required=True
    )
    
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль',
            }
        ),
        required=True
    )
    
    image_profile = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Avatar',
                }
            ),
            required=False
        )
    
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1 == '':
            raise forms.ValidationError('Пароль не может быть пустым', code='Invalid')
        return password1
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Имя не может быть пустым', code='Invalid')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Электронная почта не может быть пустой', code='Invalid')
        return email
    
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2', 'image_profile']
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'Text',
                'placeholder': 'Логин',
            }
        ),
        required=True
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Пароль',
            }
        ),
        required=True
    )
    
    error_messages = {
        'invalid_login': (
            'Введенные логин, либо пароль неправильные'
        )
    }
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='Invalid')
        return password
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='Invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('Пользователь не найден', code='Invalid')
        return username
        
        