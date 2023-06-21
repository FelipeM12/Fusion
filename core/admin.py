from django.contrib import admin

from .models import Cargo, Sevico, Equipe, Feactures

#modo de visão no Admin(localhost/admin)
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Sevico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Equipe)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Feactures)
class Feactures(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone', 'ativo')
