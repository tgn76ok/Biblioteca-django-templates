from django.contrib import admin
from Artigo import models
# Register your models here.
@admin.register(models.Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    #aparece no diplay
    list_display =('Titulo','envio_date','data_criacao','Usuario_id','mostra')
    #adicona um filter
    # list_filter = ('envio_date',)
    #adiciona os campos de pesquisas
    search_fields = 'Titulo','envio_date'
    
    
    list_per_page = 5
    
    list_max_show_all = 50
    
    list_editable = ('envio_date','mostra')
    
@admin.register(models.CategoriaArtigos)
class ArtigoAdmin(admin.ModelAdmin):
    list_display =('nome',)