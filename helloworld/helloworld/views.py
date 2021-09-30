# I have created this file- Shariar

from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, "index.html")
    # return HttpResponse("<h1>Hello Shariar Hossain, Its your Home<h1> "
    #                     "<a href=https://github.com/Shariar-Mozumder>Shariar Github</a><br>"
    #                     "<a href=https://www.facebook.com/shahriar.mozumder.33/>Shariar Facebook</a><br>"
    #                     "<a href=http://127.0.0.1:8000/Spaceremove>Spaceremove</a><br>"
    #                     "<a href=http://127.0.0.1:8000/NewLineremove>NewLineremove</a><br>"
    #                     "<a href=http://127.0.0.1:8000/CapitaFirst>CapitaFirst</a><br>"
    #                     "<a href=http://127.0.0.1:8000/RemovePunc>RemovePunc</a><br>"
    #                     "<a href=http://127.0.0.1:8000/CharCount>CharCount</a><br>")


# def Spaceremove(request):
#     return HttpResponse("Space Removing<br>"
#                         "<a href=http://127.0.0.1:8000/>Home</a><br>")
#
# def NewLineremove(request):
#     return HttpResponse("New Line remove<br>"
#                         "<a href=http://127.0.0.1:8000/>Home</a><br>")
#
# def CapitaFirst(request):
#     return HttpResponse("Capital First<br>"
#                         "<a href=http://127.0.0.1:8000/>Home</a><br>")
#
# def RemovePunc(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse("Remove Punctuations<br>"
#                         "<a href=http://127.0.0.1:8000/>Home</a><br>")
#
# def CharCount(request):
#     return HttpResponse("Character Count<br>"
#                         "<a href=http://127.0.0.1:8000/>Home</a><br>")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepuncONOFF = request.POST.get('removepunc', 'off')
    charcountONOFF = request.POST.get('charcount', 'off')
    spaceremoveONOFF = request.POST.get('spaceremove', 'off')
    newlineremoveONOFF = request.POST.get('newlineremove', 'off')
    capitalfirstONOFF = request.POST.get('capitalfirst', 'off')
    if removepuncONOFF == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = { 'analyzed_text': analyzed}
        djtext=analyzed


    if charcountONOFF == "on":
        count = 0
        for char in djtext:
            count = count + 1

        params = { 'analyzed_text': count}
        djtext = analyzed


    if spaceremoveONOFF == "on":
        space = " "
        analyzed = ""
        for char in djtext:
            if char is not space:
                analyzed = analyzed + char

        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremoveONOFF == "on":
        newline = "\n"
        analyzed = ""
        for char in djtext:
            if char is not newline and char != "\r":
                analyzed += char

        params = { 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalfirstONOFF == "on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper();

        params = { 'analyzed_text': analyzed}
        djtext = analyzed

    if removepuncONOFF != "on" and charcountONOFF != "on" and spaceremoveONOFF != "on" and newlineremoveONOFF != "on" and capitalfirstONOFF != "on":
        return HttpResponse('error')

    return render(request, 'analyze.html', params)



