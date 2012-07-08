import random
from django.db import models

class EnoughResponse(models.Model):

    text = models.TextField()
    # allow_sharing = models.BooleanField(default=True)
    when = models.DateTimeField(auto_now_add=True, editable=False)
    order = models.IntegerField(editable=False)

    def __unicode__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.order = random.randint(1, 50000)
        super(EnoughResponse, self).save(*args, **kwargs)

    class Meta:
        ordering = ("order",)