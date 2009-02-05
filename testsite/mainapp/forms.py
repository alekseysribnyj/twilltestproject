from django import forms


class LoginForm(forms.Form):
    UserLogin = forms.CharField(required = True, max_length=50,
                                                label='Your Login')
    UserPassword = forms.CharField(required = True,
                                                label='Your Password')


class RegisterForm(forms.Form):
    UserLogin = forms.CharField(required = True, max_length=50,
                                                label='Your Login')
    UserEmail = forms.EmailField(required = True, max_length=100,
                                                label='Your Email')
    UserPassword = forms.CharField(required = True, min_length=5,
                                                label='Your password')
