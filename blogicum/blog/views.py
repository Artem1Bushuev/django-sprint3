from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    """Главная страница — пять последних опубликованных публикаций."""
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    """Страница категории — публикации выбранной категории."""
    # Получаем категорию или 404, если она не опубликована
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug
    )
    # Выбираем публикации категории с учётом условий
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category.html', context)


def post_detail(request, pk):
    """Страница отдельной публикации."""
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ),
        pk=pk
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
