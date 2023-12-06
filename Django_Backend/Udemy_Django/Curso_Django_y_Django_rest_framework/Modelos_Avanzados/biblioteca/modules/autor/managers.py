from django.db import models

class AuthorManager(models.Manager):
    def search_author(self, author_name):
        search_result = self.filter(name__icontains=author_name)
        return search_result