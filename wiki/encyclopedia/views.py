from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown
import re

from . import util
markdowner = Markdown()

def search(request):

    search = request.POST.get("search")
    entry = util.get_entry(search)

    if not entry:

        if re.search("^py", search, re.IGNORECASE):

            return render(request, "encyclopedia/search.html", {
                "entry": "Python"
            })

        elif re.search("^dj", search, re.IGNORECASE):

            return render(request, "encyclopedia/search.html", {
                "entry": "Django"
            })

        elif re.search("^cs", search, re.IGNORECASE):

            return render(request, "encyclopedia/search.html", {
                "entry": "CSS"
            })

    else:
        return redirect(f'/wiki/{search}')

def index(request):

    if request.method == "POST":
        return search(request)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):

    if request.method == "POST":
        return search(request)

    entry = util.get_entry(name)

    if not entry:

        return render(request, "encyclopedia/entry.html", {
            "error": "ERROR 404: Requested page was not found!",
            "name": name
        })

    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "name": name
        })
