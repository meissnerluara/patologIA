from .models import CustomUserModel, RoleModel
from django.contrib.auth.hashers import make_password
from django import forms

class CreateSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'username','name':'username', 'placeholder':'Entre com seu nome de usuário'}))
     
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'name','name':'name', 'placeholder':'Informe seu Nome'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'lastname','name':'lastname', 'placeholder':'Informe seu sobrenome'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'name':'email', 'placeholder':'Informe seu e-mail'}))
    Mobile_Number = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control','type':'tel', 'id':'fone','name':'fone', 'placeholder':'Informe seu celular'}))
    password = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'class': 'form-control','id':'password','name':'password', 'placeholder':'Informe sua senha'}))
    confirm_password = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'class': 'form-control','id':'confirmpassword','name':'confirmpassword', 'placeholder':'Confirme sua senha'}))
    Role = forms.ModelChoiceField(queryset=RoleModel.objects.exclude(Role_Type = "student"),
        label="",
        empty_label="Escolha sua opção ...",
        widget=forms.Select(attrs={'class': 'custom-select'}))
    Accept_Terms_of_Services = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':'agree-form','name':'agree-form'}))
    Receive_News = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':'newsletter','name':'newsletter'}),
        initial=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        # Hash the password
        hashed_password = make_password(password)
        cleaned_data['password'] = hashed_password

        
    class Meta:
        model = CustomUserModel
        fields = ['username','first_name','last_name','email','Mobile_Number','password','confirm_password','Role','Accept_Terms_of_Services','Receive_News']

class CreateLogInForm(forms.ModelForm):
    Role = forms.ModelChoiceField(queryset=RoleModel.objects.all(),
        label="",
        empty_label="Escolha sua opção ...",
        widget=forms.Select(attrs={'class': 'custom-select'}))
        
    class Meta:
        model = CustomUserModel
        fields = ['Role']
        exclude = ['username','first_name','last_name','email','Mobile_Number','password','confirm_password','Accept_Terms_of_Services','Receive_News']