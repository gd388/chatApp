from django.db import models
import random
from django.utils.text import slugify

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True, null=True)

    def save(self, *args, **kwargs):
        # If the slug is not set or is empty, generate it
        if not self.slug:
            self.slug = slugify(self.name + self.name[0:2] + str(random.randint(1, 1000)))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
