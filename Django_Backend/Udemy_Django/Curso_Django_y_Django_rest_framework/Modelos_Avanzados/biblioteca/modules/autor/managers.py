from django.db import models

class AuthorManager(models.Manager):
    def list_authors(self):
        return self.all()