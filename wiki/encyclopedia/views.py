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
        title = request.POST.get("title")
        markdown = request.POST.get("markdown")
        save_path = "entries"

        for entry in util.list_entries():

            if re.search(f"^{title}$",entry,re.IGNORECASE):
                return render(request, "encyclopedia/entry.html", {
                    "entry": "Error: Entry already exists",
                    "name": "Error"
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
