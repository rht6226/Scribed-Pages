'''

home -
    The function to render the homepage of the website.
    If User is logged in it will show Username and if not then the option for Login/Signup.
    The logged in logi is inside templates/nav.html
    This page will also be used for providing information to the user and helping them in installing the extension.

Written_by - Rohit Anand
'''


from django.shortcuts import render


def home(request):
    context = {'title': 'Home'}
    print(context)
    return render(request, 'index.html', context=context)
