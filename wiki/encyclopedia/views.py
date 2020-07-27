from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    return render(request, "encyclopedia/css.html")

def django(request):
    return render(request, "encyclopedia/django.html")

def git(request):
    return render(request, "encyclopedia/git.html")

def html(request):
    return render(request, "encyclopedia/html.html")

def python(request):
    return render(request, "encyclopedia/python.html")
