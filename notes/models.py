from django.db import models

# Create your models here.
class NoteApp(models.Model):
    note_title = models.CharField(max_length=500)
    note_description = models.CharField(max_length=1200)

    def __str__(self):
        return self.note_title
    