from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound(f"""<h1 style=color:red> The contents you are looking for do not exist</h1>""")

def handler500(request):
    return HttpResponse(f"""<h1 style=color:red> Internal Server Error. Please try again later.</h1>""", status=500)


#-----------2 sep 2026 changes m----------------
#'DIRS': ['templates'],  # Specify the templates directory line no 57 in settings.py file has been added to specify the templates directory. This allows Django to look for templates in the specified directory when rendering views.
# and line no 35 in settings.py file has been added to include 'myapp' in the INSTALLED_APPS list. This ensures that Django recognizes 'myapp' as an installed application and can use its models, views, and templates.