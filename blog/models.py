from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

class BlogPost(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    img_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}: {self.author} "