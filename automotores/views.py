from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola a todos!")
def saludo_html(request):
    documento ="""<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(documento)
def despedida(request):
    return HttpResponse("Hasta luego!")
