from django.template import Context, loader
from django.conf import settings


def CustomReturnToResponse(InputTemplate, InputDictionary):
    Templ = loader.get_template(InputTemplate)
    Contx = Context(InputDictionary)
    return Templ.render(Contx)


def ReturnAbsoluteUrl():
    return str(settings.SITE_URL)
