from django.shortcuts import render
from markdown2 import Markdown

from . import util
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(entry),
        "name": entry
    })
