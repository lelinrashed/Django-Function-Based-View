from django.http import HttpResponse, HttpResponseRedirect


# def home(request):
#     # print(request)
#     # print(dir(request))
#     # print(request.method)
#     print(request.get_full_path())
#     return HttpResponse("<h1>Hello Django</h1>")


def home(request):
    response = HttpResponse(content_type="application/json")
    response = HttpResponse(content_type="text/html")
    response.content = "<h1>Hello Django</h1>"
    response.write("<p>Here's the text of the web page.</p>")
    print(response.status_code)
    return response


def redirect_somewhere(request):
    return HttpResponseRedirect("/home")
