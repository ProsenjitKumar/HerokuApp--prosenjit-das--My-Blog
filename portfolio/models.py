from django.db import models
from django.utils.text import slugify


class Gallery(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='gallery/', blank=True)
    summary = models.TextField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=88)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    percentage = models.PositiveSmallIntegerField(verbose_name='percentage')
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    source_code = models.URLField(blank=True)
    done = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(prepopulate_from=('name',))

    def __str__(self):
        return self.name


class CurrentPosition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    source_code = models.URLField(blank=True)
    joined = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True)
    source_code = models.URLField(blank=True)
    joined = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EducationalBackground(models.Model):
    degree = models.CharField(max_length=30)
    institute = models.CharField(max_length=255)
    subject = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    board = models.CharField(max_length=30)
    present_session = models.CharField(max_length=60)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.degree


class Portfolio(models.Model):
    name = models.CharField(max_length=88)
    headline = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='portfolio/', blank=True)
    goal = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


