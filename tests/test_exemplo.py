from calcula_media import verificar_aprovacao

def test_aprovado_particao_equivalencia():
    assert verificar_aprovacao([8.0, 9.0, 7.5, 9.5]) == 'Aprovado'