from django.shortcuts import render, get_object_or_404

from .models import Group, Post

# Можно лучше:
# рассказываем про magic numbers и рекомендуем вынести число в константы
POSTS_PER_PAGE = 10


def index(request):
    # Можно лучше:
    # тут можно вбросить про select related,
    # расскажут про него дальше по курсу.
    latest = Post.objects.select_related('group')[:POSTS_PER_PAGE]
    return render(request, 'posts/index.html', {'posts': latest})


def group_posts(request, slug):
    # "Надо исправить":
    # Тут просим удалить комменты, которые они копипастят из урока.
    # Это несодержательные комменты,
    # они нужны в учебных целях, в продакшн коде такое оставлять не нужно.
    group = get_object_or_404(Group, slug=slug)

    # "Можно лучше": рассказываем, зачем же мы все-таки сделали related_name
    # в модели, рассказываем про такую запись вместо того, что дают в уроке
    posts = group.posts.all()[:POSTS_PER_PAGE]
    return render(
        request,
        'posts/group_list.html',
        {'group': group, 'posts': posts}
    )
