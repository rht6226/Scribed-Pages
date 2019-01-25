from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()


class NoteBook(models.Model):

    id = models.CharField(max_length=12, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=150)
    description = RichTextField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    private = models.BooleanField(default=True)

    class Meta:
        db_table = 'notebooks'
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'

    def __str__(self):
        return self.name


class Article(models.Model):
    notebook = models.ForeignKey(NoteBook, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(serialize=True, null=True)
    title = models.CharField(null=True, max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(null=True)
    source = models.CharField(null=True, max_length=700)

    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return "{} - {}".format(self.notebook.name, self.index)
