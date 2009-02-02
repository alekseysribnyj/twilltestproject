from twill.commands import *
from twill import *
from twill import namespaces
def test():
    url = "http://clients.sribnyj.com.ua/test/"
    go(url)
    formclear('1')
    fv("1", "UserLogin", "aleksey")
    fv("1", "UserPassword", "aleksey")
    submit()
    try:
        find("Bad Karma","m")
    except:
        try:
            find("Well Done","m")
        except:
            assert False
        else:
            assert True
    else:
        assert False