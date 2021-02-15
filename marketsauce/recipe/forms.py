from django import forms
from .models import Recipe, Recipe_Reply

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Recipe_Reply
        fields = ['content']