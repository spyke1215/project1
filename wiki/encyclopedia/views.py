from django.shortcuts import render
from markdown2 import Markdown
import os.path

import re

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
        title = request.POST.get == "title"
        markdown = request.POST.get == "markdown"

        for entry in util.list_entries():

            if re.search(f"^{title}$",entry,re.IGNORECASE):
                return render(request, "encyclopedia/entry.html", {
                    "entry": "Error: Entry already exists",
                    "name": "Error"
                }) 

        save_path = "entries"

        complete_title = os.path.join(save_path, f"{title}.md")  

        new_entry = open(complete_title, "w")
        toFile = raw_input(markdown)
        new_entry.write(toFile)
        new_entry.close()

        return render(request, "encyclopedia/entry.html", {
            "entry": title,
            "name": title
        })

    else:
        return render(request, "encyclopedia/create.html")
