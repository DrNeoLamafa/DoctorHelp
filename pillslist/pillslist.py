
from django.conf import settings
from pills.models import Pills


class PillsList(object):

    def __init__(self, request):
       
        self.session = request.session
        pillslist = self.session.get(settings.CART_SESSION_ID)
        if not pillslist:
            pillslist = self.session[settings.CART_SESSION_ID] = []
        self.pillslist = pillslist
    
    def add(self, pills):
        pillsname = str(pills)
        if pillsname not in self.pillslist:
            self.pillslist.append(pills)
        
        self.save()

    def save(self):
        
        self.session[settings.CART_SESSION_ID] = self.pillslist
        self.session.modified = True

    def remove(self, pills):
        
        pillsname = str(pills)
        if pillsname in self.pillslist:
            self.pillslist.remove(pillsname)
            self.save()

    def clear(self):
    
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    

    def __iter__(self):
   
        for item in self.pillslist:
            yield item