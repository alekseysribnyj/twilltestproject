from twill.commands import *
from twill import *
SITE_URL = "http://localhost:8000"

def test_login_success():
    # User login success
    url = SITE_URL+"/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "aleksey")
    fv("1", "UserPassword", "aleksey")
    submit()
    find("Valid", "m")


def test_login_incorrect_password():
    #User try to login with incorrect password
    url = SITE_URL+"/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "aleksey")
    fv("1", "UserPassword", "11")
    submit()
    find("wrong password", "m")



def test_login_incorrect_username():
    #User try to login with incorrect username
    url = SITE_URL+"/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "1aleksey")
    fv("1", "UserPassword", "1")
    submit()
    find("wrong login", "m")



def test_register_and_login():
    #User register as new user and login to his account
    url = SITE_URL+"/register/"
    Login = "aleksey2"
    Password = "aleksey2"
    Email = "aleksey2@aleksey2.com"
    go(url)
    formclear('1')
    fv("1", "UserLogin", Login)
    fv("1", "UserPassword", Password)
    fv("1", "UserEmail", Email)
    submit()
    find("been registered", "m")

    url = SITE_URL+"/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", Login)
    fv("1", "UserPassword", Password)
    submit()
    find("Valid", "m")



def test_forgot_password():
    #User forget his password and want to get email with link to reset password
    url = SITE_URL+"/forgot/"
    go(url)
    formclear('1')
    fv("1", "email", "aleksey@aleksey.com")
    submit()
    find("check your mail", "m")



def test_get_new_password():
    url = SITE_URL+"/reset/1-2a5-1b00ecfbaec95570d237/"
    go(url)
    formclear('1')
    fv("1", "new_password1", "aleksey")
    fv("1", "new_password2", "newpassword")
    submit()
    find("password has been set")
