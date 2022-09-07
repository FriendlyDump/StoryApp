from django.contrib import admin
from blog.models import Post, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'city')

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)