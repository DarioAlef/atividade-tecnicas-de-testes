import pytest
from calcula_media import verificar_aprovacao

def test_passar_numeros_invalidos():
    notas = [8.0, "1.0", 7.5, 9.5]  # String em vez de número
    assert verificar_aprovacao(notas) == "Erro: A lista deve conter apenas números reais."
    
