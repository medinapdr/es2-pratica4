import unittest
from valida_cpf import valida_cpf

class TestValidaCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(valida_cpf("880.767.100-06"))
        self.assertTrue(valida_cpf("209.344.950-17"))

    def test_cpf_invalido(self):
        self.assertFalse(valida_cpf("123.456.789-00"))
        self.assertFalse(valida_cpf("111.222.333-45"))

    def test_cpf_com_caracteres_invalidos(self):
        self.assertFalse(valida_cpf("abc.def.ghi-jk"))
        self.assertFalse(valida_cpf("1234-5678@9"))

    def test_cpf_com_tamanho_incorreto(self):
        self.assertFalse(valida_cpf("123.456.789"))
        self.assertFalse(valida_cpf("123.456.789-1234"))

if __name__ == '__main__':
    unittest.main()
