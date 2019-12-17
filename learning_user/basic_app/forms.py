# from django import forms
# from django.contrib.auth.models import User
# from basic_app.models import userprofileinfo

#
# class userForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput())
#
#     class Meta:
#         model = User
#         Fiels = ('username','email','password')
#
# class userprofileinfoForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('profile_url','profile_pic')

from django import forms
from django.contrib.auth.models import User
from basic_app.models import userprofileinfo
from django.core import validators
from basic_app.models import article

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = userprofileinfo
        fields = ('profile_url','profile_pic')

# def check_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError("start with z")

class FormName(forms.Form):
    name2 = forms.CharField()
    email2 = forms.EmailField()
    verify_email = forms.EmailField(label='enter you mail beach')
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email2']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('olagh')

class user22(forms.ModelForm):
    class Meta():
        model = article
        fields = '__all__'




    # def clean_botcacher(self):
    #     botcacher = self.cleaned_data['botcacher']
    #     if len(botcacher) > 0 :
    #         raise forms.ValidationError('kir')
    #     return botcacher
