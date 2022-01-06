from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from filmes_preferidos.models import Movie

# Register your models here.


class MovieAdmin(ModelAdmin):
    list_display = ['titulo_filme', 'ano_filme', 'ganhou_oscar']


site.register(Movie, MovieAdmin)
