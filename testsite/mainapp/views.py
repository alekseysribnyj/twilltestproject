from django.contrib.auth.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.views import password_reset
from django.shortcuts import render_to_response
from testsite.funcs import CustomReturnToResponse, ReturnAbsoluteUrl
from testsite.mainapp.forms import *
from testsite.mainapp.models import UserProfile


def index(request):
    #Index page. Output menu
    PageContent = CustomReturnToResponse('main.tpl',
         {"abslturl": ReturnAbsoluteUrl()})
    return render_to_response('index.tpl',
        {'PageTitle': 'Main Page', 'PageContent': PageContent})


def forgot(request):
    #Forgot password form and it's processing
    return password_reset(request,
                          template_name='resetpassword/form.tpl',
                          email_template_name= 'resetpassword/email.tpl',
                          post_reset_redirect='/forgot/done/')


def forgot_message(request):
    #Output message. Shown after successful forgot password processing
    return render_to_response('index.tpl',
        {'PageTitle': 'Login', 'PageContent': "Please check your mail"})


def login(request):
    #Login page
    Content = {}
    Content["CustomErrors"] = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                #Check for user login
                User.objects.get(
                    username__exact=form.cleaned_data['UserLogin'])
            except:
                #Wrong login
                Content["CustomErrors"].append("You've entered wrong login.")
            else:
                user = authenticate(username=form.cleaned_data['UserLogin'],
                password=form.cleaned_data['UserPassword'])
                if user is None:
                    #Wrong password
                    Content["CustomErrors"].\
                        append("You've entered wrong password.")
                else:
                    #Let's try to get profile
                    try:
                        user.get_profile()
                    except:
                        Content["CustomErrors"].\
                            append("Sorry, we don't have you profile")
                    else:
                        Content["CustomErrors"].\
                            append("Grats! Valid login and password.")


    else:
        form = LoginForm()
    Content["form"] = form
    PageContent = CustomReturnToResponse('loginform.tpl', Content)
    return render_to_response('index.tpl',
            {'PageTitle': 'Login', 'PageContent': PageContent})


def register(request):
    #Register page
    Content = {}
    Content["CustomErrors"] = []
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                #Try getting user with entered email
                User.objects.get(email__exact=form.cleaned_data['UserEmail'])
            except:
                #We don't have user with such mail
                #Let's try to register user
                newuser = User.objects.create_user(
                            username=form.cleaned_data['UserLogin'],
                            email=form.cleaned_data['UserEmail'],
                            password=form.cleaned_data['UserPassword'])
                try:
                    #Save user
                    newuser.save()
                    try:
                        profile = UserProfile(SomeData=1, user=newuser)
                        profile.save()
                    except:
                        Content["CustomErrors"].\
                            append("Error while registering profile")
                    else:
                        Content["CustomErrors"].\
                            append("You've been registered")
                except:
                    #Error!
                    Content["CustomErrors"].\
                    append("User with such username was already registered.\
                            Please, enter another login")
            else:
                #We have user with such email
                Content["CustomErrors"].\
                    append("User with such email was already registered.\
                            Please, enter another mail")


    else:
        form = RegisterForm()

    Content["form"] = form
    Content["abslturl"] = ReturnAbsoluteUrl()
    PageContent = CustomReturnToResponse('registerform.tpl', Content)
    return render_to_response('index.tpl',
            {'PageTitle': 'Register', 'PageContent': PageContent})
