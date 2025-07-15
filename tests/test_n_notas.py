import pytest
from calcula_media import verificar_aprovacao

def test_menos_notas():
    notas = [8.0, 9.0, 7.5]  # Apenas 3 notas
    assert verificar_aprovacao(notas) == "Erro: A lista deve conter exatamente 4 notas."
    

def test_mais_notas():
    notas = [8.0, 9.0, 7.5, 9.5, 6.0]  # 5 notas
    assert verificar_aprovacao(notas) == "Erro: A lista deve conter exatamente 4 notas."