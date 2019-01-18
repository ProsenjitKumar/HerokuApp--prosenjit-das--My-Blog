from blog.models import BlogPost
from django import forms


class BlogPostSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search name or surname!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )
