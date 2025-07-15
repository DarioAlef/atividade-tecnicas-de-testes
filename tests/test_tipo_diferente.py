import pytest
from calcula_media import verificar_aprovacao

def test_passar_numero():
    notas = 8.5
    assert verificar_aprovacao(notas) == "Erro: A entrada deve ser uma lista de notas."
    
def test_passar_string():
    notas = "8.5, 9.0, 7.5, 6.0"
    assert verificar_aprovacao(notas) == "Erro: A entrada deve ser uma lista de notas."
    
def test_passar_lista_vazia():
    notas = []
    assert verificar_aprovacao(notas) == "Erro: A lista deve conter exatamente 4 notas."