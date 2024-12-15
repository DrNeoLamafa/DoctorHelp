from .pillslist import PillsList

def cart(request):
    return {'cart': PillsList(request)}