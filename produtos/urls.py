from django.urls import path
from .views import lista_produtos, novo_produto, atualiza_produto, deleta_produto

urlpatterns = [
    path('lista/', lista_produtos, name="lista_produtos"),
    path('novo/', novo_produto, name="novo_produto"),
    path('atualiza/<int:id>/', atualiza_produto, name="atualiza_produto"),
    path('excluir/<int:id>/', deleta_produto, name="deleta_produto"),
]