from django.db import models


class NewsLetterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class NewsLetter(models.Model):
    EMAIL_STATUS_CHOICE = (
        ("Draft", "Draft"),
        ("Published", "Published"),
    )

    subject = models.CharField(max_length=299)
    content = models.TextField()
    email = models.ManyToManyField(NewsLetterUser)
    status = models.CharField(max_length=11, choices=EMAIL_STATUS_CHOICE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject