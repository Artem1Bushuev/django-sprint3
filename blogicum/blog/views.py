from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category

# Константа для количества отображаемых постов
POSTS_PER_PAGE = 5


def get_published_posts():
    """Возвращает QuerySet опубликованных постов"""
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )


def index(request):
    """Главная страница — пять последних опубликованных публикаций."""
    # Убираем сортировку по дате публикации
    posts = get_published_posts()[:POSTS_PER_PAGE]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    """Страница категории — публикации выбранной категории."""
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug
    )
    posts = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category.html', context)


def post_detail(request, post_id):
    """Страница отдельной публикации."""
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
