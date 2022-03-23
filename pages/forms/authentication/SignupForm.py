from django import forms
from django.contrib.auth.forms import UserCreationForm
from pages.form_validators import cpf_already_registered  

from users.models import User,Group
from users.validators import cpf_validator, age_validator

class SignupForm(UserCreationForm):
    full_name_Field = forms.CharField(
        label = "Nome Completo",
        required= True,
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'Seu Nome'
            }
        )
    )

    cpf_Field = forms.CharField(
        label= "CPF (apenas números)",
        required= True,
        max_length=11,
        min_length=11,
        validators= [cpf_validator, cpf_already_registered],
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'11 Dígitos'
            }
        )
    )

    date_of_birth_Field = forms.DateField(
        label= "Data de Nascimento",
        required= True,
        validators= [age_validator],
        widget= forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    groups_Field = forms.ModelMultipleChoiceField(
        label = "Grupo de Atendimento",
        queryset = Group.objects.filter(visivel = True),
        required = False,
        widget= forms.SelectMultiple(
            attrs= {
                'class':'form-control',
            }
        ),
        help_text = 'Pressione a tecla "SHIFT" ou "CTRL" para selecionar multiplos grupos (Campo não-obrigatório)'
    )

    had_covid_Field = forms.BooleanField(
        label = "Selecione caso você tenha sido diagnósticado com covid nos ultimos 30 dias",
        required=False
    )

    field_order = ['full_name_Field', 'cpf_Field', 'date_of_birth_Field', 'groups_Field', 'password1', 'password2']
    
    class Meta:
        model = User
        exclude = ('username',)
        fields = ['password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
    def register(self):
        new_user = User()

        new_user.full_name = self.cleaned_data['full_name_Field']
        new_user.cpf = self.cleaned_data['cpf_Field']
        new_user.date_of_birth = self.cleaned_data['date_of_birth_Field']
        new_user.had_covid_last_month = self.cleaned_data['had_covid_Field']
        
        new_user.set_password(self.cleaned_data['password1'])
        
        new_user.save()

        new_user.groups.set(self.cleaned_data['groups_Field'])

        

        

        

    