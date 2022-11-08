from django.shortcuts import render

from MyApp.models import Familiares
# Create your views here.

def mostrar_familia(request):

    f1 = Familiares(nombre='Daniel', apellido='Padilla', edad='38', nacimiento='1984-07-24')
    f2 = Familiares(nombre='Dulce', apellido='Padilla', edad='34', nacimiento='1988-09-05')
    f3 = Familiares(nombre='Alejandro', apellido='Padilla', edad='15', nacimiento='2007-02-18')

    return render(request, 'MyApp/Templates/familiares.html', {'familiares':[f1, f2, f3]})