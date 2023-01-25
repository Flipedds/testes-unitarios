import mostrar


class TestClass:
    def test_somar(self):
        assert mostrar.somar(5, 6) == 11

    def test_mostrar(self):
        assert mostrar.mostrar('filipe') == 'filipe'

    def test_hello(self):
        assert mostrar.hello_word('filipe') == 'hello word, filipe'

    def test_split(self):
        assert mostrar.split('filipe andre') == ['filipe', 'andre']

    def test_maior_menor(self):
        assert mostrar.maior_menor(2, 8) == 'y maior'

    def test_recebe(self):
        assert mostrar.recebe(1, 7) == 8
