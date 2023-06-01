from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from blog.models import Category, Tag, Post, Recipe, Comment


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'create_at')
    list_display_links = ('title',)
    inlines = (RecipeInline,)
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', 'post')


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website', 'create_at')
    list_display_links = ('name',)


admin.site.register(Tag)
