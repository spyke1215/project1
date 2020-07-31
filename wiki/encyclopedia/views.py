from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2
import random
import os.path
import re


from . import util

global test

# SEARCH
def search(request):

    search = request.POST.get("search") # getting data on POST
    test = util.get_entry(search) # checking if the is a entry already
    
    # if theres no entry
    if not test:

        final = None

        # checking all the entries
        for entry in util.list_entries():
            
            # checking if the serach has a substring on list of entries
            result = re.search(rf"^{search}\w+|^{search}$",entry,re.IGNORECASE)

            if not result: # if result is None
                continue
            elif re.search(f"^{search}$",entry,re.IGNORECASE): #if entry case insensitive found
                return redirect(f'/wiki/{result.group()}')
            else: #store the result in final
                final = result.group()
        
        #after the loop redirect to search.html
        return render(request, "encyclopedia/search.html", {
            "entries": final
        })

    # if there is entry, redirect to the page
    else:
        return redirect(f'/wiki/{search}')

# INDEX PAGE
def index(request):
    
    # if POST go to search function
    if request.method == "POST":
        return search(request)

    # if GET render index.html
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random": random.choice(util.list_entries())
    })

# ENTRY PAGE
def entry(request, name):

    # if post go to search function
    if request.method == "POST":
        return search(request)

    # checking if entry is in the list of entries
    entry = util.get_entry(name)
    
    if not entry: #if entry is None 

        return render(request, "encyclopedia/entry.html", { # return an error
            "error": "ERROR 404: Requested page was not found!",
            "name": name,
            "random": random.choice(util.list_entries())
        })

    else: # if entry has a value
        
        entry = open(f"entries/{name}.md", "r") # dosen't work
        markdown = entry.read()
        entry.close()

        return render(request, "encyclopedia/entry.html", { # show the entry to user
            "entry": markdown2.markdown(markdown),
            "name": name
        })
        
# EDIT PAGE
def edit(request):

    # if POST go to create function
    if request.method == "POST":

        title = request.POST.get("title") # getting title entered by the user
        markdown = request.POST.get("markdown") # getting markdown entered by the user

        save_path = "entries" # saving the path for entries

        complete_title = os.path.join(save_path, f"{title}.md") # combine the path and the title

        entry = open(complete_title, "w") # open the file
        entry.write(markdown) # write in the file
        entry.close() # close file

        return redirect(f'/wiki/{title}') # redirect to entry to show the user

    # if GET open edit.html
    else:
        entry = open(f"entries/{test}.md", "r") # dosen't work
        markdown = entry.read()
        entry.close()

        return render(request, "encyclopedia/edit.html", { # render the data to edit
            "title": "HTML",
            "markdown": markdown,
            "random": random.choice(util.list_entries())
        })

# NEW PAGE
def create(request):

    # if POST 
    if request.method == "POST":

        title = request.POST.get("title") # getting title entered by the user
        markdown = request.POST.get("markdown") # getting markdown entered by the user

        save_path = "entries" # saving the path for entries

        # loop entries
        for entry in util.list_entries(): 

            if re.search(f"^{title}$",entry,re.IGNORECASE): # if title has already exist
                return render(request, "encyclopedia/entry.html", { # return an error
                    "error": "Error: Entry already exists",
                    "name": title,
                    "random": random.choice(util.list_entries())
                }) 

        complete_title = os.path.join(save_path, f"{title}.md") # combine the path and the title

        entry = open(complete_title, "w") # open the file
        entry.write(markdown) # write in the file
        entry.close() # close file

        return redirect(f'/wiki/{title}') # redirect to entry to show the user

    # if GET render create.html
    else:
        return render(request, "encyclopedia/create.html", {
            "random": random.choice(util.list_entries())
        })
