'''

home -
    The function to render the homepage of the website.
    If User is logged in it will show Username and if not then the option for Login/Signup.
    The logged in logi is inside templates/nav.html
    This page will also be used for providing information to the user and helping them in installing the extension.

Written_by - Rohit Anand
'''


from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, HttpResponse
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags
from django.utils.timezone import now
from .models import NoteBook, User
from .forms import NotebookCreationForm, NotebookChangeForm

import random


def home(request):
    context = {'title': 'Home'}
    print(context)
    return render(request, 'index.html', context=context)


def create_notebook_id(size):
    uid = get_random_string(length=size)

    # check if notebook already exists if not, return id
    try:
        notebook = NoteBook.objects.get(id=uid)
    except:
        notebook = None

    if not notebook:
        return uid
    else:
        create_notebook_id(size)  # If uid already exists recreate uid


def create_notebook(request):

    form = NotebookCreationForm()

    if request.method == 'POST':
        # clean data
        name = strip_tags(request.POST.get('name'))
        user = request.user
        about = request.POST.get('description')
        notebook_id = create_notebook_id(random.randint(5, 10))

        new_name = name if name else 'untitled'

        form = NotebookCreationForm()
        try:
            book = NoteBook.objects.create(id=notebook_id, name=new_name, owner=user, description=about)
            print('Notebook - {} created'.format(name))
            book.created_at = book.updated_at = now()
            book.save()
            context = {'title': 'Create', 'messages': ['Notebook created successfully'], 'form': form}
            return render(request, 'notebook_creation_form.html', context=context)

        except Exception as e:
            print(e)
            context = {'title': 'Create', 'messages': [e], 'form': form}
            return render(request, 'notebook_creation_form.html', context=context)

    else:
        context = {'title': 'Create', 'form': form}
        return render(request, 'notebook_creation_form.html', context=context)

