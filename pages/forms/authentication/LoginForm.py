from django import forms

class LoginForm(forms.Form):
    cpf_Field = forms.CharField(
        label='CPF(apenas números)',
        min_length=11,
        max_length=11,
        widget= forms.TextInput(
            attrs = {
                "class" : "form-control"
            }
        )
    )
    password_Field = forms.CharField(
        label ='Senha',
        widget= forms.PasswordInput(
            attrs = {
                "class" : "form-control",
            }
        ),
        min_length=8
    )