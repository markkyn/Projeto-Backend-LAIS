from django import forms

class LoginForm(forms.Form):
    cpf_Field = forms.CharField(label='CPF(apenas números)', min_length=11, max_length=11)
    password_Field = forms.CharField(label='Senha' , widget= forms.PasswordInput)