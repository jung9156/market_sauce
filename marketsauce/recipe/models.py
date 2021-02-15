from django.db import models
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= "user_recipe")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_recommend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="recommend_recipe", blank=True)
    user_favorit = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="favorit_recipe", blank=True)


class Recipe_Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= "user_reply")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_first_reply")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    