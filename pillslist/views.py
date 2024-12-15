import datetime
import locale
from django.conf import settings
from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .pillslist import PillsList
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, DatePeople
from docxtpl import DocxTemplate


@login_required()
def pills_add(request):
    cart = PillsList(request)
    id = request.POST.get('pillsId')
    cart.add(id)
    

    return JsonResponse({"name": id}, status=200)
@login_required()
def pills_detail(request):
    cart = PillsList(request)
    formList = []

    for pill in cart:
        formList.append(RecipeForm(initial={'pillsName': pill}))
        
    if request.method == "POST":
        
        fillBlank(request)
        return FileResponse(open(str(settings.BASE_DIR) + '/pillslist/static/fillblank' + str(request.user.id) + '.docx','rb'))
        
    else:

        return render(request, 'pillslist.html', {'cart': cart, 'formList': formList, 'datePeople': DatePeople()})

@login_required()
def pills_remove(request, product_id):
    cart = PillsList(request)
    cart.remove(product_id)
    return redirect('pillslist:pills_detail')

   
def fillBlank(request):
    locale.setlocale(locale.LC_ALL, "")
    doctor = request.POST.get("doctor")
    patient = request.POST.get("patient")
    birthday = datetime.date(int(request.POST.get("birthday_year")), int(request.POST.get("birthday_month")), int(request.POST.get("birthday_day")))
    pillsNames = request.POST.getlist('pillsName')
    recipes = request.POST.getlist('recipe')
 
    context = {
        'name1': '',
        'howto1': '',
        'name2': '',
        'howto2': '',
        'name3': '',
        'howto3': '',
        'doctor': doctor,
        'patient': patient,
        'day': datetime.date.today().strftime("%d"),
        'mon': datetime.date.today().strftime("%B"),
        'year': datetime.date.today().strftime("%y"),
        'birthday': birthday.strftime("%d.%m.%Y")
        }

    for i in range(len(pillsNames)):
        context['name' + str(i+1)] = pillsNames[i]
        context['howto' + str(i+1)] = recipes[i]
    
    doc = DocxTemplate(str(settings.BASE_DIR) + '/pillslist/static/blank.docx')
    
    doc.render(context)
    doc.save(str(settings.BASE_DIR) + '/pillslist/static/fillblank' + str(request.user.id) + '.docx')

