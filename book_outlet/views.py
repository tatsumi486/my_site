from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("author")
    total = books.count()
    avg_rate = books.aggregate(Avg("rating"))
    context = {
        "books": books,
        "total": total,
        "avg_rating": avg_rate
    }
    return render(request, "books/index.html", context)

def book_deets(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    }
    return render(request, "books/book_detail.html", context)