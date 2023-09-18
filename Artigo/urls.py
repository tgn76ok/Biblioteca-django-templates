from django.urls import path
from .views import index,DetalheArtigo,Create,search,update,delete

app_name='artigo'

urlpatterns = [
    path('',index,name='index' ),
    path('search/', search, name='search'),  # type:ignore

    #CRUD
    path('Artigo/<int:pk>/detalhes/',DetalheArtigo,name='DetalheArtigo'),
    path('Artigo/Create/',Create,name='Create'),
    path('Artigo/<int:pk>/update/',update, name='update'),
    path('Artigo/<int:pk>/delete/',delete, name='delete'),


]
