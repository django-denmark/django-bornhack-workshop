from django.db import models


class Task(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content

