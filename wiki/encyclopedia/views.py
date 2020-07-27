from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown

from . import util
markdowner = Markdown()

def index(request):

    if request.method == "POST":

            search = request.POST.get("search")
            entry = util.get_entry(search)

            if not entry:
                return render(request, "encyclopedia/search.html", {
                    "entries": util.list_entries()
                })
            #else:
                # TOFIX return entry(request, search)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):

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
