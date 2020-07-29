from django.shortcuts import render
from markdown2 import Markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):

    entry = util.get_entry(name)

    if not entry:
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry("notFound"),
            "name": name
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "name": name
        })

def create(request):

    if request.method == "POST":
        return

    else:
        return render(request, "encyclopedia/create.html")
