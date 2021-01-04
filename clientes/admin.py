from django.contrib import admin
from .models import Funcionario, CPF, Telefone, Departamento

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'endereco', 'email')
    list_filter = ('id', 'nome', 'cpf', 'endereco', 'email', 'departamentos',)
    search_fields = ('id', 'nome', 'email', 'departamentos__nome')

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(CPF)
admin.site.register(Telefone)
admin.site.register(Departamento)
