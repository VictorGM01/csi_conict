from django.shortcuts import render


def index(request):
    return render(request, "artigos/geral_artigos.html")


def desenvolvedores(request):
    return render(request, "principal/desenvolvedores.html")


def instituicao(request):
    return render(request, "principal/instituicao.html")


def sitemap(request):
    return render(request, 'sitemap.xml', content_type='xml')


def termos_de_uso(request):
    return render(request, "principal/termos_de_uso.html")


def politica_de_privacidade(request):
    return render(request, "principal/politica_de_privacidade.html")