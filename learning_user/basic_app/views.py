from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm,UserForm,FormName
from . import forms
# extra import
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basic_app.forms import user22
from basic_app.models import article


def index(request):
    return render(request,'basic_app/index.html',)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #save to db
            user = user_form.save()
            # hash passwod
            user.set_password(user.password)
            # update with hash pasword
            user.save()
            # canot commit because need manipulation
            profile = profile_form.save(commit =False)

            # set oto relation between userform and userprofileform
            profile.user = user

            # check if they provide pic profile
            if 'profile_pic' in request.FILES :
                # if yes , grab it from post reply
                profile.profile_pic = request.FILES['profile_pic']
            # save model
            profile.save()

            #registraion okay
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registration.html',{'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    return render(request,'user_login.html',)

def basic_app(request):
    return render(request,'basic_app.html',)

def Form_Name(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            #do something
            print('validation success')
            print(form.cleaned_data['name2'])
            print(form.cleaned_data['email2'])
            print(form.cleaned_data['text'])
    return render(request,'basic_app/Form_Name.html' , {'form':form} )

def user2(request):
    form4 = forms.user22()
    if request.method == 'POST':
        form4 = user22(request.POST)
        if form4.is_valid():
            form4.save(commit=True)
            return allarticle(request)
    # return allarticle(request)
    # HttpResponseRedirect(allarticle)
    return render(request, 'basic_app/user2.html', {'user2':form4} )


def allarticle(request):
    list_article = article.objects.order_by('name')
    data_article = {'listofart':list_article}
    return render(request, 'basic_app/allarticle.html',
     context = data_article  )
