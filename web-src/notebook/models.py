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
