import pytest
from tests.conftest import sample_parameter
from calcula_media import verificar_aprovacao

# Teste de partição de equivalência

def test_aprovado(sample_parameter):
    sample_parameter[0] = 8.0
    sample_parameter[1] = 9.0
    sample_parameter[2] = 7.5
    sample_parameter[3] = 9.5
    assert verificar_aprovacao(sample_parameter) == 'Aprovado'
    
def test_recuperacao(sample_parameter):
    sample_parameter[0] = 6.0
    sample_parameter[1] = 5.5
    sample_parameter[2] = 7.0
    sample_parameter[3] = 6.5
    assert verificar_aprovacao(sample_parameter) == 'Recuperação'
    
def test_reprovado(sample_parameter):
    sample_parameter[0] = 4.0
    sample_parameter[1] = 3.5
    sample_parameter[2] = 5.0
    sample_parameter[3] = 2.0
    assert verificar_aprovacao(sample_parameter) == 'Reprovado'