from django import forms
from .models import NoteBook, Article
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NotebookCreationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = NoteBook
        fields = (
            'name', 'description',
        )


class NotebookChangeForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = NoteBook
        fields = {
            'name',
            'description',
        }


class ArticleCreationForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Article
        fields = {
            'title',
            'content',
        }


class ArticleChangeForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Article
        fields = {
            'title',
            'content',
        }
