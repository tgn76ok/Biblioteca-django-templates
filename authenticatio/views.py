from django.shortcuts import render

# Create your views here.
def index(request):
    # Artigos =  Artigo.objects \
    #     .filter(mostra=True)\
    #     .order_by('-id')

    # paginator = Paginator(Artigos, 10)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    
    # context = {
    #     'page_obj':page_obj,
    #     'site_title': 'Artigos - '

    # }
    
    return render(
        request,
        'authenticatio/index.html',
        # context
    )