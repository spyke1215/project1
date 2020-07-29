from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown
import os.path
import re

from . import util

def search(request):

    search = request.POST.get("search")
    test = util.get_entry(search)
    
    if not test:

        final = None

        for entry in util.list_entries():

            result = re.search(rf"^{search}\w+|^{search}$",entry,re.IGNORECASE)

            if not result:
                continue
            elif re.search(f"^{search}$",entry,re.IGNORECASE):
                return redirect(f'/wiki/{result.group()}')
            else:
                final = result.group()
        
        return render(request, "encyclopedia/search.html", {
            "entries": final
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

def create(request):

    if request.method == "POST":
        title = request.POST.get("title")
        markdown = request.POST.get("markdown")
        save_path = "entries"

        for entry in util.list_entries():

            if re.search(f"^{title}$",entry,re.IGNORECASE):
                return render(request, "encyclopedia/entry.html", {
                    "error": "Error: Entry already exists",
                    "name": title
                }) 

        complete_title = os.path.join(save_path, f"{title}.md")  

        entry = open(complete_title, "w")
        entry.write(markdown)
        entry.close()

        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title),
            "name": title
        })

    else:
        return render(request, "encyclopedia/create.html")
