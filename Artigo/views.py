from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse

from django import forms

from Artigo.models import Artigo

def index(request):
    Artigos =  Artigo.objects \
        .filter(mostra=True)\
        .order_by('-id')

    paginator = Paginator(Artigos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    context = {
        'page_obj':page_obj,
        'site_title': 'Artigos - '

    }
    
    return render(
        request,
        'Artigo/pages/index.html',
        context
    )
    
    

def DetalheArtigo(request,pk):
    Artigos_unico = Artigo.objects.get(pk=pk)
    
    context = {
        'Artigo':Artigos_unico,
        'site_title': 'Artigo - '
    }
    
    return render(
        request,
        'Artigo/pages/Artigo.html',
        context
    )
    
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('artigo:index')

    artigos = Artigo.objects \
        .filter(mostra=True)\
        .filter(
            Q(Titulo__icontains=search_value) |
            Q(sinopse__icontains=search_value) |
            Q(Usuario_id__username__icontains=search_value) |
            Q(id__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(artigos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'Artigo/pages/index.html',
        context
    )

def Create(request):
    form_action = reverse('artigo:Create')

    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Criar - '
            
        }
        
        if form.is_valid():
            artigo = form.save()
            return redirect('artigo:update', pk=artigo.pk)

        
        return render(
            request,
            'Artigo/pages/create.html',
            context
        )
    context = {
        'form': ArtigoForm(),
        'form_action': form_action,

    }    
    return render(
        request,
        'Artigo/pages/create.html',
        context
    )
    
    
def update(request, pk):
    artigo = get_object_or_404(
        Artigo, pk=pk, mostra=True
    )
    form_action = reverse('artigo:update', args=(pk,))

    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            artigo = form.save()
            return redirect('artigo:update', Artigo_id=artigo.pk)

        return render(
            request,
            'Artigo/pages/create.html',
            context
        )

    context = {
        'form': ArtigoForm(instance=artigo),
        'form_action': form_action,
    }

    return render(
        request,
        'Artigo/pages/create.html',
        context
    )
    
def delete(request, pk):
    artigo = get_object_or_404(
        Artigo, pk=pk, mostra=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        artigo.delete()
        return redirect('artigo:index')

    return render(
        request,
        'Artigo/pages/Artigo.html',
        {
            'Artigo': artigo,
            'confirmation': confirmation,
        }
    )
    
class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ('Titulo',
                  'sinopse',
                  'data_criacao',
                  
                  'categoria',
                  'Usuario_id',
                  'Capa',
                  'pdf'
                  )
        
        
        
        
        
    def clean(self):
        cleaned_data = self.cleaned_data

        

        return super().clean()