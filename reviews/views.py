from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect 
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .forms import ReviewForm
from .models import Review

# views as methods:
# def review(request):
#     if request.method=="POST":
#         existing_model = Review.objects.get(pk=2)
#         form = ReviewForm(request.POST, instance=existing_model)
#         if form.is_valid():
#             form.save() #only availiable for modelform
#             return render(request,"thankyou.html")
#     else:
#         form = ReviewForm()
#         context = {
#             "form":form
#         }
#     return render(request, "review.html",context)

# def thankyou(request):
#     return render(request,"thankyou.html")


#views as class:

# class ReviewView(View): #access in urls.py with  views.ReviewView.as_view()
#     def get(self, request):
#         form = ReviewForm()
#         context = {
#             "form":form
#         }
#         return render(request, "review.html",context)

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thankyou")

#         return render(request, "review.html", {
#             "form": form
#         })

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "review.html"
#     success_url = "/reviews/thankyou"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    # fields="__all__" #like class meta in the formmodel. 
    #or:
    form_class = ReviewForm
    template_name ="review.html"
    success_url = "/reviews/thankyou"
    #so no need to manually save/valid and stuff

    
class ThankView(TemplateView):
    template_name = "thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Works!"
        return context


class ReviewsListView(ListView):
    template_name = "review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data



class SingleReviewView(DetailView):
    template_name = "single_review.html"
    model = Review
    