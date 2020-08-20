from django.forms import ModelForm
from .models import Produtos

class FormProduto(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'preco', 'descricao', 'data_validade', 'quantidade']