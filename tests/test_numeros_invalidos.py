import pytest
from calcula_media import verificar_aprovacao

def test_passar_numeros_invalidos():
    notas = [8.0, "1.0", 7.5, 9.5]  # Nota negativa
    assert verificar_aprovacao(notas) == "Erro: Todas as notas devem ser números entre 0 e 10."
    
