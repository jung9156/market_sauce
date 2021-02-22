from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Recipe_Reply
from .forms import RecipeForm, ReplyForm
from user.models import Profile
# Create your views here.

#index는 첫 페이지 (read 후에)
def index(request):
    user = request.user
    recipe = Recipe.objects.all()
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipe/index.html', context)


def write(request):
    user = request.user
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = user
            recipe.save()
            return redirect('recipe:detail', recipe.pk)
    else:
        form = RecipeForm()
        context = {
            'form': form,
            'update': False,
        }
    return render(request, 'recipe/form.html', context)


def detail(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    reply = Recipe_Reply.objects.filter(recipe=recipe)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.recipe = recipe
            reply.save()
            return redirect('recipe:detail', recipe.pk)
    else:
        form = ReplyForm()
        context = {
            'recipe': recipe,
            'reply': reply,
            'form': form,
            'update': False,
        }
    return render(request, 'recipe/detail.html', context)


def detail_reply_u(request, recipe_pk, reply_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    reply_up = get_object_or_404(Recipe_Reply, pk=reply_pk)
    reply = Recipe_Reply.objects.filter(recipe=recipe)
    if reply_up.user == request.user:
        if request.method == 'POST':
            form = ReplyForm(request.POST, instance=reply_up)
            if form.is_valid():
                reply_up.save()
                return redirect('recipe:detail', recipe.pk)
        else:
            form = ReplyForm(instance=reply_up)
        
        context = {
            'form': form,
            'recipe': recipe,
            'reply': reply,
            'update': True,
        }
        return render(request, 'recipe/detail.html', context)
    return redirect('recipe:detail', recipe.pk)


def detail_reply_d(request, recipe_pk, reply_pk):
    reply_up = get_object_or_404(Recipe_Reply, pk=reply_pk)
    if reply_up.user == request.user:
        reply_up.delete()
    
    return redirect('recipe:detail', recipe_pk)


def update(request, recipe_pk, user_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    if recipe.user.pk == user_pk:
        if request.method == 'POST':
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                recipe.save()
                return redirect('recipe:detail', recipe.pk)
        else:
            form = RecipeForm(instance=recipe)
        context = {
            'form': form,
            'update': True,
            'recipe': recipe,
        }
        return render(request, 'recipe/form.html', context)

    else:
        # 메세지 띄우기
        msg = '권한이 부족합니다.'
        context = {
            'msg': msg
        }
        return redirect('recipe:detail', recipe.pk)

# 추후 삭제시 이메일 확인을 통해 실행 하도록 바꿀 것(모달 형태)
def delete(request, recipe_pk, user_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    if recipe.user.pk == user_pk:
        recipe.delete()
        return redirect('recipe:index')
    else:
        return redirect('recipe:detail', recipe.pk)


def recommend(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    user = request.user
    if user in recipe.user_recommend.all():
        recipe.user_recommend.remove(user)
        recipe.recommend_count -= 1
        recipe.save()
    else:
        recipe.user_recommend.add(user)
        recipe.recommend_count += 1
        recipe.save()
    return redirect('recipe:detail', recipe.pk)
    #이러면 수정이 된것으로 보이나?