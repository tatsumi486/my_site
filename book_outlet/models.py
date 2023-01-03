from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}, {self.code}"
    
    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street=models.CharField(max_length=80)
    zipcode=models.CharField(max_length=5)
    city=models.CharField(max_length=80)

    def __str__(self):
        return f"{self.street}, {self.zipcode} {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null = True)
     #since one to one, it won't return a set, just a single address

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    #author.book_set will be all the books that it needs (reverse many-to-one)
    #unless you have that other model marked with a "related_name", then just call it by the related name



class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="book") 
    #cascade is if author is deleted, also delete the the associated book
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling=models.BooleanField(default=False)
    published_country = models.ManyToManyField(Country, verbose_name=("Country"))
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #index makes the thing move faster

    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"