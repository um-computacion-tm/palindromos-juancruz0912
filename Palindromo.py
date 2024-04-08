import unittest

#Utilizando una función creada por mi
""" def juntar(string):
     nuevo_string = ""
     for i in range(len(string)):
         if string[i] != " ":
             nuevo_string += string[i]
     return nuevo_string

def palindromo(string):
     string = juntar(string)
     print(string)
     for i in range(len(string)):  
         if string[i] != string[-(i+1)]:
             return False
     return True """

# Utilizando métodos de string
def palindromo(string):
    string = string.replace(" ","")
    for i in range(len(string)):  
        if string[i] != string[-(i+1)]:
            return False
    return True


class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = palindromo('a')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = palindromo('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = palindromo('ab')
        self.assertEqual(resultado, False)

    def test_aCa(self):
        resultado = palindromo('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = palindromo('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = palindromo('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = palindromo('ABCA')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = palindromo('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = palindromo('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = palindromo('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = palindromo('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = palindromo('neuqueM')
        self.assertEqual(resultado, False)

    def test_neuquene(self):
        resultado = palindromo('n euq uen')
        self.assertEqual(resultado, True)

unittest.main()
