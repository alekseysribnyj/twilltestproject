from twill.commands import *
from twill import *


def test_login_success():
    # User login success
    url = "http://localhost:8000/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "aleksey22")
    fv("1", "UserPassword", "aleksey22")
    submit()
    try:
        find("Valid", "m")
    except:
        assert False
    else:
        assert True


def test_login_incorrect_password():
    #User try to login with incorrect password
    url = "http://localhost:8000/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "aleksey")
    fv("1", "UserPassword", "11")
    submit()
    try:
        find("wrong password", "m")
    except:
        assert False
    else:
        assert True


def test_login_incorrect_username():
    #User try to login with incorrect username
    url = "http://localhost:8000/login/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "1aleksey")
    fv("1", "UserPassword", "1")
    submit()
    try:
        find("wrong login", "m")
    except:
        assert False
    else:
        assert True


def test_register_and_login():
    #User register as new user and login to his account
    url = "http://localhost:8000/register/"
    Login = "1124124512412"
    Password = "112412451241211241245124121124124512412"
    Email = "1124124512412@1124124512412.com"
    go(url)
    formclear('1')
    fv("1", "UserLogin", Login)
    fv("1", "UserPassword", Password)
    fv("1", "UserEmail", Email)
    submit()
    try:
        find("been registered", "m")
    except:
        assert False
    else:
        #Login
        url = "http://localhost:8000/login/"
        go(url)
        formclear('1')
        fv("1", "UserLogin", Login)
        fv("1", "UserPassword", Password)
        submit()
        try:
            find("Valid", "m")
        except:
            assert False
        else:
            assert True


def test_forgot_password():
    #User forget his password and want to get email with link to reset password
    url = "http://localhost:8000/forgot/"
    go(url)
    formclear('1')
    fv("1", "email", "aleksey@aleksey.com")
    submit()
    try:
        find("check your mail", "m")
    except:
        assert False
    else:
        assert True


def test_get_new_password():
    url = "http://localhost:8000/reset/1-2a5-1b00ecfbaec95570d237/"
    go(url)
    formclear('1')
    fv("1", "new_password1", Login)
    fv("1", "new_password2", Password)
    submit()
    try:
        find("password has been set")
    except:
        assert False
    else:
        assert True
