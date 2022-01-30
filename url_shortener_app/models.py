from django.db import models
from utils import create_shortened_url


# Create your models here.
class UrlShortener(models.Model):
    short_url = models.CharField(max_length=15)
    long_url = models.URLField()
    click_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super(UrlShortener, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.short_url} from {self.long_url}'