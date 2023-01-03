from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(required=True, label="Name", max_length=10, 
#         error_messages={
#             "required":"Your name must not be empty",
#             "max_length":"Please enter a shorter name!"
#         })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=8000)
#     rating= forms.IntegerField(label="Rating", max_value=5, min_value=1)
    
class ReviewForm(forms.ModelForm): #django makes the form for you this time
    class Meta: 
        model = Review
        fields = '__all__' #get all fields plz
        #exclude = [''] #all fields except listed
        labels={
            "username":"Your name",
            "review_text": "Feeback:",
            "rating": "Rating"
        }
        error_messages={
            "username":{
                "required":"Your name must not be empty",
                "max_length":"Please enter a shorter name!"
            }
        }