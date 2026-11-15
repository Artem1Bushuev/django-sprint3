from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name', 'slug')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'is_published')
        }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',
                    'location', 'pub_date', 'is_published')
    list_filter = ('is_published', 'pub_date', 'category', 'author')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)

    help_texts = {
        'is_published': 'Снимите галочку, чтобы скрыть публикацию.',
        'slug': (
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, '
            'дефис и подчёркивание.'
        ),
        'pub_date': (
            'Если установить дату и время в будущем, '
            'можно делать отложенные публикации.'
        ),
    }

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name in self.help_texts:
            field.help_text = self.help_texts[db_field.name]
        return field
