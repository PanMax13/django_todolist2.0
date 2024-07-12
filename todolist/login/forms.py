from django import forms


class RegisterForm(forms.Form):
    userName = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'UserName', 'name': 'userName'}))
    email = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'name': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name': 'password'}), label='')
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'repeat_password': 'password2'}), label='')



