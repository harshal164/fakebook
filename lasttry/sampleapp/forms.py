from django import forms
from .models import user, fileModel, comments

class RegisterForm(forms.Form):
    username=forms.CharField()
    pwd = forms.CharField(widget=forms.PasswordInput)
    name=forms.CharField()
    details=forms.CharField()
    qual=forms.CharField(widget=forms.Textarea)

class registerForm2(forms.ModelForm):
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),max_length=50)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'What\'s your name?'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Choose a username'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Write something about yourself'}))
    qual = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'What are your qualifications?'}))
    class Meta:
        model=user
        fields=['name','username','pwd','details','qual','photo']

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),max_length=50)

class fileForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter file name to display'}),max_length=100)
    class Meta:
        model = fileModel
        fields=['title','file']


class commentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment']