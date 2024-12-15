from functools import reduce
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:

        searchform = SearchForm()
        return render(request, 'main.html', {'searchform': searchform})
    else:
        return redirect('/user/login/')
    
#поиск аналогов
@login_required()
def result(request):

    def findAnalogue(vectorSeach, type):
        #вектор поиска и тип поиска
        filtdict = {f'{type}__in': vectorSeach}
        
        result = {}
        finded = list(Pills.objects.filter(**filtdict))
        
        for item in finded:
            result[item] = finded.count(item)
        
        return map(lambda item: item[0], sorted(result.items(), key=lambda x: x[1], reverse=True))
    #удаление лишних символов, создание Q запроса для поиска связанных объектов
    def prepareData(rawdata, type):
        q_list = filter(lambda w: w != '', rawdata)
        match type:
            case 'name':
                q_list = map(lambda n: Q(name__icontains=n), q_list)
            case 'composit':
                q_list = map(lambda n: Q(composit__icontains=n), q_list)
            case 'diseases':
                q_list = map(lambda n: Q(diseases__icontains=n), q_list)
        q_list = reduce(lambda a, b: a | b, q_list)
        return q_list

    typesearch = request.GET.get('type')
    input  = request.GET.get('search').split(' ')
    match typesearch:
        # поиск по имени и аналогов по составу 
        case '1':
            q_list = prepareData(input, 'name')
            pillObj = Pills.objects.filter(q_list)
            vect = []
            if pillObj:
                vect = pillObj[0].composition.all()
                result = list(findAnalogue(vect, 'composition'))
                result.remove(pillObj[0])
                result.insert(0, pillObj[0])
            else: 
                result = []
            
        # поиск по составу 
        case '2':
            q_list = prepareData(input, 'composit')
            vect = Composition.objects.filter(q_list)
            result = findAnalogue(vect, 'composition')

        # поиск по болезням
        case '3':
            q_list = prepareData(input, 'diseases')
            vect = Diseases.objects.filter(q_list)
            result = findAnalogue(vect, 'diseases')
    searchform = SearchForm()
    searchform.fields["searchType"].initial = [int(typesearch)]
    return render(request, 'result.html', {'searchform': searchform, 'findPill' : result})



def search(request):
    # предварительный поиск для подстановки
    result = []
    enter = request.GET.get('search')
    typesearch = request.GET.get('type')
    if enter:
        if typesearch == '1':
            names = Pills.objects.filter(name__istartswith=enter)
            for name in names:
                result.append(name.name)
        elif typesearch == '2':
            word = enter.split()
            names = Composition.objects.filter(composit__istartswith=word[-1])
            for name in names:
                result.append(name.composit) 
        else:
            word = enter.split()
            names = Diseases.objects.filter(diseases__istartswith=word[-1])
            for name in names:
                
                result.append(name.diseases)
            
        
    return JsonResponse({'status': typesearch, 'data': result})