from django.db import models


class Book(models.Model):
    class CoverType(models.TextChoices):
        SOLID = "s", 'Solid'
        FLEXIBLE = "f", 'Flexible'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=50)
    cover = models.CharField(max_length=1, choices=CoverType.choices, default=CoverType.FLEXIBLE)
    publish_time = models.IntegerField()
    added_time = models.DateTimeField(auto_now_add=True)
    aupdated_time = models.DateTimeField(auto_now=True)
    isbn = models.CharField(max_length=13, null=True)
    rating = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return f'{self.title}, {self.author}'