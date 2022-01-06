from django.contrib.auth.models import User
from django.db.models import Model
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import BooleanField
from django.db.models import ForeignKey
from django.db.models import PROTECT
from django.db.models import DateTimeField
from django.db.models import IntegerField

# Create your models here.


class Movie(Model):
    titulo_filme = CharField(max_length=255, verbose_name='Título')
    ano_filme = IntegerField(verbose_name='Ano')
    descricao_filme = TextField(verbose_name='Descrição')
    ganhou_oscar = BooleanField(default=False, verbose_name='Ganhou Oscar?')

    choices = (('S', 'Sim'), ('N', 'Não'))
    idade_permitida = CharField(
        max_length=3, choices=choices, verbose_name='Maior de 18 anos?')
    usuario = ForeignKey(User, on_delete=PROTECT)
    data_criacao = DateTimeField(
        blank=True, null=True, verbose_name='Data de publicação')
