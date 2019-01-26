"""

home -
    The function to render the homepage of the website.
    If User is logged in it will show Username and if not then the option for Login/Signup.
    The logged in logi is inside templates/nav.html
    This page will also be used for providing information to the user and helping them in installing the extension.

Written_by - Rohit Anand
"""

from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, HttpResponse
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags
from django.utils.timezone import now
from .models import NoteBook, Article, User
from .forms import NotebookCreationForm, NotebookChangeForm, ArticleCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import random
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../scribe-fdf862bebb2f.json"

def text2speech(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # instead return the encoded audio_content to decode and play in Javascript
    return response.audio_content


@csrf_exempt
def getAudio(request):
   if request.method == 'POST':

        from gtts import gTTS

        # This module is imported so that we can
        # play the converted audio
        import os

        # The text that you want to convert to audio
        mytext = strip_tags(request.POST.get('text'))
        print(mytext)
        # Language in which you want to convert
        language = 'en'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("scribe/assets/speech.mp3")
        speech = 'scribe/assets/speech.mp3'
        # Playing the converted file
        f = open(speech, "rb")
        response = HttpResponse(f.read())
        response['Content-Type'] = 'audio/mp3'
        response['Content-Length'] = os.path.getsize(speech)
        nothing ={"nothing":"nothing"}
        return JsonResponse(nothing)


def getlist(request, uid):
    id = []
    name = []
    user = User.objects.get(username=uid)

    try:
        notes = get_list_or_404(NoteBook, owner=user)
        for item in notes:
            id.append(item.id)
            name.append(item.name)
        x = {"id": id, "name": name}
        return JsonResponse(x)

    except:
        x = {"id": "id", "name": "name"}
        return JsonResponse(x)


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


@login_required(login_url='/accounts/login/')
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


@csrf_exempt
def view_notebook(request, uid):
    if request.method == 'POST':

        notebook = NoteBook.objects.get(id=uid)
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(content)
        try:
            article = Article.objects.create(notebook=notebook, title=title, content=content)
            # print('Article - {} created'.format(content[:100]))

            article.created_at = now()
            article.save()
            return redirect('view_notebook', uid=uid)

        except Exception as e:
            context = {'title': 'Error', 'messages': [e]}
            return render(request, 'notebook.html', context=context)

    else:
        # def get(self, request, uid):
        try:
            notebook = get_object_or_404(NoteBook, id=uid, owner=request.user)
        except Exception as e:
            context = {'title': '404', 'messages': [e, 'OR, You do not own this notebook!']}
            return render(request, 'notebook.html', context=context)

        try:
            articles = get_list_or_404(Article, notebook=notebook)
        except:
            articles = None

        form = ArticleCreationForm()

        context = {'title': notebook.name, 'notebook': notebook, 'articles': articles,
                   'article_form': form} if articles is not None else {
            'title': notebook.name, 'notebook': notebook, 'article_form': form}
        return render(request, 'notebook.html', context=context)
